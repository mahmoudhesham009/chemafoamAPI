
def filterByDate(dataFrame,date):
    if date != None:
        filt=dataFrame['Date']==date
        return dataFrame[filt]

    else :
        return dataFrame    
