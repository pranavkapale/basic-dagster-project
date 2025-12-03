import dagster as dg
from .jobs import car_price_job

car_price_schedule = dg.ScheduleDefinition(
    name="car_price_schedule",
    job=car_price_job,
    cron_schedule="* * * * *",  # Every Sunday at midnight
)