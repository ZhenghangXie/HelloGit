#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    DBM = dv.add_formula('DBM', 
               "If( open<=Delay(open,1),Max(open-low,open-Delay(open,1)),0)"
               , is_quarterly=False, add_data=True)
    STM = dv.add_formula('STM',"Ts_Sum(DBM,20)",is_quarterly=False,add_data=True)

    return STM

