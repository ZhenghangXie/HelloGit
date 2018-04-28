
def run_formula(dv, param = None):
    defult_param = {'t':3}
    if not param:
        param = defult_param
    
    VEMA10 = dv.add_formula('VEMA10', 
           '''Ta('EMA',0,volume,volume,volume,volume,volume,%s)'''%(param['t']),
           is_quarterly=False)
    
    return VEMA10    