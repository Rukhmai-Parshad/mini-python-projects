import sqlite3

def create_connection():
    return sqlite3.connect("tasks.db")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def display_task(task):
    print("-" * 35)
    print(f"ID       : {task[0]}")
    print(f"Task     : {task[1]}")
    print(f"Priority : {task[2]}")
    print(f"Status   : {task[3]}")    

def add_task(task_name, priority):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks(task_name, priority, status)
        VALUES (?, ?, ?)
    """, (task_name, priority, "Pending"))

    connection.commit()
    print("Task added successfully!")
    connection.close()

def view_tasks():
    connection = create_connection()
    cursor  = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks found!")
    else:
        for task in tasks:
            display_task(task)

    connection.close()            

def update_task(task_id, task_name, priority, status):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET task_name = ?, priority = ?, status = ?
        WHERE id = ?
        """, (task_name, priority, status, task_id))

    if cursor.rowcount == 0:
        print("Task ID not found!")
    else:
        print("Task updated successfully!")

    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = create_connection()
    cursor = connection.cursor()    

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
        """, (task_id,))

    if cursor.rowcount == 0:
        print("Task ID not found!")
    else:
        print("Task deleted successfully!")
        
    connection.commit()
    connection.close()

def search_task(keyword):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM tasks
        WHERE task_name LIKE ?
    """, (f"%{keyword}%",))

    tasks = cursor.fetchall()
    if not tasks:
        print("No matching task found!")

    else:
        for task in tasks:
            display_task(task)

    connection.close()    
