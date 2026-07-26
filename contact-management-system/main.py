import json
from logger import log_info, log_warning
from export import export_to_csv, export_to_excel
from config import JSON_PATH



from validators import (
    is_valid_age,
    is_valid_mobile,
    is_valid_email,
    is_valid_name
)


def load_contacts() -> dict:
    """
    Load all contacts from the JSON file.
    """
    try:
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts(data: dict) -> None:
    """
    Save contacts to the JSON file.
    """
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=4)

contacts = load_contacts()

def email_exists(email: str, current_name: str = None) -> bool:
    for name, contact in contacts.items():
        if current_name and name == current_name:
            continue
        if contact["email"].lower() == email.lower():
            return True
    return False


def mobile_exists(mobile: str, current_name: str = None) -> bool:
    for name, contact in contacts.items():
        if current_name and name == current_name:
            continue
        if contact["mobile"] == mobile:
            return True
    return False


while True:
    print("\n" + "=" * 20 + " Contact Management System " + "=" * 20)
    print()

    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Export to CSV")
    print("8. Export to Excel")
    print("9. Exit")
    print()

    try:
        choice = int(input("Enter your choice: "))
        print()
    except ValueError:
        print("Enter a valid number!\n")
        continue

    # Create Contact
    if choice == 1:
        name = input("Enter your name:\n").strip()
        print()

        if not is_valid_name(name):
            print("Name must be between 2 and 50 characters.\n")
            continue

        if name in contacts:
            log_warning(f"Duplicate contact creation attempt: {name}")
            print("Contact already exists!\n")
            continue

        age = input("Enter age:\n")
        print()

        if not is_valid_age(age):
            log_warning(f"Invalid age entered for {name}: {age}")
            print("Invalid age.\n")
            continue

        email = input("Enter email:\n").strip()
        print()

        if not is_valid_email(email):
            log_warning(f"Invalid email entered for {name}: {email}")
            print("Invalid email format!\n")
            continue

        if email_exists(email):
            log_warning(f"Duplicate email attempt: {email}")
            print("Email already exists!\n")
            continue

        mobile = input("Enter mobile number:\n").strip()
        print()

        if not is_valid_mobile(mobile):
            log_warning(f"Invalid mobile entered for {name}: {mobile}")
            print("Mobile must be 10 digits.\n")
            continue

        if mobile_exists(mobile):
            log_warning(f"Duplicate mobile attempt: {mobile}")
            print("Mobile number already exists!\n")
            continue

        contacts[name] = {
            "age": int(age),
            "email": email,
            "mobile": mobile
        }

        save_contacts(contacts)

        log_info(f"Contact created: {name}")
        print("Contact created successfully!\n")

    # View Contact
    elif choice == 2:
        name = input("Enter contact name:\n").strip()

        if name in contacts:
            contact = contacts[name]

            log_info(f"Contact viewed: {name}")

            print("\nContact Details")
            print()
            print("-" * 30)
            print(f"Name   : {name}")
            print(f"Age    : {contact['age']}")
            print(f"Email  : {contact['email']}")
            print(f"Mobile : {contact['mobile']}")
            print("-" * 30)
        

        else:
            log_warning(f"View failed - contact not found: {name}")
            print("Contact not found!\n")

    # Update Contact
    elif choice == 3:
        name = input("Enter name to update: ").strip()

        if name in contacts:
            age = input("Enter new age: ")

            if not is_valid_age(age):
                print("Invalid age!\n")
                continue

            email = input("Enter new email: ").strip()

            if not is_valid_email(email):
                print("Invalid email format!\n")
                continue

            if email_exists(email, name):
                print("Email already exists!\n")
                continue

            mobile = input("Enter new mobile number: ").strip()

            if not is_valid_mobile(mobile):
                print("Mobile must be 10 digits.\n")
                continue

            if mobile_exists(mobile, name):
                print("Mobile number already exists!\n")
                continue

            contacts[name] = {
                "age": int(age),
                "email": email,
                "mobile": mobile
            }

            save_contacts(contacts)

            log_info(f"Contact updated: {name}")
            print("Updated successfully!\n")

        else:
            log_warning(f"Update failed - contact not found: {name}")
            print("Contact not found!\n")

    # Delete Contact
    elif choice == 4:
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            save_contacts(contacts)

            log_info(f"Contact deleted: {name}")
            print("Deleted successfully!\n")

        else:
            log_warning(f"Delete failed - contact not found: {name}")
            print("Contact not found!\n")

    # Search Contact
    elif choice == 5:
        search = input("Search name: ").strip()

        found = False

        print()

        for name, contact in contacts.items():
            if search.lower() in name.lower():
                print(f"Name   : {name}")
                print(f"Age    : {contact['age']}")
                print(f"Email  : {contact['email']}")
                print(f"Mobile : {contact['mobile']}")
                print("-" * 30)
                found = True

        if not found:
            log_warning(f"No search result found for: {search}")
            print("No match found!\n")
        else:
            print()

    # Count Contact
    elif choice == 6:
        print(f"Total Contacts: {len(contacts)}\n")

    # Export to CSV
    elif choice == 7:
        export_to_csv(contacts)
        log_info("Contacts exported to CSV")
        print("Contacts exported successfully!\n")

    # Export to Excel
    elif choice == 8:
        export_to_excel(contacts)
        log_info("Contacts exported to Excel")
        print("Contacts exported successfully!\n")

    # Exit
    elif choice == 9:
        print("Exiting application...\n")
        break

    else:
        print("Invalid choice!\n")