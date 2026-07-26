import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JSON_PATH = os.path.join(BASE_DIR, "contacts.json")
CSV_PATH = os.path.join(BASE_DIR, "contacts.csv")
EXCEL_PATH = os.path.join(BASE_DIR, "contacts.xlsx")

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")