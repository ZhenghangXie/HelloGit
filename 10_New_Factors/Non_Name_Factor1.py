
def run_formula(dv, param = None):
    
    Non_Name_Factor1 = dv.add_formula('Non_Name_Factor1', 
               "StdDev((close/Delay(close,1))-1,60)"
               , is_quarterly=True, add_data=True) 
    
    return Non_Name_Factor1  