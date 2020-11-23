from HashMap import HashMap

def convertDate(date):
    # 1/17/2008 -> 20080117
    # MM/DD/YYYY -> YYYYMMDD
    l = date.split("/")
    month = l[0]
    if len(month) == 1:
        month = "0" + month
    day = l[1]
    if len(day) == 1:
        day = "0" + day
    year = l[2]

    done = year + month + day
    done = int(done)
    return done

def initializeCompaniesMap():
    Companies = {}
    Companies["Google"] = HashMap();
    Companies["Amazon"] = HashMap();
    Companies["Apple"] = HashMap();
    Companies["Microsoft"] = HashMap();
    Companies["Facebook"] = HashMap();
    Companies["Intel"] = HashMap();
    Companies["Adobe"] = HashMap();
    Companies["Netflix"] = HashMap();
    Companies["IBM"] = HashMap();
    Companies["Salesforce"] = HashMap();
    Companies["Oracle"] = HashMap();
    Companies["Samsung"] = HashMap();
    Companies["Accenture"] = HashMap(); #13
    Companies["Cisco"] = HashMap();
    return Companies

companiesMap = initializeCompaniesMap();
str = "8/27/2017"
newb = convertDate(str)
companiesMap["Accenture"].insert(newb, 789)
x = companiesMap["Accenture"].retrieve(newb)
print(x)
