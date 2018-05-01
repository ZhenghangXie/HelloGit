
def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':20}
    if not param:
        param = defult_param
    
    ILLIQ_X = dv.add_formula('ILLIQ_X', 
               "Ts_Mean(Abs(Return(close,%s)),%s)/(volume*(high+low+close)/3)"%(param['t1'],param['t2'])
               , is_quarterly=False, add_data=True) 
    
    return ILLIQ_X   