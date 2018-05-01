
def run_formula(dv, param = None):
    defult_param = {'t1':0.8,'t2':20}
    if not param:
        param = defult_param
    
    DEVOL20 = dv.add_formula('DEVOL20', 
               "Decay_exp(turnover_ratio,%s,%s)"%(param['t1'],param['t2'])
               , is_quarterly=False, add_data=True) 
    
    return DEVOL20   