
def run_formula(dv, param = None):
    
    HL60 = dv.add_formula('HL60', 
               "Ts_Mean(high/low,60)"
               , is_quarterly=True, add_data=True)  
    
    return HL60  