

from google.cloud import bigquery
from google.api_core.exceptions import NotFound

def create_meals_table_if_needed():
    client = bigquery.Client()
    table_id = "vocal-spirit-372618.diet_data.meals"  # Replace with your own project/dataset

    schema = [
        bigquery.SchemaField("timestamp", "DATETIME", mode="REQUIRED"),
        bigquery.SchemaField("user_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("meal_description", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("calories", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("protein_g", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("carbs_g", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("fat_g", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("raw_response", "STRING", mode="REQUIRED"),
    ]

    try:
        client.get_table(table_id)
        print("✅ Table already exists.")
    except NotFound:
        table = bigquery.Table(table_id, schema=schema)
        client.create_table(table)
        print(f"✅ Created table {table_id}")


from datetime import datetime

def insert_meal_to_bq(user_id, meal, nutrition_data, raw_response):
    client = bigquery.Client()
    table_id = "vocal-spirit-372618.diet_data.meals"

    row = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "meal_description": meal,
        "calories": nutrition_data.get("calories"),
        "protein_g": nutrition_data.get("protein_g"),
        "carbs_g": nutrition_data.get("carbs_g"),
        "fat_g": nutrition_data.get("fat_g"),
        "raw_response": raw_response
    }

    errors = client.insert_rows_json(table_id, [row])
    if errors:
        print("❌ BigQuery insert errors:", errors)
    else:
        print("✅ Meal inserted into BigQuery.")


