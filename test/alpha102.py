#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter
def SMA(A,n,m):
    # 设置alpha的比例
	alpha = m/n
    #通过ewm计算递归函数
	return A.ewm(alpha=alpha, adjust=False).mean()
              
def run_formula(dv):
	alpha102 = dv.add_formula('alpha102', 
               "SMA(Max(volume-Delay(volume,1),0),6,1)/SMA(Abs(volume-Delay(volume,1)),6,1)*100"
             , is_quarterly=False, add_data=True,
             register_funcs={"SMA":SMA}
             )

	return alpha102