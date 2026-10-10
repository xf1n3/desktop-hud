import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x250+1300+0")
ctk.set_appearance_mode("dark")
ctk.deactivate_automatic_dpi_awareness()
root.overrideredirect(False)
root.attributes("-topmost", True)
ctk.set_default_color_theme("dark-blue")
root.maxsize(500, 750)
root.minsize(500, 250)
root.title("Desktop-Hud")

root.mainloop()