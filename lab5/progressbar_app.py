import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Прогрессбар")
root.geometry("350x180")

label = tk.Label(root, text="Нажмите кнопку для запуска:")
label.pack(pady=15)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=250,
    mode="determinate",
    maximum=100
)
progress.pack(pady=10)


def start_progress():
    if progress["value"] >= 100:
        progress["value"] = 0

    progress["value"] += 10

    if progress["value"] < 100:
        root.after(300, start_progress)


button = tk.Button(
    root,
    text="Запустить",
    command=start_progress
)
button.pack(pady=10)

root.mainloop()
