import customtkinter as ctk

tasks_list = []

def add_task(event=None):
    entry_text = task_entry.get()
    len(tasks_list)

    if entry_text:
        new_task = len(tasks_list)
        task_label = ctk.CTkEntry(root_scroll, width=470, height=75, font=("Arial", 20))
        task_label.insert(0, entry_text)
        task_label.grid(row=new_task, column=0, pady=(5, 0), padx=(5, 0))

        confirm_button = ctk.CTkButton(root_scroll, text="✓", height=75, width=75, command=confirm_task, fg_color="#119702")
        confirm_button.grid(row=new_task, column=1, pady=(5, 0))

        tasks_list.append(task_label)
        task_entry.delete(0, "end")
        
def confirm_task(event):
    e

root = ctk.CTk()
root.geometry("700x575+1210+10")

ctk.set_appearance_mode("dark")
ctk.deactivate_automatic_dpi_awareness()
ctk.set_default_color_theme("dark-blue")

root.overrideredirect(True)
root.attributes("-topmost", True)
root.maxsize(700, 1050)
root.minsize(700, 575)
root.title("Desktop-Hud")
root.config(bg="#000001")
root.attributes("-alpha", 1.0)
root.attributes("-transparentcolor", "#000001")
root_frame = ctk.CTkFrame(root, fg_color="#1e1e1e", corner_radius=20, bg_color="#000001", border_width=1, border_color="#000000")
root_frame.pack(fill="both", expand=True)
root_scroll = ctk.CTkScrollableFrame(root_frame, width=550, height=250, corner_radius=20, fg_color="#1D1B1B", border_color="#000000", border_width=1)
root_scroll.grid(pady=(20, 0), padx=50, row=2)

task_entry = ctk.CTkEntry(root_frame, placeholder_text="Впишите задачу...", width=550, height=75, font=("Arial", 20))
task_entry.grid(row=0, pady=10)

add_task_button = ctk.CTkButton(root_frame, text="Добавить новую задачу", command=add_task, font=("Arial", 20), width=550, height=75, border_width=1, border_color="#000000")
add_task_button.grid(row=1, pady=5)

close_button = ctk.CTkButton(root_frame, text="Выйти", font=("Arial", 20), command=root.destroy, border_width=1, border_color="#000000", width=183, height=60)
close_button.grid(row=3, padx=(400, 0), pady=(5, 0))

root.mainloop()