import tkinter as tk


root = tk.Tk()
root.title("Секундомер")
root.geometry("300x200")

elapsed_seconds = 0
running = False

time_label = tk.Label(root, text="00:00", font=("Arial", 32))
time_label.pack(pady=20)


def update_timer():
    global elapsed_seconds

    if running:
        elapsed_seconds += 1
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60
        time_label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)


def start_timer():
    global running

    if not running:
        running = True
        root.after(1000, update_timer)


def stop_timer():
    global running
    running = False


def reset_timer():
    global elapsed_seconds, running

    running = False
    elapsed_seconds = 0
    time_label.config(text="00:00")


tk.Button(root, text="Старт", command=start_timer).pack(side="left", padx=15)
tk.Button(root, text="Стоп", command=stop_timer).pack(side="left", padx=15)
tk.Button(root, text="Сброс", command=reset_timer).pack(side="left", padx=15)

root.mainloop()
