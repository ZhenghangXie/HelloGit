
def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param
    
    HLCEMA_X = dv.add_formula('HLCEMA_X', 
               "Ta('EMA',0,(high-low)/close,(high-low)/close,(high-low)/close,(high-low)/close,(high-low)/close,5)"
               , is_quarterly=False, add_data=True)
    
    return HLCEMA_X    