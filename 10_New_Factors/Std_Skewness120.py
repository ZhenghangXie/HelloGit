
def run_formula(dv, param = None):
    
    Std_Skewness120 = dv.add_formula('Std_Skewness120', 
               "Ts_Skewness(Standardize(close),120)"
               , is_quarterly=True, add_data=True) 
    
    return Std_Skewness120  