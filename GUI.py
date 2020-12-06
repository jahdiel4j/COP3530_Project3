  
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

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()
var7 = tk.StringVar()
var8 = tk.StringVar()
var9 = tk.StringVar()
var10 = tk.StringVar()
var11 = tk.StringVar()
var12= tk.StringVar()
var13 = tk.StringVar()
var14 = tk.StringVar()
var15 = tk.StringVar()
var16 = tk.StringVar()
var17 = tk.StringVar()
var18 = tk.StringVar()
var19 = tk.StringVar()
var20 = tk.StringVar()
var21 = tk.StringVar()
var22 = tk.StringVar()
var23 = tk.StringVar()
var24 = tk.StringVar()
var25 = tk.StringVar()
var26 = tk.StringVar()
var27 = tk.StringVar()
var28 = tk.StringVar()
var29 = tk.StringVar()
# Column 1
google = tk.Checkbutton(root, text="Google", variable=var1, onvalue = "GOOG", offvalue="")
microsoft = tk.Checkbutton(root, variable=var2, text="Microsoft", onvalue = "MSFT", offvalue="")
acn = tk.Checkbutton(root, variable=var3, text="ACN", onvalue = "ACN", offvalue="")
adobe = tk.Checkbutton(root, variable=var4, text="Adobe", onvalue = "ADBE", offvalue="")
amazon = tk.Checkbutton(root, variable=var5, text="Amazon", onvalue = "AMZN", offvalue="")
cisco = tk.Checkbutton(root, variable=var6, text="Cisco", onvalue = "CSCO", offvalue="")
fb = tk.Checkbutton(root, variable=var7, text="Facebook", onvalue = "FB", offvalue="")
ibm = tk.Checkbutton(root, variable=var8, text="IBM", onvalue = "IBM", offvalue="")
intel = tk.Checkbutton(root, variable=var9, text="Intel", onvalue = "INTC", offvalue="")
netflix = tk.Checkbutton(root, variable=var10, text="Netflix", onvalue = "NFLX", offvalue="")
oracle = tk.Checkbutton(root, variable=var11, text="Oracle", onvalue = "ORCL", offvalue="")
salesforce = tk.Checkbutton(root, variable=var12, text="Salesforce", onvalue = "CRM", offvalue="")
qualcomm = tk.Checkbutton(root, variable=var13, text="Qualcomm", onvalue = "QCOM", offvalue="")
exxon = tk.Checkbutton(root, variable=var14, text="Exxon", onvalue = "XOM", offvalue="")
att = tk.Checkbutton(root, variable=var15, text="AT&T", onvalue = "T", offvalue="")

google.place(relx=0.07, rely=0.16)
microsoft.place(relx=0.07, rely=0.21)
acn.place(relx=0.07, rely=0.26)
adobe.place(relx=0.07, rely=0.31)
amazon.place(relx=0.07, rely=0.36)
cisco.place(relx=0.07, rely=0.41)
fb.place(relx=0.07, rely=0.46)
ibm.place(relx=0.07, rely=0.51)
intel.place(relx=0.07, rely=0.56)
netflix.place(relx=0.07, rely=0.61)
oracle.place(relx=0.07, rely=0.66)
salesforce.place(relx=0.07, rely=0.71)
qualcomm.place(relx=0.07, rely=0.76)
exxon.place(relx=0.07, rely=0.81)
att.place(relx=0.07, rely=0.86) 

# Column 2
apple = tk.Checkbutton(root, variable=var16, text="Apple", onvalue = "AAPL", offvalue="")
bankA = tk.Checkbutton(root, variable=var17, text="Bank of America", onvalue = "BAC", offvalue="")
ge = tk.Checkbutton(root, variable=var18, text="General Electric", onvalue = "GE", offvalue="")
lock = tk.Checkbutton(root, variable=var19, text="Lockhead Martin", onvalue = "LMT", offvalue="")
hp = tk.Checkbutton(root, variable=var20, text="Hewlett-Packard", onvalue = "HPQ", offvalue="")
jpm = tk.Checkbutton(root, variable=var21, text="JPMorgan Chase", onvalue = "JPM", offvalue="")
pg = tk.Checkbutton(root, variable=var22, text="Proctor and Gamble", onvalue = "PG", offvalue="")
ups = tk.Checkbutton(root, variable=var23, text="UPS", onvalue = "UPS", offvalue="")
dell = tk.Checkbutton(root, variable=var24, text="Dell", onvalue = "DELL", offvalue="")
raytheon = tk.Checkbutton(root, variable=var25, text="Raytheon", onvalue = "RTX", offvalue="")
wf = tk.Checkbutton(root, variable=var26, text="Wells Fargo", onvalue = "WFC", offvalue="")
appen = tk.Checkbutton(root, variable=var27, text="Appen", onvalue = "AXP", offvalue="")
disney = tk.Checkbutton(root, variable=var28, text="Disney", onvalue = "DIS", offvalue="")
kroger = tk.Checkbutton(root, variable=var29, text="Kroger", onvalue = "KR", offvalue="")

apple.place(relx=0.22, rely=0.16)
bankA.place(relx=0.22, rely=0.21)
ge.place(relx=0.22, rely=0.26)
lock.place(relx=0.22, rely=0.31)
hp.place(relx=0.22, rely=0.36)
jpm.place(relx=0.22, rely=0.41)
pg.place(relx=0.22, rely=0.46)
ups.place(relx=0.22, rely=0.51)
dell.place(relx=0.22, rely=0.56)
raytheon.place(relx=0.22, rely=0.61)
wf.place(relx=0.22, rely=0.66)
appen.place(relx=0.22, rely=0.71)
disney.place(relx=0.22, rely=0.76)
kroger.place(relx=0.22, rely=0.81)

company_vars = [google, microsoft, acn, adobe, amazon, cisco, fb, ibm, intel, netflix, oracle, salesforce, qualcomm,
                exxon, att, apple, bankA, ge, lock, hp, jpm, pg, ups, dell, raytheon, wf, appen, disney, kroger]

for company in company_vars:
    company.deselect()
    company.config(font=("Calibri", 12))

List = [] # LIST List for the comapnies checked
# LIST List for the variables of the companies
varList = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, 
          var16, var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29] 

""" --- Analysis Buttons --- """
# Displays text depending on the boxes checked
def checked():
    l = tk.Label(root, text=var1.get())
    l.pack()

# LIST Add checked checkboxes to list 
def addtolist():
    global List

    List = []
    for item in varList:
        if item.get() != "":
            List.append(item.get())
    print(List)
# LIST Testing button for the addtolist() 
b1 = tk.Button(root, text="TEST LIST", command=addtolist)
b1.place(relx=0.3, rely=0.1)

best_button = tk.Button(root, text="Find Best Stock Growth", command=[checked(), retrieve_date()])
best_button.config(width=20, bg="light steel blue", relief="groove")
best_button.place(relx=0.607, rely=0.46)

worst_button = tk.Button(root, text="Find Worst Stock Growth", command=[checked(), retrieve_date()])
worst_button.config(width =20, bg="light steel blue", relief="groove")
worst_button.place(relx=0.607, rely=0.52)


root.mainloop()