#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter



def run_formula(dv):
    LongDebtToAssets = dv.add_formula('LongDebtToAssets',"(lt_borrow/tot_assets)",is_quarterly=False, add_data=True)
    return LongDebtToAssets    
