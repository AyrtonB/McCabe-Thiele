import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def Pre_Output():
    
    def Decimalise(x,dec):   
        a = pow(10,dec)
        x = int(x*a)/a
        return x
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Getting variables from .csv 
    
    import csv
    
    def getval(x):
        
        Variables = []
        Values = []   
        
        with open('Inputs.csv', 'rt') as g:
            reader = csv.reader(g)
            
            # read file row by row
            rowNr = 0
            for row in reader:
                # Skip the header row.
                if rowNr >= 1:
                    #g.seek(0) <-- makes it freeze on start up
                    Variables.append(row[0])
                    Values.append(row[1])
         
                # Increase the row number
                rowNr = rowNr + 1
        
        if x == 'F':
            x = float(Values[0])
        
        elif x == 'xf':
            x = float(Values[1])
        elif x == 'xd':
            x = float(Values[2])
        elif x == 'xb':
            x = float(Values[3])
            
        elif x == 'P_Tot':
            x = float(Values[4])
        elif x == 'q':
            x = float(Values[5])
        elif x == 'Rf':
            x = float(Values[6])
            
        elif x == 'AC_LK_A':
            x = float(Values[7])
        elif x == 'AC_LK_B':
            x = float(Values[8])
        elif x == 'AC_LK_C':
            x = float(Values[9])
            
        elif x == 'AC_HK_A':
            x = float(Values[10])
        elif x == 'AC_HK_B':
            x = float(Values[11])
        elif x == 'AC_HK_C':
            x = float(Values[12])
            
        elif x == 'N_Size':
            x = int(Values[13])
        elif x == 'Max_Pl':
            x = int(Values[14])
        
        return x
            
    #print(getval('xf'))
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Variables to set (Values are taken from the Inputs file)
    
    F = getval('F')
    
    AC_LK = np.array([getval('AC_LK_A'),getval('AC_LK_B'),getval('AC_LK_C')])
    AC_HK = np.array([getval('AC_HK_A'),getval('AC_HK_B'),getval('AC_HK_C')])
        
    Max_Pl = getval('Max_Pl')
    N_Size = getval('N_Size') # 1001 = 0.1% accuracy for xA
        
    xf = getval('xf')
    xd = getval('xd')
    xb = getval('xb')
    
    P_Tot = getval('P_Tot') # Bara    
    q = getval('q')
    Rf = getval('Rf')
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # making x array which contains xA, yA and T from xA = 0 -> 1 @ step = 1/(N_Size-1)
    
    xA = np.linspace(0,1,N_Size)
    yA = np.linspace(0.00,0.00,N_Size)
    T = np.linspace(0.00,0.00,N_Size)
    
    x = np.array([xA[0:N_Size],yA[0:N_Size],T[0:N_Size]]) # x[xA,yA,T]
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Fitting T values to xA for Eqm line
    
    def xA_T(N):
        xA_Ant = x[0,N]
        def P_Ant(T):
    
            PA = pow(10,AC_LK[0]-(AC_LK[1]/(T+AC_LK[2])))*xA_Ant
            PB = pow(10,AC_HK[0]-(AC_HK[1]/(T+AC_HK[2])))*(1-xA_Ant)
    
            F = np.empty((1))
            F[0] = P_Tot - (PA + PB)
            return F[0]
        
        TGuess = [100]
        T = opt.fsolve(P_Ant,TGuess)
    
        x[2,N] = T
        
        return x
    
    for N in range(0,len(xA)):
        xA_T(N)
        x[1,N] = pow(10,AC_LK[0]-(AC_LK[1]/(x[2,N]+AC_LK[2])))*x[0,N]/P_Tot
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # xA to yA polynomial function
    
    Eqm_Poly_x2y = np.polyfit(x[0,0:N_Size], x[1,0:N_Size], 6)
    Eqm_Poly_y2x = np.polyfit(x[1,0:N_Size], x[0,0:N_Size], 6)
    Eqm_Poly_x2T = np.polyfit(x[0,0:N_Size], x[2,0:N_Size], 6)
    
    def Eqm_x2y(xA_poly):
        
        yA_poly = Eqm_Poly_x2y[0]*pow(xA_poly,6)+Eqm_Poly_x2y[1]*pow(xA_poly,5)+Eqm_Poly_x2y[2]*pow(xA_poly,4)+Eqm_Poly_x2y[3]*pow(xA_poly,3)+Eqm_Poly_x2y[4]*pow(xA_poly,2)+Eqm_Poly_x2y[5]*pow(xA_poly,1)+Eqm_Poly_x2y[6]*pow(xA_poly,0)
        
        return yA_poly
    
    def Eqm_y2x(yA_poly):
        
        xA_poly = Eqm_Poly_y2x[0]*pow(yA_poly,6)+Eqm_Poly_y2x[1]*pow(yA_poly,5)+Eqm_Poly_y2x[2]*pow(yA_poly,4)+Eqm_Poly_y2x[3]*pow(yA_poly,3)+Eqm_Poly_y2x[4]*pow(yA_poly,2)+Eqm_Poly_y2x[5]*pow(yA_poly,1)+Eqm_Poly_y2x[6]*pow(yA_poly,0)
        
        return xA_poly
    
    def Eqm_x2T(TA_poly):
        
        TA_poly = Eqm_Poly_x2T[0]*pow(TA_poly,6)+Eqm_Poly_x2T[1]*pow(TA_poly,5)+Eqm_Poly_x2T[2]*pow(TA_poly,4)+Eqm_Poly_x2T[3]*pow(TA_poly,3)+Eqm_Poly_x2T[4]*pow(TA_poly,2)+Eqm_Poly_x2T[5]*pow(TA_poly,1)+Eqm_Poly_x2T[6]*pow(TA_poly,0)
        
        return TA_poly
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # fitting q line to eqm
    
    if q != 1:
        q_int = ((-q*0)/(1-q)) + (xf/(1-q))
    else:
        q_int = Eqm_x2y(xf)
    
    q_Poly = np.polyfit([xf,0], [xf,q_int], 1)
        
    def qline_Eqm(x_q):
        
        if q != 1:
            y_q = q_Poly[0]*x_q + q_Poly[1]
        else:
            y_q = Eqm_x2y(xf)
        
        eqm_y = Eqm_x2y(x_q)
        
        F = np.empty((1))
        F[0] = y_q - eqm_y 
        
        return F
    
    x_qGuess = [0.5]
    x_q = opt.fsolve(qline_Eqm,x_qGuess)
    
    q_eqm = Eqm_x2y(x_q)
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Finding the TOL
    
    TOL_Rmin_Poly = np.polyfit([xd,x_q], [xd,Eqm_x2y(x_q)], 1)
    
    Rmin = 0.00
    Rmin = TOL_Rmin_Poly[0]/(1-TOL_Rmin_Poly[0])
    R = Rmin*Rf
    
    def qline_TOL(x_q_TOL):
        
        if q != 1:
            y_q = q_Poly[0]*x_q_TOL + q_Poly[1]
        else:
            y_q = (R*xf)/(R+1) + xd/(R+1)
        
        y_TOL = (R*x_q_TOL)/(R+1) + xd/(R+1)
        
        F = np.empty((1))
        F[0] = y_q - y_TOL 
        
        return F
    
    x_q_TOLGuess = [0.5]
    x_q_TOL = opt.fsolve(qline_TOL,x_q_TOLGuess)
    
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # fitting TOL & BOL to polynomials
    
    TOL_Poly = np.polyfit([xd,x_q_TOL], [xd,(R*x_q_TOL)/(R+1) + xd/(R+1)], 1)
    BOL_Poly = np.polyfit([xb,x_q_TOL], [xb,(R*x_q_TOL)/(R+1) + xd/(R+1)], 1)
    
    def TOL_x2y(xA_poly):
        
        yA_poly = TOL_Poly[0]*xA_poly+TOL_Poly[1]
        
        return yA_poly
    
    def BOL_x2y(xA_poly):
        
        yA_poly = BOL_Poly[0]*xA_poly+BOL_Poly[1]
        
        return yA_poly
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Making plates array
    
    xp = np.linspace(0.00,0.00,2*Max_Pl+1)
    
    All_Pl = np.array([xp[0:2*Max_Pl+1],xp[0:2*Max_Pl+1]]) # x[xp,yp], All plates is all the data points from the plate calculations
    
    All_Pl[0,0] = xd
    All_Pl[1,0] = xd
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Setting plates array
    
    def xy_All_Pl(N):
        
        if N % 2 == 0:  
            All_Pl[0,N] = All_Pl[0,N-1]
            if All_Pl[0,N-1] > x_q_TOL:
                All_Pl[1,N] = TOL_x2y(All_Pl[0,N-1])
            else:
                All_Pl[1,N] = BOL_x2y(All_Pl[0,N-1])
        
        else:
            All_Pl[0,N] = Eqm_y2x(All_Pl[1,N-1])
            All_Pl[1,N] = All_Pl[1,N-1]
        
        return All_Pl
    
    for N in range(1,len(xp)):
        xy_All_Pl(N)
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # 
    
    delx = All_Pl[0,:] - xb
    idx = sum(1 for i in delx if i > 0) + 2 # idx = num of data points along column
    
    xp = np.linspace(0.00,0.00,idx)
    Plates = np.array([xp[0:idx],xp[0:idx]]) # x[xp,yp], All plates is all the data points from the plate calculations
     
#    print('idx = ', idx)
#    print('All_Pl length = ', len(All_Pl))
#    print('Plates length = ', len(Plates))
                     
    def Act_Pl(N):
        
        Plates[0,N] = All_Pl[0,N]
        Plates[1,N] = All_Pl[1,N]
        
        return Plates
        
    for N in range (0,idx):
        Act_Pl(N) # Actual plates        
             
              
    Num_Stages = int((idx-1)/2)
    Num_Plates = Num_Stages - 1
    
    xba = Plates[0,idx-2] 
    yba = Plates[1,idx-2]
    
    qdelx = All_Pl[0,:] - x_q_TOL
    qidx = sum(1 for i in qdelx if i > 0) + 2 # idx = num of data points along column
    
    Feed_Plate = int((qidx-1)/2)
    
    D = F*(xf-xb)/(xd-xb)
    B = F - D
    
    
    #--------------------------------------------------------------------------------------------------------------------------------
    # Graphs
    
    def GUI_MT():
        plt.clf()
        plt.figure(figsize=(9,8))
        plt.plot(x[0,0:N_Size],x[1,0:N_Size],'c-',linewidth=1, label='Eqm')
        plt.plot(Plates[0,0:2*Max_Pl+1],Plates[1,0:2*Max_Pl+1],'k-',linewidth=1, label='Plates')
        plt.plot([0,1],[0,1],'k--',linewidth=1, label='45')
        plt.plot([xf,xf],[0,xf],'b-',linewidth=1, label='Feed')
        plt.plot([xd,xd],[0,xd],'b-',linewidth=1, label='Distillate')
        plt.plot([xb,xb],[0,xb],'b-',linewidth=1, label='Bottoms')
        plt.plot([xf,x_q_TOL],[xf,(R*x_q_TOL)/(R+1) + xd/(R+1)],'r-',linewidth=1, label='q Line')
        plt.plot([xd,x_q_TOL],[xd,(R*x_q_TOL)/(R+1) + xd/(R+1)],'m-',linewidth=1, label='TOL')
        plt.plot([xb,x_q_TOL],[xb,(R*x_q_TOL)/(R+1) + xd/(R+1)],'g-',linewidth=1, label='BOL')
        plt.legend(loc=4)
        plt.xlabel('xA')
        plt.ylabel('yA')
        plt.xlim([0.00, 1])
        plt.ylim([0.00, 1])
        plt.savefig('MT.png')

    x_q_TOL = float(x_q_TOL)    
    
    GUI_MT()
    
    with open('TestOutputs.csv', 'w', newline='') as csvfile:
        
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(['Variable', 'Value'])
        
        filewriter.writerow(['Rmin', Rmin])
        filewriter.writerow(['R', R])
        filewriter.writerow(['Num_Stages', Num_Stages])
        filewriter.writerow(['Num_Plates', Num_Plates])
        filewriter.writerow(['Feed_Plate', Feed_Plate])
        filewriter.writerow(['Tf', Eqm_x2T(x_q_TOL)])
        filewriter.writerow(['Td', Eqm_x2T(xd)])
        filewriter.writerow(['Tb', Eqm_x2T(xb)])
        filewriter.writerow(['D', D])
        filewriter.writerow(['B', B])
        
        
    
    