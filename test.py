import pandas as pd

df=pd.read_excel('DataSheet.xlsx')

def filterByDate(dataFrame,date):
    if date != None:
        filt=dataFrame['Date']==date
        return dataFrame[filt]

    else :
        return dataFrame 


print(filterByDate(df,'2/1/2021'))
print(filterByDate(df,'10/4/2021'))