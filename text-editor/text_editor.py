import tkinter as tk
from tkinter import filedialog, messagebox

current_file = None

# ---------------------- FILE OPERATIONS ----------------------

def new_file():
    global current_file
    text.delete(1.0, tk.END)          # Remove all text
    current_file = None               # No file is currently associated
    root.title("Simple Text Editor")  # Reset window title

def open_file():
    global current_file

    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)      # Clear existing text
            text.insert(tk.END, file.read())  # Insert file content

        current_file = file_path
        root.title(f"Simple Text Editor - {file_path}")

def save_file():
    global current_file

    if current_file:
        with open(current_file, 'w') as file:
            file.write(text.get(1.0, tk.END))

        messagebox.showinfo("Info", "File saved successfully!")

    else:
        save_as_file()

def save_as_file():
    global current_file

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

        current_file = file_path
        root.title(f"Simple Text Editor - {file_path}")

        messagebox.showinfo("Info", "File saved successfully!")

# ---------------------- EDIT OPERATIONS ----------------------

def cut_text():
    text.event_generate("<<Cut>>")

def copy_text():
    text.event_generate("<<Copy>>")

def paste_text():
        text.event_generate("<<Paste>>")

# ---------------------- TOOLS ----------------------

def show_word_count():  
    content = text.get(1.0, tk.END)
    words = len(content.split())

    messagebox.showinfo("Word Count", f"Total words: {words}")

def show_character_count():  
    content = text.get(1.0, tk.END)

    characters = len(content.rstrip("\n"))

    messagebox.showinfo(
        "Character Count",
        f"Total characters: {characters}"
    )

# ---------------------- MAIN WINDOW ----------------------

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# ---------------------- MENU BAR ----------------------

menu = tk.Menu(root)
root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Tools Menu
tools_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Tools", menu=tools_menu)

tools_menu.add_command(label="Word Count", command=show_word_count)
tools_menu.add_command(label="Character Count", command=show_character_count)

# ---------------------- TEXT AREA ----------------------

text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12),
    fg="blue"
)

text.pack(expand=tk.YES, fill=tk.BOTH)

# ---------------------- RUN APPLICATION ----------------------

root.mainloop()