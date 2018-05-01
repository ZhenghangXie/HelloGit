
def run_formula(dv, param = None):
    
    CFinNP_2 = dv.add_formula('CFinNP_2', 
               "((net_cash_flows_oper_act)/net_profit)^2"
               , is_quarterly=False, add_data=True)   
    
    return CFinNP_2  