import customtkinter  as c











class main_page(c.CTk):
 	def __init__(self):

 		super().__init__()

 		self.title("POTATO-GPT")
 		self.geometry(f"{800}x{600}")
 		self.grid_rowconfigure(0, weight=1)
 		self.grid_columnconfigure(0, weight=1)

 		self.main = c.CTkFrame(self, fg_color="grey")
 		self.main.grid(row=0, column=0, sticky="nsew")