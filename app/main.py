import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def open_settings():
    # Create the settings window
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Settings content
    tk.Label(settings_window, text="Settings Option 1:").pack(padx=10, pady=5)
    tk.Entry(settings_window).pack(padx=10, pady=5)

    tk.Label(settings_window, text="Settings Option 2:").pack(padx=10, pady=5)
    tk.Entry(settings_window).pack(padx=10, pady=5)

    tk.Button(settings_window, text="Save", command=lambda: messagebox.showinfo("Settings", "Settings saved!")).pack(
        pady=10)


def main():
    global root
    root = tk.Tk()
    root.title("Main Window")
    tk.Label(root, text="This is the main application").pack(padx=10, pady=10)
    tk.Button(root, text="Settings", command=open_settings).pack(pady=20)
    root.mainloop()


if __name__ == "__main__":
    main()
