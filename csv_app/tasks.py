from celery import shared_task
import pandas as pd
from django.core.cache import cache

@shared_task
def process_csv(file_path):
    df = pd.read_csv(file_path)

    # Identify numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns

    results = {}
    for col in numeric_columns:
        results[col] = {
            "sum": df[col].sum(),
            "average": df[col].mean(),
            "count": df[col].count(),
        }
    
    # Store in cache for dynamic display
    cache.set("processed_results", results, timeout=3600)
    return results
