from flask import Flask ,request
from flask_restful import Api, Resource
import pandas as pd

df=pd.read_excel('DataSheet.xlsx')

app=Flask(__name__)
date=None



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

def filterByFoamType(dataFrame,foamType):
    if foamType != None:
        filt=dataFrame['FoamType']==foamType
        return dataFrame[filt]
    else :
        return dataFrame

def applyFilters(dataFrame,date,week,month,shift,foamtype):
    return filterByFoamType(filterByShift(filterByMonth(filterByWeek(filterByDate(dataFrame,date),week),month),shift),foamtype)


def get_presntage(x,y):
    print(x,y)
    return (x/y)*100

def getDamaged(df):
    filt_a=filterByShift(df,'A')
    filt_b=filterByShift(df,'B')

    shift_A_total_amount=filt_a['إجمالى الإستهلاك\n/م3'].sum()
    shift_B_total_amount=filt_b['إجمالى الإستهلاك\n/م3'].sum()
    total_amount=shift_A_total_amount+shift_B_total_amount

    
    shift_A_damage=filt_a['الهالك\n/م3'].sum()
    shift_B_damage=filt_b['الهالك\n/م3'].sum()
    total_damage=shift_A_damage+shift_B_damage

    return get_presntage(shift_A_damage,shift_A_total_amount),get_presntage(shift_B_damage,shift_B_total_amount),get_presntage(total_damage,total_amount)


def getPlanHour(df):
    filt_a=filterByShift(df,'A')
    filt_b=filterByShift(df,'B')

    shift_A_plan_hour=filt_a['Plan Hour'].sum()
    shift_B_plan_hour=filt_b['Plan Hour'].sum()
    total_plan_hour=shift_A_plan_hour+shift_B_plan_hour

    
    shift_A_actual_hour=filt_a['ساعات\nالعمل\nالفعلية'].sum()
    shift_B_actual_hour=filt_b['ساعات\nالعمل\nالفعلية'].sum()
    total_actual_hour=shift_A_actual_hour+shift_B_actual_hour

    return get_presntage(shift_A_plan_hour,shift_A_actual_hour),get_presntage(shift_B_plan_hour,shift_B_actual_hour),get_presntage(total_plan_hour,total_actual_hour)
    

@app.route('/',methods=['GET'])
def params():
    try:
        date=request.args['date']
        print(type(date))
    except:
        date=None

    try:
        week=int(request.args['week'])
    except:
        week=None

    try:
        month=request.args['month']
    except:
        month=None

    try:
        shift=request.args['shift']
    except:
        shift=None

    try:
        foamType=request.args['foamtype']
    except:
        foamType=None    

    fdf=applyFilters(df,date,week,month,shift,foamType)
    
    AD,BD,TD=getDamaged(fdf)
    AW,BW,TW=getPlanHour(fdf)

    return {'Data':{
                'Damage':{
                        'A damage': AD ,
                        'B damage': BD ,
                        'total damage': TD
                },
                'Work Hours':{
                        'A Work Hour':AW ,
                        'B Work Hour':BW ,
                        'Total Work Hour':TW
                }
            }
            
        }
        


