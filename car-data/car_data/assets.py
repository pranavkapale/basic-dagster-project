import dagster as dg
import polars as pl
import duckdb


CSV_URL = "https://raw.githubusercontent.com/Azure/carprice/refs/heads/master/dataset/carprice.csv"
CSV_PATH = "data/carprice.csv"

DUCKDB_PATH = "data/car_data.duckdb"
TABLE_NAME = "avg_price_per_brand"

@dg.asset
def car_data_file(context: dg.AssetExecutionContext):
    """Download the dataset from the given URL and load it into a Polars DataFrame."""
    context.log.info(f"Downloading dataset from {CSV_URL}")
    df = pl.read_csv(CSV_URL)
    df = df.with_columns([
        pl.col('normalized-losses').cast(pl.Float64, strict=False),
        pl.col('price').cast(pl.Float64, strict=False)
    ])
    df.write_csv(CSV_PATH)

@dg.asset(deps={"car_data_file": dg.AssetIn()})
def car_data(context: dg.AssetExecutionContext):
    """Load the car data from the CSV file into a Polars DataFrame."""
    context.log.info(f"Creating aggregated DuckDB table from {CSV_PATH}")
    df = pl.read_csv(CSV_PATH)
    df = df.drop_nulls(['price', 'normalized-losses'])
    
    # Compute average price per brand
    avg_price_df = df.group_by('make').agg(pl.col('price').mean().alias('average_price'))
    context.log.info(f"Computed average prices for {avg_price_df.height} brands")

    # Store data in Duck DB 
    # Convert data to list of tuples for insertion
    data_tuples = [(row["make"], row["average_price"]) for row in avg_price_df.to_dicts()]

    with duckdb.connect(DUCKDB_PATH) as conn:
        conn.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                make VARCHAR,
                average_price FLOAT
            )
        """)
        # Insert data into the table
        conn.executemany(f"INSERT INTO {TABLE_NAME} (make, average_price) VALUES (?, ?)", data_tuples)