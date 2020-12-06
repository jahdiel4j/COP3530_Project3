import tkinter as tk
#import tkinter.ttk as ttk
import tkcalendar

companies = ["ACN", "AT&T", "Adobe", "Amazon", "Appen", "Apple", "Bank of America", "Cisco", "Dell", "Disney", "Exxon", "Facebook",
            "General Electric", "Google", "Hewlett-Packard", "IBM", "Intel", "JPMorgan Chase", "Kroger", "Lockheed Martin", "Microsoft",
            "Netflix", "Oracle", "Proctor and Gamble", "Qualcomm", "Raytheon", "Salesforce", "UPS", "Wells Fargo"]

""" --- Window Set-up --- """

root = tk.Tk()
root.title("Tech Stock Performance Analyzer")
root.resizable(False, False)
#ttk.Style('alt')

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

implementations = ["Hash Map", "AVL Tree"]
imp_options = tk.StringVar()
imp_options.set(implementations[0])

implementation_menu = tk.OptionMenu(root, imp_options, *implementations)
implementation_menu.config(bg="light steel blue", relief="groove")
implementation_menu.place(relx=0.88, rely=0.03)


""" --- Calendars --- """

def retrieve_date():
    print(start_cal.get_date())

start_cal_label = tk.Label(root, text="START DATE")
start_cal_label.config(font=("Calibri", 12, "bold"))
start_cal_label.place(relx=0.493, rely=0.1)

end_cal_label = tk.Label(root, text="END DATE")
end_cal_label.config(font=("Calibri", 12, "bold"))
end_cal_label.place(relx=0.7772, rely=0.1)

start_cal = tkcalendar.Calendar(root, selectmode="day", year=2005, month=1, day=3, locale='en_US', date_pattern='MM/dd/yyyy')
start_cal.place(relx=0.422, rely=0.16)

end_cal = tkcalendar.Calendar(root, selectmode="day", year=2020, month=11, day=27, locale='en_US', date_pattern='MM/dd/yyyy')
end_cal.place(relx=0.7, rely=0.16)


""" --- Search Box --- """

search_border = tk.Label(root, text="", borderwidth="1", relief="solid", width=66, height = 3)
search_border.place(relx=0.468, rely=0.6)

search_options = tk.StringVar()
search_options.set(companies[0])

search_menu = tk.OptionMenu(root, search_options, *companies)
search_menu.config(relief="groove")
search_menu.place(relx=0.485, rely=0.614)

search_cal = tkcalendar.DateEntry(locale='en_US', date_pattern='MM/dd/yyyy')
search_cal.place(relx=0.632, rely=0.619)

search_button = tk.Button(root, text="Search")
search_button.config(width=10, bg="light steel blue", relief="groove")
search_button.place(relx=0.8, rely=0.617)


""" --- Output --- """

output_box_label = tk.Label(root, text="OUTPUT")
output_box_label.config(font=("Calibri", 12, "bold"))
output_box_label.place(relx=0.645, rely=0.708)

output_box = tk.Text(root, width=68, height = 5)
output_box.place(relx=0.425, rely=0.76)


""" --- Companies --- """

company_label = tk.Label(root, text="COMPANIES")
company_label.config(font=("Calibri", 12, "bold"))
company_label.place(relx=0.15, rely=0.1)

# Column 1
var1 = tk.StringVar()
google = tk.Checkbutton(root, text="Google", variable=var1, onvalue = "Google is checked", offvalue="Google is unchecked")
google.place(relx=0.07, rely=0.16)

microsoft = tk.Checkbutton(root, text="Microsoft")
microsoft.place(relx=0.07, rely=0.21)

acn = tk.Checkbutton(root, text="ACN")
acn.place(relx=0.07, rely=0.26)

adobe = tk.Checkbutton(root, text="Adobe")
adobe.place(relx=0.07, rely=0.31)

amazon = tk.Checkbutton(root, text="Amazon")
amazon.place(relx=0.07, rely=0.36)

cisco = tk.Checkbutton(root, text="Cisco")
cisco.place(relx=0.07, rely=0.41)

fb = tk.Checkbutton(root, text="Facebook")
fb.place(relx=0.07, rely=0.46)

ibm = tk.Checkbutton(root, text="IBM")
ibm.place(relx=0.07, rely=0.51)

intel = tk.Checkbutton(root, text="Intel")
intel.place(relx=0.07, rely=0.56)

netflix = tk.Checkbutton(root, text="Netflix")
netflix.place(relx=0.07, rely=0.61)

oracle = tk.Checkbutton(root, text="Oracle")
oracle.place(relx=0.07, rely=0.66)

salesforce = tk.Checkbutton(root, text="Salesforce")
salesforce.place(relx=0.07, rely=0.71)

qualcomm = tk.Checkbutton(root, text="Qualcomm")
qualcomm.place(relx=0.07, rely=0.76)

exxon = tk.Checkbutton(root, text="Exxon")
exxon.place(relx=0.07, rely=0.81)

att = tk.Checkbutton(root, text="AT&T")
att.place(relx=0.07, rely=0.86)

# Column 2
apple = tk.Checkbutton(root, text="Apple")
apple.place(relx=0.22, rely=0.16)

bankA = tk.Checkbutton(root, text="Bank of America")
bankA.place(relx=0.22, rely=0.21)

ge = tk.Checkbutton(root, text="General Electric")
ge.place(relx=0.22, rely=0.26)

lock = tk.Checkbutton(root, text="Lockhead Martin")
lock.place(relx=0.22, rely=0.31)

hp = tk.Checkbutton(root, text="Hewlett-Packard")
hp.place(relx=0.22, rely=0.36)

jpm = tk.Checkbutton(root, text="JPMorgan Chase")
jpm.place(relx=0.22, rely=0.41)

pg = tk.Checkbutton(root, text="Proctor and Gamble")
pg.place(relx=0.22, rely=0.46)

ups = tk.Checkbutton(root, text="UPS")
ups.place(relx=0.22, rely=0.51)

dell = tk.Checkbutton(root, text="Dell")
dell.place(relx=0.22, rely=0.56)

raytheon = tk.Checkbutton(root, text="Raytheon")
raytheon.place(relx=0.22, rely=0.61)

wf = tk.Checkbutton(root, text="Wells Fargo")
wf.place(relx=0.22, rely=0.66)

appen = tk.Checkbutton(root, text="Appen")
appen.place(relx=0.22, rely=0.71)

disney = tk.Checkbutton(root, text="Disney")
disney.place(relx=0.22, rely=0.76)

kroger = tk.Checkbutton(root, text="Kroger")
kroger.place(relx=0.22, rely=0.81)

company_vars = [google, microsoft, acn, adobe, amazon, cisco, fb, ibm, intel, netflix, oracle, salesforce, qualcomm,
                exxon, att, apple, bankA, ge, lock, hp, jpm, pg, ups, dell, raytheon, wf, appen, disney, kroger]

for company in company_vars:
    company.deselect()
    company.config(font=("Calibri", 12))

""" --- Analysis Buttons --- """

# Displays text depending on the boxes checked
def checked():
    l = tk.Label(root, text=var1.get())
    l.pack()

best_button = tk.Button(root, text="Find Best Stock Growth", command=[checked(), retrieve_date()])
best_button.config(width=20, bg="light steel blue", relief="groove")
best_button.place(relx=0.607, rely=0.46)

worst_button = tk.Button(root, text="Find Worst Stock Growth", command=[checked(), retrieve_date()])
worst_button.config(width =20, bg="light steel blue", relief="groove")
worst_button.place(relx=0.607, rely=0.52)


root.mainloop()
