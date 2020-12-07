import tkinter as tk
import tkcalendar
import HashSetup
import AVLSetup

companies = ["AAPL", "ACN", "ADBE", "AMZN", "AXP", "BAC", "CRM", "CSCO", "DELL",
            "DIS", "FB", "GE", "GOOG", "HPQ", "IBM", "INTC", "JPM", "KR", "LMT",
            "MSFT", "NFLX", "ORCL", "PG", "QCOM", "RTX", "T", "UPS", "WFC", "XOM"]

AVL = AVLSetup.AVLSetup()
AVL.initialize_companies_map()
Hash = HashSetup.HashSetup()
Hash.initialize_companies_map()

""" --- Window Set-up --- """

root = tk.Tk()
root.title("Tech Stock Performance Analyzer")
root.resizable(False, False)

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

disclaimer = tk.Label(root, text="* Stock analysis is based on closing times.", fg="gray")
disclaimer.config(font=("Calibri", 10))
disclaimer.place(relx=0.025, rely=0.035)


""" --- Output --- """

output_box_label = tk.Label(root, text="OUTPUT")
output_box_label.config(font=("Calibri", 12, "bold"))
output_box_label.place(relx=0.644, rely=0.708)

output_box = tk.Text(root, width=68, height = 5)
output_box.place(relx=0.427, rely=0.76)


""" --- Drop-down Menu for Implementation Choice --- """

implementations = ["Hash Map", "AVL Tree"]
imp_option = tk.StringVar()
imp_option.set(implementations[0])

implementation_menu = tk.OptionMenu(root, imp_option, *implementations)
implementation_menu.config(bg="light steel blue", relief="groove")
implementation_menu.place(relx=0.885, rely=0.035)


""" --- Calendars --- """

start_cal_label = tk.Label(root, text="START DATE")
start_cal_label.config(font=("Calibri", 12, "bold"))
start_cal_label.place(relx=0.493, rely=0.1)

end_cal_label = tk.Label(root, text="END DATE")
end_cal_label.config(font=("Calibri", 12, "bold"))
end_cal_label.place(relx=0.7772, rely=0.1)

start_cal = tkcalendar.Calendar(root, selectmode="day", year=2005, month=1, day=3, locale='en_US', date_pattern='MM/dd/yyyy',
            mindate=tkcalendar.calendar_.calendar.datetime.date(2005, 1, 3), maxdate=tkcalendar.calendar_.calendar.datetime.date(2020, 11, 27))
start_cal.place(relx=0.422, rely=0.16)

end_cal = tkcalendar.Calendar(root, selectmode="day", year=2020, month=11, day=27, locale='en_US', date_pattern='MM/dd/yyyy',
            mindate=tkcalendar.calendar_.calendar.datetime.date(2005, 1, 3), maxdate=tkcalendar.calendar_.calendar.datetime.date(2020, 11, 27))
end_cal.place(relx=0.7, rely=0.16)


""" --- Search Box --- """

def output_search_retry():
    output_box.delete("1.0", "end")
    output_box.insert(tk.INSERT, "Please check selected date/company and try again.")

def output_search(result, company, date):
    output_box.delete("1.0", "end")
    output_box.insert(tk.INSERT, company)
    output_box.insert(tk.INSERT, " on ")
    output_box.insert(tk.INSERT, date)
    output_box.insert(tk.INSERT, ":\n")
    output_box.insert(tk.INSERT, result)

def search():
    company = search_option.get()
    date = search_cal.get_date().strftime("%m/%d/%Y")

    if imp_option.get() == "Hash Map":
        price = Hash.search(company, date)
    else:
        price = AVL.search(company, date)

    if price == -1:
        output_search_retry()
    else:
        output_search(str(price), company, date)

search_border = tk.Label(root, text="", borderwidth="1", relief="solid", width=50, height = 3)
search_border.place(relx=0.519, rely=0.6)

search_option = tk.StringVar()
search_option.set(companies[0])

search_menu = tk.OptionMenu(root, search_option, *companies)
search_menu.config(relief="groove")
search_menu.place(relx=0.535, rely=0.613)

search_cal = tkcalendar.DateEntry(root, selectmode="day", year=2005, month=1, day=3, locale='en_US', date_pattern='MM/dd/yyyy',
            mindate=tkcalendar.calendar_.calendar.datetime.date(2005, 1, 3), maxdate=tkcalendar.calendar_.calendar.datetime.date(2020, 11, 27))
search_cal.place(relx=0.632, rely=0.619)

search_button = tk.Button(root, text="Search")
search_button.config(width=10, bg="light steel blue", relief="groove", command=search)
search_button.place(relx=0.75, rely=0.616)


""" --- Companies --- """

company_label = tk.Label(root, text="COMPANIES")
company_label.config(font=("Calibri", 12, "bold"))
company_label.place(relx=0.15, rely=0.1)

# Variables to determine selected companies
var1, var2, var3, var4, var5, var6 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
var7, var8, var9, var10, var11, var12 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
var13, var14, var15, var16, var17, var18 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
var19, var20, var21, var22, var23, var24 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
var25,var26, var27, var28, var29 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

var_list = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, 
          var16, var17, var18, var19, var20, var21, var22, var23, var24, var25, var26, var27, var28, var29]

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

# Configuring each checkbox
company_vars = [google, microsoft, acn, adobe, amazon, cisco, fb, ibm, intel, netflix, oracle, salesforce, qualcomm,
                exxon, att, apple, bankA, ge, lock, hp, jpm, pg, ups, dell, raytheon, wf, appen, disney, kroger]

for company in company_vars:
    company.deselect()
    company.config(font=("Calibri", 12))


""" --- Analysis Buttons --- """

def output_analysis(choice, company, growth, start, end):
    output_box.delete("1.0", "end")
    output_box.insert(tk.INSERT, choice)
    output_box.insert(tk.INSERT, " growth from ")
    output_box.insert(tk.INSERT, start)
    output_box.insert(tk.INSERT, " to ")
    output_box.insert(tk.INSERT, end)
    output_box.insert(tk.INSERT, ":\n")
    output_box.insert(tk.INSERT, company)
    output_box.insert(tk.INSERT, ", ")
    output_box.insert(tk.INSERT, format(growth, ".2f"))

def output_retry():
    output_box.delete("1.0", "end")
    output_box.insert(tk.INSERT, "Please check selected dates/companies and try again.")
    
# Returns list of checked companies
def get_checked():
    checked_companies = []
    for item in var_list:
        if item.get() != "":
            checked_companies.append(item.get())
    return checked_companies

def find_best():
    checked_companies = get_checked()
    start = start_cal.get_date()
    end = end_cal.get_date()
    
    if imp_option.get() == "Hash Map":
        company, growth = Hash.find_best_stock_growth(checked_companies, start, end)
    else:
        company, growth = AVL.find_best_stock_growth(checked_companies, start, end)

    if growth == -1000 or company == "":
        output_retry()
    else:
        output_analysis("Best", company, growth, start, end)

def find_worst():
    checked_companies = get_checked()
    start = start_cal.get_date()
    end = end_cal.get_date()
    
    if imp_option.get() == "Hash Map":
        company, growth = Hash.find_worst_stock_growth(checked_companies, start, end)
    else:
        company, growth = AVL.find_worst_stock_growth(checked_companies, start, end)

    if growth == 1000 or company == "":
        output_retry()
    else:
        output_analysis("Worst", company, growth, start, end)

best_button = tk.Button(root, text="Find Best Stock Growth", command=find_best)
best_button.config(width=20, bg="light steel blue", relief="groove")
best_button.place(relx=0.607, rely=0.46)

worst_button = tk.Button(root, text="Find Worst Stock Growth", command=find_worst)
worst_button.config(width =20, bg="light steel blue", relief="groove")
worst_button.place(relx=0.607, rely=0.52)

root.mainloop()