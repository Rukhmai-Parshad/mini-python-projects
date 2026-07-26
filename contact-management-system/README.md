# Contact Management System

A modular Contact Management System built with Python for efficiently storing and managing contact information.

The application allows users to create, view, search, update, and delete contacts while maintaining clean code organization through separate modules for configuration, validation, logging, and data export. Contact data is stored in a JSON file, making the application lightweight and easy to use without requiring a database server.

This project demonstrates practical Python programming concepts, modular application design, input validation, structured logging, and file-based data management.

---

## Features

- Add new contacts
- View all contacts
- Search contacts by name
- Update existing contacts
- Delete contacts
- Validate user input
- Store contact data in JSON format
- Export contacts to CSV
- Export contacts to Excel
- Application logging
- Modular project architecture
- Exception handling

---

## Technologies Used

- Python 3
- JSON
- Pandas
- OpenPyXL

---

## Software Engineering Concepts

This project demonstrates:

- Modular Programming
- Separation of Concerns
- JSON Data Management
- File Handling
- Input Validation
- Logging
- Exception Handling
- Data Export
- Code Reusability
- Maintainable Project Structure

---

## Project Structure

```text
contact-management-system/
│
├── logs/
│   └── app.log
│
├── screenshots/
│
├── config.py
├── export.py
├── logger.py
├── validators.py
├── main.py
├── contacts.json
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rukhmai-Parshad/python-projects.git
```

Navigate to the project directory:

```bash
cd python-projects/contact-management-system
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Usage

Launch the application and select the desired option from the menu.

Typical workflow:

1. Create a contact.
2. View saved contacts.
3. Search contacts.
4. Update contact information.
5. Delete contacts.
6. Export contacts to CSV or Excel.

---

## Screenshots

Project screenshots are available in the **screenshots/** directory.

---

## Key Highlights

- Clean and modular architecture
- JSON-based data storage
- Reusable Python modules
- Structured logging
- Input validation
- CSV and Excel export
- Organized project structure
- Easy to maintain and extend

---

## Future Improvements

Potential enhancements include:

- SQLite database support
- Contact categories
- Import contacts from CSV
- Backup and restore functionality
- Unit testing
- Password-protected access
- Advanced search filters
- Graphical user interface (GUI)

---

## License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

## Author

**Rukhmai Parshad**

GitHub: https://github.com/Rukhmai-Parshad