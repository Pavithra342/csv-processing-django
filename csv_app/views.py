from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd

def upload_csv(request):
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        
        # Save file
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        file_path = fs.path(filename)

        # Read CSV and process data
        try:
            df = pd.read_csv(file_path)

            column_names = df.columns.tolist()
            sum_values = df.sum(numeric_only=True).tolist()
            avg_values = df.mean(numeric_only=True).tolist()
            count_values = df.count().tolist()

            processed_data = zip(column_names, sum_values, avg_values, count_values)

            return render(request, "upload.html", {
                "processed_data": processed_data,
                "file_uploaded": True
            })

        except Exception as e:
            return render(request, "upload.html", {
                "error": f"Error processing file: {str(e)}",
                "file_uploaded": False
            })

    return render(request, "upload.html", {"file_uploaded": False})
