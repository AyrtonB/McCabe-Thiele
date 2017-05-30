import numpy as np
#import scipy.optimize as opt
#import matplotlib.pyplot as plt
#import Eqm

#--------------------------------------------------------------------------------------------------------------------------------
# Variables to set

a = np.array([4.02232,1206.53,220.291]) # (AC_LK)
b = np.array([4.0854,1348.77,219.976]) # (AC_HK)

c = 0.25 # (P_Tot) in Bara
d = 1001 # (N_Size), 1001 = 0.1% accuracy for xA

e = 0.55 # (xf) Feed mol fraction of A, where 1 = 100%
f = 0.5 # (q)

g = 0.95 # (xd) Distillate mol fraction of A
h = 0.03 # (xb) Bottoms mol fraction of A

i = 1.40 # (Rf) multiplier for Rmin

j = 30 # (Max_Pl) Maximum number of plates


#--------------------------------------------------------------------------------------------------------------------------------
# Sets variables for Eqm

manual = 'y'

def Var_In(x):
    
    if manual == 'y':
        
        if x == 'P_Tot':
            x = c
        
        if x == 'xf':
            x = e
        
        if x == 'q':
            x = f

        if x == 'xd':
            x = g        

        if x == 'xb':
            x = h 

        if x == 'Rf':
            x = i
    
    else:
        from gui import Extract_Inputs
        
        if x == 'P_Tot':
            x = Extract_Inputs(self,'P_Tot')   
        
        if x == 'xf':
            x = Extract_Inputs('xf')   
        
        if x == 'q':
            x = Extract_Inputs('q')  

        if x == 'xd':
            x = Extract_Inputs('xd')         

        if x == 'xb':
            x = Extract_Inputs('xb')  

        if x == 'Rf':
            x = Extract_Inputs('Rf')         
            
    if x == 'AC_LK':
            x = a
        
    elif x == 'AC_HK':
            x = b
        
    elif x == 'N_Size':
            x = d
    
    elif x == 'Max_Pl':
            x = j

    return x

#--------------------------------------------------------------------------------------------------------------------------------
# Outputs to return to console

if __name__ == '__main__':

    import Eqm as Eqm
    
    def Outputs(x):
        
        if x == 'Num_Plates':
            x = Eqm.Outputs('Num_Plates')
            
        elif x == 'R':
            x = Eqm.Outputs('R')
            
        elif x == 'Rmin':
            x = Eqm.Outputs('Rmin')
                    
        elif x == 'x_q_TOL':
            x = float(Eqm.Outputs('x_q_TOL'))
    
        return x
    
    Num_Plates = Outputs('Num_Plates')
    Rmin = Outputs('Rmin')
    R = Outputs('R')
    x_q_TOL = Outputs('x_q_TOL')
        
    print('Number of Plates = ', Num_Plates)
    print('Rmin = ', Rmin)
    print('R = ', R)
    print('xA @ q & TOL intercept = ', x_q_TOL)
    
    Eqm.Plot_MT()