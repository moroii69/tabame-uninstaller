import os
import shutil
import tkinter as tk
from tkinter import messagebox

def delete_file(file_path, listbox):
    """Delete a single file and update the listbox."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            listbox.insert(tk.END, f"Deleted file: {file_path}")
        else:
            listbox.insert(tk.END, f"File not found: {file_path}")
    except Exception as e:
        listbox.insert(tk.END, f"Error deleting file {file_path}: {e}")

def delete_directory(directory_path, listbox):
    """Delete a directory and its contents, update the listbox."""
    try:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            listbox.insert(tk.END, f"Deleted directory: {directory_path}")
        else:
            listbox.insert(tk.END, f"Directory not found: {directory_path}")
    except Exception as e:
        listbox.insert(tk.END, f"Error deleting directory {directory_path}: {e}")

def create_gui():
    """Create the Tkinter GUI for the uninstaller."""
    root = tk.Tk()
    root.title("Uninstaller for Tabame")
    root.geometry("500x400")
    
    listbox = tk.Listbox(root, width=60, height=15)
    listbox.pack(pady=20)
    
    # Add a "Start Uninstallation" button
    start_button = tk.Button(root, text="Start Uninstallation", command=lambda: start_uninstallation(listbox, root))
    start_button.pack(pady=10)

    root.mainloop()

def start_uninstallation(listbox, root):
    """Start the uninstallation process and display results."""
    # Get the current user's username
    username = os.getlogin()

    # List of files to delete
    files = [
        fr"C:\Users\{username}\AppData\Local\Temp\tabame.zip",
        fr"C:\Users\{username}\AppData\Local\Tabame\tabamewin32_plugin.dll",
        fr"C:\Users\{username}\AppData\Local\Tabame\tabame.exe",
        r"C:\Windows\Prefetch\TABAME.EXE-3A670142.pf",
        fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Tabame.lnk",
        fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Tabame Interface.lnk",
        fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\tabame.lnk",
        fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Recent\Tabame.lnk",
        fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Recent\tabame_installer.ps1.lnk",
        fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Recent\tabame-uninstall.ps1.lnk",
    ]

    # List of directories to delete
    directories = [
        fr"C:\Users\{username}\AppData\Local\Tabame"
    ]

    listbox.insert(tk.END, "Starting uninstallation...\n")

    # Delete all files
    for file in files:
        delete_file(file, listbox)

    # Delete all directories
    for directory in directories:
        delete_directory(directory, listbox)

    listbox.insert(tk.END, "\nUninstallation completed.")
    messagebox.showinfo("Uninstallation Complete", "The software has been uninstalled successfully!")

if __name__ == "__main__":
    create_gui()
