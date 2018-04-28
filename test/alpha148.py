#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter
def run_formula(dv):
	alpha148 = dv.add_formula('alpha148', 
               "-1*(Rank(Correlation((open),Ts_Sum(Ts_Mean(volume,60),9),6))<Rank((open - Ts_Min(open,14))))"
               , is_quarterly=False, add_data=True)
	return alpha148   
