
def run_formula(dv, param = None):
    
    M_B = dv.add_formula('M_B', 
               "capital_stk*close/tot_assets"
               , is_quarterly=False, add_data=True)  
    
    return M_B  