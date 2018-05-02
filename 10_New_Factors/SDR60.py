
def run_formula(dv, param = None):
    
    SDR60 = dv.add_formula('SDR60', 
               "StdDev((close/Delay(close,1))-1,60)"
               , is_quarterly=True, add_data=True) 
    
    return SDR60  