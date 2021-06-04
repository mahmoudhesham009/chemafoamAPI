def filterByDate(dataFrame,date):
    if date != None:
        filt=dataFrame['Date']==date
        return dataFrame[filt]

    else :
        return dataFrame 

def filterByWeek(dataFrame,week):
    if week != None:
        filt=dataFrame['Week']==week
        return dataFrame[filt]
    else :
        return dataFrame 

def filterByMonth(dataFrame,month):
    if month != None:
        filt=dataFrame['Month']==month
        return dataFrame[filt]
    else :
        return dataFrame 

def filterByShift(dataFrame,shift):
    if shift != None:
        filt=dataFrame['Shift']==shift
        return dataFrame[filt]
    else :
        return dataFrame 

def filterByFomType(dataFrame,fomType):
    if fomType != None:
        filt=dataFrame['FomType']==fomType
        return dataFrame[filt]
    else :
        return dataFrame

def applyFilters(dataFrame,date,week,month,shift,fomtype):
    return filterByFomType(filterByShift(filterByMonth(filterByWeek(filterByDate(dataFrame,date),week),month),shift),fomtype)