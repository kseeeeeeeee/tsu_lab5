import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Выбор элемента из списка")
root.geometry("350x300")

label = tk.Label(root, text="Выберите любимый язык программирования:")
label.pack(pady=10)

listbox = tk.Listbox(root, height=6, width=25)
listbox.pack(pady=5)

languages = ["Python", "Java", "C++", "JavaScript", "C#"]

for language in languages:
    listbox.insert(tk.END, language)


def show_selection():
    selection = listbox.curselection()

    if selection:
        selected_language = listbox.get(selection[0])
        messagebox.showinfo("Выбор", f"Вы выбрали: {selected_language}")
    else:
        messagebox.showwarning("Внимание", "Сначала выберите элемент!")


button = tk.Button(root, text="Показать выбор", command=show_selection)
button.pack(pady=10)

root.mainloop()
