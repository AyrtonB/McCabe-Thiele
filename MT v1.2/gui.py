import tkinter as tk
from tkinter import ttk

from PIL import ImageTk as imtk #, Image as im
import csv


AC_LK_A = 4.02232
AC_LK_B = 1206.53
AC_LK_C = 220.291 # (AC_LK)

AC_HK_A = 4.0854
AC_HK_B = 1348.77
AC_HK_C = 219.976 # (AC_HK)

N_Size = 1001 # (N_Size), 1001 = 0.1% accuracy for xA
Max_Pl = 50 # (Max_Pl) Maximum number of plates

Large_Font = ("Verdana", 12)
Label_Font = ("Verdana", 10)

def getval(x):
    
    Variables = []
    Values = []
    
    with open('TestOutputs.csv', 'rt') as g:
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
    
    if x == 'Rmin':
        x = float(Values[0])   
        
    if x == 'R':
        x = float(Values[1])
        
    if x == 'Num_Stages':
        x = float(Values[2])
        
    if x == 'Num_Plates':
        x = float(Values[3])
        
    if x == 'Feed_Plate':
        x = float(Values[4])
        
    if x == 'Tf':
        x = float(Values[5])
        
    if x == 'Td':
        x = float(Values[6])
        
    if x == 'Tb':
        x = float(Values[7])
        
    if x == 'D':
        x = float(Values[8])
        
    if x == 'B':
        x = float(Values[9])
    
    return x

def Decimalise(x,dec):   
    a = pow(10,dec)
    x = int(x*a)/a
    return x

def To_Print(self):
                      
    if Check_Inputs_Entered(self) == 'y':
        
        Write_Inputs_To_CSV(self)
        
        import Eqm
        
        Eqm.Pre_Output()
        
        Rmin = getval('Rmin')
        R = getval('R')
        Num_Stages = getval('Num_Stages')
        Num_Plates = getval('Num_Plates') 
        Feed_Plate = getval('Feed_Plate')
        Tf = getval('Tf')
        Td = getval('Td')
        Tb = getval('Tb')
        D = getval('D')
        B = getval('B')
        
        Rmin = Decimalise(Rmin,2)
        R = Decimalise(R,2)
        Num_Stages = int(Num_Stages)
        Num_Plates = int(Num_Plates)
        Feed_Plate = int(Feed_Plate)
        
        Tf = Decimalise(Tf,2)
        Td = Decimalise(Td,2)
        Tb = Decimalise(Tb,2)
        
        D = Decimalise(D,2)
        B = Decimalise(B,2)
        
        F = Extract_Inputs(self,'F')
        
        xd = Extract_Inputs(self,'xd')
        xf = Extract_Inputs(self,'xf')
        xb = Extract_Inputs(self,'xb')
        
        print(' ')
        print('New Run')
        print(' ')
        print('F = ', F)
        print('D = ', D)
        print('B = ', B)
        print(' ')
        print('xd = ', xd)
        print('xf = ', xf)
        print('xb = ', xb)
        print(' ')
        print('Rmin = ', Rmin)
        print('R = ', R)
        print(' ')
        print('Num_Stages = ', Num_Stages)
        print('Num_Plates = ', Num_Plates)
        print('Feed_Plate = ', Feed_Plate)
        print(' ')
        print('Tf = ', Tf)
        print('Td = ', Td)
        print('Tb = ', Tb)
        print(' ')
        
        
        self.img = imtk.PhotoImage(file="MT.png")
        self.panel = tk.Label(self, image = self.img)
        self.panel.grid(row = 0, column = 2, rowspan = 30)
        
        self.l_O_D = ttk.Label(self, text=D, background="white", relief="ridge")
        self.l_O_D.grid(row=11, column=1, sticky="ew", padx=5)
        
        self.l_O_B = ttk.Label(self, text=B, background="white", relief="ridge")
        self.l_O_B.grid(row=12, column=1, sticky="ew", padx=5)
        
        
        self.l_O_Rmin = ttk.Label(self, text=Rmin, background="white", relief="ridge")
        self.l_O_Rmin.grid(row=14, column=1, sticky="ew", padx=5)
        
        self.l_O_R = ttk.Label(self, text=R, background="white", relief="ridge")
        self.l_O_R.grid(row=15, column=1, sticky="ew", padx=5)
        
        self.l_O_Num_Stages = ttk.Label(self, text=Num_Stages, background="white", relief="ridge")
        self.l_O_Num_Stages.grid(row=17, column=1, sticky="ew", padx=5)
        
        self.l_O_Num_Plates = ttk.Label(self, text=Num_Plates, background="white", relief="ridge")
        self.l_O_Num_Plates.grid(row=18, column=1, sticky="ew", padx=5)
        
        self.l_O_Feed_Plate = ttk.Label(self, text=Feed_Plate, background="white", relief="ridge")
        self.l_O_Feed_Plate.grid(row=19, column=1, sticky="ew", padx=5)
        
        self.l_O_Tf = ttk.Label(self, text=Tf, background="white", relief="ridge")
        self.l_O_Tf.grid(row=21, column=1, sticky="ew", padx=5)
        
        self.l_O_Td = ttk.Label(self, text=Td, background="white", relief="ridge")
        self.l_O_Td.grid(row=22, column=1, sticky="ew", padx=5)
        
        self.l_O_Tb = ttk.Label(self, text=Tb, background="white", relief="ridge")
        self.l_O_Tb.grid(row=23, column=1, sticky="ew", padx=5)
        
    else:
        print('Enter All Inputs')
        self.img = imtk.PhotoImage(file="Init_MT.png")
        self.panel = tk.Label(self, image = self.img)
        self.panel.grid(row = 0, column = 2, rowspan = 30)
        
    
    
def Check_Inputs_Entered(self):
    
    Entered = 'y'
    
    if len(self.e_xf.get()) == 0:
          Entered = 'n'
    
    elif len(self.e_xd.get()) == 0:
          Entered = 'n'
          
    elif len(self.e_xb.get()) == 0:
          Entered = 'n'
          
    elif len(self.e_P_Tot.get()) == 0:
          Entered = 'n'
          
    elif len(self.e_q.get()) == 0:
          Entered = 'n'
          
    elif len(self.e_Rf.get()) == 0:
          Entered = 'n'
          
    return Entered

def Extract_Inputs(self,x): # Enter inputs from values typed in      
                
      F_In = float(self.e_F.get())
                  
      xf_In = float(self.e_xf.get())
      xd_In = float(self.e_xd.get())
      xb_In = float(self.e_xb.get())
      
      P_Tot_In = float(self.e_P_Tot.get())
      q_In = float(self.e_q.get())
      Rf_In = float(self.e_Rf.get())
      
      if x == 'F':
          x = F_In
      
      if x == 'xf':
          x = xf_In/100 
          
      if x == 'xd':
          x = xd_In/100
          
      if x == 'xb':
          x = xb_In/100
          

      if x == 'P_Tot':
          x = P_Tot_In 
          
      if x == 'q':
          x = q_In
          
      if x == 'Rf':
          x = Rf_In
      
      return x

def Write_Inputs_To_CSV(self):
    
    F = Extract_Inputs(self,'F')
    
    xf = Extract_Inputs(self,'xf')
    xd = Extract_Inputs(self,'xd')
    xb = Extract_Inputs(self,'xb')
    
    P_Tot = Extract_Inputs(self,'P_Tot')
    q = Extract_Inputs(self,'q')
    Rf = Extract_Inputs(self,'Rf')
    
    with open('Inputs.csv', 'w', newline='') as csvfile:
        
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(['Variable', 'Value'])
        
        filewriter.writerow(['F', F])
        
        filewriter.writerow(['xf', xf])
        filewriter.writerow(['xd', xd])
        filewriter.writerow(['xb', xb])
        
        filewriter.writerow(['P_Tot', P_Tot])
        filewriter.writerow(['q', q])
        filewriter.writerow(['Rf', Rf])
        
        filewriter.writerow(['AC_LK_A', AC_LK_A])
        filewriter.writerow(['AC_LK_B', AC_LK_B])
        filewriter.writerow(['AC_LK_C', AC_LK_C])
        filewriter.writerow(['AC_HK_A', AC_HK_A])
        filewriter.writerow(['AC_HK_B', AC_HK_B])
        filewriter.writerow(['AC_HK_C', AC_HK_C])
        
        filewriter.writerow(['N_Size', N_Size])
        filewriter.writerow(['Max_Pl', Max_Pl])

class ChemEngApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self,default='CES.ico')
        tk.Tk.wm_title(self, "McCabe - Thiele")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        ##### Making Labels #####
        
        self.l_Title = ttk.Label(self, text="Start Page", font=Large_Font)
        self.l_Title.grid(row=0, columnspan = 2)
        
        
        self.l_F = ttk.Label(self, text="F (kg/hr) :")
        self.l_F.grid(row=1, sticky="e", padx=5)
        
        
        self.l_xf = ttk.Label(self, text="xA of Feed (%) :")
        self.l_xf.grid(row=3, sticky="e", padx=5)
        
        self.l_xd = ttk.Label(self, text="xA of Distillate (%) :")
        self.l_xd.grid(row=4, sticky="e", padx=5)
        
        self.l_xb = ttk.Label(self, text="xA of Bottoms (%) :")
        self.l_xb.grid(row=5, sticky="e", padx=5)
        
        
        self.l_P_Tot = ttk.Label(self, text="Operating Pressure (Bar) :")
        self.l_P_Tot.grid(row=7, sticky="e", padx=5)
        
        self.l_q = ttk.Label(self, text="q :")
        self.l_q.grid(row=8, sticky="e", padx=5)
        
        self.l_Rf = ttk.Label(self, text="R factor :")
        self.l_Rf.grid(row=9, sticky="e", padx=5)
        
        ##### Making Entry Boxes #####
        
        self.e_F = ttk.Entry(self)
        self.e_F.grid(row=1, column=1, padx=5)
        
        
        self.e_xf = ttk.Entry(self)
        self.e_xf.grid(row=3, column=1, padx=5)
        
        self.e_xd = ttk.Entry(self)
        self.e_xd.grid(row=4, column=1, padx=5)
        
        self.e_xb = ttk.Entry(self)
        self.e_xb.grid(row=5, column=1, padx=5)
        
        
        self.e_P_Tot = ttk.Entry(self)
        self.e_P_Tot.grid(row=7, column=1, padx=5)
        
        self.e_q = ttk.Entry(self)
        self.e_q.grid(row=8, column=1, padx=5)
        
        self.e_Rf = ttk.Entry(self)
        self.e_Rf.grid(row=9, column=1, padx=5)       
        
        
        self.b_Run = ttk.Button(self, text="Run Simulation", command=lambda: To_Print(self))
        self.b_Run.grid(row=10, column=0, columnspan = 2, sticky="ew", padx=20)  
        
        self.img = imtk.PhotoImage(file="Init_MT.png")
        self.panel = tk.Label(self, image = self.img)
        self.panel.grid(row = 0, column = 2, rowspan = 30) 
    
#        self.b_pg1 = ttk.Button(self, text="Change Parameters",
#                            command=lambda: controller.show_frame(PageOne))
#        self.b_pg1.grid(row = 8, column=1, columnspan = 1)
        
        
        self.txtRmin = " "
        
        
        self.l_D = ttk.Label(self, text="D (kg/hr) :")
        self.l_D.grid(row=11, column=0, sticky="e", padx=5)
        
        self.l_O_D = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_D.grid(row=11, column=1, sticky="ew", padx=5)
        
        self.l_B = ttk.Label(self, text="B (kg/hr) :")
        self.l_B.grid(row=12, column=0, sticky="e", padx=5)
        
        self.l_O_B = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_B.grid(row=12, column=1, sticky="ew", padx=5)
        
        self.l_Rmin = ttk.Label(self, text="Rmin :")
        self.l_Rmin.grid(row=14, column=0, sticky="e", padx=5)
        
        self.l_O_Rmin = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Rmin.grid(row=14, column=1, sticky="ew", padx=5)
        
        self.l_R = ttk.Label(self, text="R :")
        self.l_R.grid(row=15, column=0, sticky="e", padx=5)
        
        self.l_O_R = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_R.grid(row=15, column=1, sticky="ew", padx=5)
        
        self.l_Num_Stages = ttk.Label(self, text="Number of Stages :")
        self.l_Num_Stages.grid(row=17, column=0, sticky="e", padx=5)
        
        self.l_O_Num_Stages = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Num_Stages.grid(row=17, column=1, sticky="ew", padx=5)
        
        self.l_Num_Plates = ttk.Label(self, text="Number of Plates :")
        self.l_Num_Plates.grid(row=18, column=0, sticky="e", padx=5)
        
        self.l_O_Num_Plates = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Num_Plates.grid(row=18, column=1, sticky="ew", padx=5)
        
        self.l_Feed_Plate = ttk.Label(self, text="Feed Plate :")
        self.l_Feed_Plate.grid(row=19, column=0, sticky="e", padx=5)
        
        self.l_O_Feed_Plate = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Feed_Plate.grid(row=19, column=1, sticky="ew", padx=5)
        
        self.l_Tf = ttk.Label(self, text="Tf :")
        self.l_Tf.grid(row=21, column=0, sticky="e", padx=5)
        
        self.l_O_Tf = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Tf.grid(row=21, column=1, sticky="ew", padx=5)
        
        self.l_Td = ttk.Label(self, text="Td :")
        self.l_Td.grid(row=22, column=0, sticky="e", padx=5)
        
        self.l_O_Td = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Td.grid(row=22, column=1, sticky="ew", padx=5)
        
        self.l_Tb = ttk.Label(self, text="Tb :")
        self.l_Tb.grid(row=23, column=0, sticky="e", padx=5)
        
        self.l_O_Tb = ttk.Label(self, text=" ", background="white", relief="ridge")
        self.l_O_Tb.grid(row=23, column=1, sticky="ew", padx=5)
        
        
        self.b_pg1 = ttk.Button(self, text="Edit Parameters",
                            command=lambda: controller.show_frame(PageOne))
        self.b_pg1.grid(row = 25, columnspan=2, sticky="ew", padx=20)

    
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Edit Programme Parameters", font=Large_Font)
        label.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5)
        

        self.l_F = ttk.Label(self, text=" ")
        self.l_F.grid(row=1, sticky="e", padx=5)
        
        
        self.l_xf = ttk.Label(self, text="A")
        self.l_xf.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        self.l_xd = ttk.Label(self, text="B")
        self.l_xd.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
        
        self.l_xb = ttk.Label(self, text="C")
        self.l_xb.grid(row=2, column=3, sticky="ew", padx=5, pady=5)
        
        
        self.l_P_Tot = ttk.Label(self, text="LK :")
        self.l_P_Tot.grid(row=3, sticky="e", padx=5, pady=5)
        
        self.l_q = ttk.Label(self, text="HK :")
        self.l_q.grid(row=4, sticky="e", padx=5, pady=5)
        
        
        self.l_Rf = ttk.Label(self, text=" ")
        self.l_Rf.grid(row=5, sticky="ew", padx=5, pady=5)
        
        
        self.l_Rf = ttk.Label(self, text="N_Size :")
        self.l_Rf.grid(row=6, columnspan=1, sticky="e", padx=5, pady=5)
        
        self.l_Rf = ttk.Label(self, text="Max_Pl :")
        self.l_Rf.grid(row=7, columnspan=1, sticky="e", padx=5, pady=5)
        
        ##### Making Entry Boxes #####
        
        self.e_F = ttk.Entry(self)
        self.e_F.grid(row=3, column=1, padx=5, pady=5)
        
        self.e_xf = ttk.Entry(self)
        self.e_xf.grid(row=3, column=2, padx=5, pady=5)
        
        self.e_xd = ttk.Entry(self)
        self.e_xd.grid(row=3, column=3, padx=5, pady=5)
        
        
        self.e_xb = ttk.Entry(self)
        self.e_xb.grid(row=4, column=1, padx=5, pady=5)
        
        self.e_P_Tot = ttk.Entry(self)
        self.e_P_Tot.grid(row=4, column=2, padx=5, pady=5)
        
        self.e_q = ttk.Entry(self)
        self.e_q.grid(row=4, column=3, padx=5, pady=5)
        
        
        self.e_Rf = ttk.Entry(self)
        self.e_Rf.grid(row=6, column=1, columnspan=1, padx=5, pady=5)
        
        self.e_Rf = ttk.Entry(self)
        self.e_Rf.grid(row=7, column=1, columnspan=1, padx=5, pady=5)       
        
        
        self.l_F = ttk.Label(self, text=" ")
        self.l_F.grid(row=8, sticky="e", padx=5)


        button1 = ttk.Button(self, text="Return to McCabe-Thiele",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=10, column=0, columnspan=4, sticky="ew", padx=5, pady=5)
        
        #ttk.Sizegrip(parent).grid(column=999, row=999, sticky="ew")



if __name__ == '__main__': 
    app = ChemEngApp()
    app.mainloop()