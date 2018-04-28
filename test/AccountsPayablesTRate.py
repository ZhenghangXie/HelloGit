#type2  -  only use add_formula function with parameter
        
dv.add_field('tot_oper_cost')
dv.add_field('acct_payable')
dv.add_field('notes_payable')
dv.add_field('pre_pay')
def run_formula(dv, param = None):
    defult_param = {'t1':4,'t2':4,'t3':4}
    if not param:
        param = defult_param
    
    AccountsPayablesTRate = dv.add_formula('BBI_J', 
           '''AccountsPayablesTRate_H',"tot_oper_cost/(Ts_Mean(acct_payable,4)+Ts_Mean(notes_payable,4)-Ts_Mean(pre_pay,4))'''%(param['t1'],param['t2'],param['t3']),
           is_quarterly=False)
    
    return AccountsPayablesTRate

