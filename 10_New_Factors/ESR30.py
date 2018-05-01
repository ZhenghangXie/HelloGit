
def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':2,'t3':60,'t4':30}
    if not param:
        param = defult_param
    
    ESR30 = dv.add_formula('VEMA10', 
           '''Ewma(StdDev(Return(close,%s,%s),%s),%s)'''%(param['t1'],param['t2'],param['t3'],param['t4']),
           is_quarterly=False)
    
    return ESR30    