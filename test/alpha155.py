#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter
def SMA(A,n,m):
    # 设置alpha的比例
	alpha = m/n
    #通过ewm计算递归函数
	return A.ewm(alpha=alpha, adjust=False).mean()
              
def run_formula(dv):
	alpha155 = dv.add_formula('alpha155', 
               "SMA(volume,13,2)-SMA(volume,27,2)-SMA(SMA(volume,13,2)-SMA(volume,27,2),10,2)"
             , is_quarterly=False, add_data=True,
             register_funcs={"SMA":SMA}
             )

	return alpha155