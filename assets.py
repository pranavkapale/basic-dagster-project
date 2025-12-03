import dagster as dg

@dg.asset
def process_data():
    # Simulate data processing
    data = [1, 2, 3, 4, 5]
    processed_data = [x * 2 for x in data]
    return processed_data

@dg.asset
def summarize_data(process_data):
    # Summarize the processed data
    summary = {
        "count": len(process_data),
        "sum": sum(process_data),
        "average": sum(process_data) / len(process_data)
    }
    return summary

@dg.asset(deps ={"summarize_data": dg.AssetIn()})
def report_data(summarize_data):
    # Generate a report based on the summary
    report = f"Data Summary:\nCount: {summarize_data['count']}\nSum: {summarize_data['sum']}\nAverage: {summarize_data['average']}"
    print(report)
    return report

defs = dg.Definitions(assets=[process_data, summarize_data, report_data])