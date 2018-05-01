def SMA(A,n,m):
    # 设置alpha的比例
    alpha = m/n
    #通过ewm计算递归函数
    return A.ewm(alpha=alpha, adjust=False).mean()
        

def run_formula(dv, param = None):
    defult_param = {'t1':13,'t2':2,'t3':13,'t4':2}
    if not param:
        param = defult_param
    
    BIAS_SMA = dv.add_formula('BIAS_SMA', 
               "100*((close-SMA(close,%s,%s))/SMA(close,%s,%s))"%(param['t1'],param['t2'],param['t3'],param['t4'])
             , is_quarterly=False, add_data=True,
             register_funcs={"SMA":SMA}
             )
    return BIAS_SMA

