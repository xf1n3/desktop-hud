import customtkinter as ctk

root = ctk.CTk()
root.geometry("700x350+1220+0")

ctk.set_appearance_mode("dark")
ctk.deactivate_automatic_dpi_awareness()
ctk.set_default_color_theme("dark-blue")

root.overrideredirect(True)
root.attributes("-topmost", True)
root.maxsize(700, 1050)
root.minsize(700, 350)
root.title("Desktop-Hud")
root.config(bg="#000001")
root.attributes("-alpha", 1.0)
root.attributes("-transparentcolor", "#000001")
root_frame = ctk.CTkFrame(root, fg_color="#1e1e1e", corner_radius=20, bg_color="#000001")
root_frame.pack(fill="both", expand=True)

close_button = ctk.CTkButton(root_frame, text="Выйти", command=root.destroy)
close_button.pack()

task_entry = ctk.CTkEntry(root_frame, placeholder_text="Впишите задачу...", width=300)
task_entry.pack()

root.mainloop()