import csv
import pandas as pd

from config import CSV_PATH, EXCEL_PATH


def prepare_data(contacts):
    data = []

    for name, contact in contacts.items():
        data.append({
            "Name": name,
            "Age": contact["age"],
            "Email": contact["email"],
            "Mobile": contact["mobile"]
        })

    return data


def export_to_csv(contacts):
    data = prepare_data(contacts)

    with open(CSV_PATH, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Age",
            "Email",
            "Mobile"
        ])

        for row in data:
            writer.writerow([
                row["Name"],
                row["Age"],
                row["Email"],
                row["Mobile"]
            ])


def export_to_excel(contacts):

    data = prepare_data(contacts)

    if not data:
        print("No contacts available to export!")
        return

    df = pd.DataFrame(data)

    df.to_excel(EXCEL_PATH, index=False)