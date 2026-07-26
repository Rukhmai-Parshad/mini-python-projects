import os
import time

def create_file(filename):
    try:
        with open (filename, 'x') as f:
            print(f"'{filename}' created successfully.")
            print()

    except FileExistsError:
        print(f"'{filename}' already exists.")
        print()

    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir()

    if not files:
        print("No files found.")
        print()
    else:
        print("Files in current directory")
        print("-" * 35)

        for file in files:
            if os.path.isfile(file):
                print(file)

        print("-" * 35)
        print()

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"'{filename}' deleted successfully.")
        print()

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if not content:
                print("The file is empty.")
                print()
            else:
                print("-" * 50)
                print(f"Contents of '{filename}'")
                print("-" * 50)
                print(content)
                print("-" * 50)
                print()

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter text to append: ")
            print()
            f.write(content + "\n")
            print(f"Content added successfully to '{filename}'.")
            print()

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print(f"An error occurred: {e}")   

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"'{old_name}' renamed to '{new_name}'.")
        print()

    except FileNotFoundError:
        print(f"{old_name} doesn't exist!")

    except FileExistsError:
        print(f"{new_name} already exists!")

    except Exception as e:
        print(f"An error occurred: {e}")

def file_details(filename):
    try:
        size = os.path.getsize(filename)
        modified = os.path.getmtime(filename)

        print("-" * 40)
        print("File Details")
        print("-" * 40)
        print(f"File Name      : {filename}")
        print(f"Size           : {size} bytes")
        print(f"Last Modified  : {time.ctime(modified)}")
        print("-" * 40)
        print()

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print(f"An error occurred: {e}")   

def search_file(keyword):
    files = os.listdir()
    found = False

    print("Matching Files")
    print("-" * 35)

    for file in files:
        if os.path.isfile(file) and keyword.lower() in file.lower():
            print(file)
            found = True

    print("-" * 35)
    print()

    if not found:
        print("No matching file found!")    

def file_statistics(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()

            words = len(content.split())
            lines = len(content.splitlines())

            print("-" * 35)
            print("File Statistics")
            print("-" * 35)
            print(f"Word Count : {words}")
            print(f"Line Count : {lines}")
            print("-" * 35)
            print()

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\n" + "=" * 25 + " File Management System " + "=" * 25)
        print()

        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Rename File")
        print("7. File Details")
        print("8. Search File")
        print("9. File Statistics")
        print("10. Exit")

        print()

        choice = input("Enter your choice (1-10): ")
        print()

        if choice == '1':
            filename = input("Enter file name: ")
            print()
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter file name to delete: ")
            print() 
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter file name: ")
            print()
            read_file(filename) 

        elif choice == '5':
            filename = input("Enter file name: ")
            print()
            edit_file(filename) 

        elif choice == '6':
            old_name = input("Enter current file name: ")
            new_name = input("Enter new file name: ")
            print()
            rename_file(old_name, new_name)

        elif choice == '7':
            filename = input("Enter the file name for file details: ")
            file_details(filename)             

        elif choice == '8':
            keyword = input("Enter file name to search: ")
            print()   
            search_file(keyword)

        elif choice == '9':
            filename = input("Enter file name: ")
            file_statistics(filename)

        elif choice == '10':
            print()
            print("Thank you for using File Management System.")
            print("Application closed successfully.")
            print()
            break                 

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")
            print()

if __name__=="__main__":
    main()

