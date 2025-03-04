# 📂 CSV Processing Django Project

This project allows users to **upload CSV files**, process them **asynchronously using Celery and Redis**, and view the processed results dynamically.

---

## 🚀 **Project Features**
✅ Upload CSV files from the frontend  
✅ Process CSV data asynchronously using **Celery & Redis**  
✅ Perform **sum, average, and count** calculations on the uploaded data  
✅ Display real-time results dynamically on the frontend  

---

## 🔧 **Setup Instructions**

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Pavithra342/csv-processing-django.git

cd csv-processing-django

2️⃣Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Database Migrations
python manage.py migrate

5️⃣ Start Redis Server
redis-server  # For Mac/Linux

6️⃣ Start Celery Worker
celery -A csv_project worker --loglevel=info

7️⃣ Run Django Development Server
python manage.py runserver

🛠 Technologies Used
Django – Backend framework
Celery – Asynchronous task processing
Redis – Task queue management
Bootstrap – Frontend styling
