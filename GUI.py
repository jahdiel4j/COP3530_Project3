import tkinter as tk

""" --- Window Set-up --- """

root = tk.Tk()
root.title("Tech Stock Performance Analyzer")

# Dimensions of tk root window
width = 1100
height = 700

# Screen dimensions & coordinates for window placement
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/1.85)

# Set screen dimensions & location the root window
root.geometry('%dx%d+%d+%d' % (width, height, x, y))


""" --- Drop-down Menu for Implementation Choice --- """

structures = ["Hash Map", "AVL Tree"]
clicked = tk.StringVar()
clicked.set(structures[0])

menu = tk.OptionMenu(root, clicked, *structures)
menu.place(relx=0.87, rely=0.05)


""" --- Unfinished --- """

# Displays text depending on the boxes checked
def checked():
    l = tk.Label(root, text=var1.get())
    l.pack()

# Company options
company_label = tk.Label(root, text="COMPANIES")
company_label.config(font=("Calibri", 12, "bold"))
company_label.place(relx=0.16, rely=0.12)

var1 = tk.StringVar()
google = tk.Checkbutton(root, text="Google", variable=var1, onvalue = "Google is checked", offvalue="Google is unchecked")
google.deselect()
google.config(font=("Calibri", 12))
google.place(relx=0.08, rely=0.19)

apple = tk.Checkbutton(root, text="Apple")
apple.deselect()
apple.config(font=("Calibri", 12))
apple.place(relx=0.25, rely=0.19)

microsoft = tk.Checkbutton(root, text="Microsoft")
microsoft.deselect()
microsoft.config(font=("Calibri", 12))
microsoft.place(relx=0.08, rely=0.245)


b = tk.Button(root, text="Run Analysis", command=checked)
b.pack(pady=20)


root.mainloop()