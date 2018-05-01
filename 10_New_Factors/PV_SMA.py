def SMA(A,n,m):
    # 设置alpha的比例
    alpha = m/n
    #通过ewm计算递归函数
    return A.ewm(alpha=alpha, adjust=False).mean()
        

def run_formula(dv, param = None):
    defult_param = {'t1':13,'t2':2}
    if not param:
        param = defult_param
    
    PV_SMA = dv.add_formula('PV_SMA', 
               "SMA(1/3*(close+high+low)*volume,%s,%s)"%(param['t1'],param['t2'])
             , is_quarterly=False, add_data=True,
             register_funcs={"SMA":SMA}
             )
    return PV_SMA

