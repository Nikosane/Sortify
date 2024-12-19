import tkinter as tk
from tkinter import filedialog
from organizer import start_monitoring

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_label.config(text=f"Selected Folder: {folder}")
        start_monitoring(folder)

root = tk.Tk()
root.title("Advanced File Organizer")

folder_label = tk.Label(root, text="No folder selected")
folder_label.pack(pady=10)

select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)

root.mainloop()
