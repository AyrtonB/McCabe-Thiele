import tkinter as tk
from tkinter import ttk

from PIL import ImageTk as imtk #, Image as im
import csv


#AC_LK = np.array([4.02232,1206.53,220.291]) # (AC_LK)
#AC_HK = np.array([4.0854,1348.77,219.976]) # (AC_HK)

AC_LK_A = 4.02232
AC_LK_B = 1206.53
AC_LK_C = 220.291 # (AC_LK)

AC_HK_A = 4.0854
AC_HK_B = 1348.77
AC_HK_C = 219.976 # (AC_HK)

N_Size = 1001 # (N_Size), 1001 = 0.1% accuracy for xA
Max_Pl = 30 # (Max_Pl) Maximum number of plates

Large_Font = ("Verdana", 12)
Label_Font = ("Verdana", 10)

def Decimalise(x,dec):   
    a = pow(10,dec)
    x = int(x*a)/a
    return x

def To_Print(self):
                      
    if Check_Inputs_Entered(self) == 'y':
        
        Write_Inputs_To_CSV(self)
        
        import Eqm
        
        Eqm.Pre_Output()
        
        Rmin = Decimalise(Eqm.Outputs('Rmin'),3)
        R = Decimalise(Eqm.Outputs('R'),3)
        Num_Plates = Eqm.Outputs('Num_Plates')
        x_q_TOL = Decimalise(Eqm.Outputs('x_q_TOL'),3)
        
        xd = Extract_Inputs(self,'xd')
        xf = Extract_Inputs(self,'xf')
        xb = Extract_Inputs(self,'xb')
        
        print('xd = ', xd)
        print('xf = ', xf)
        print('xb = ', xb)
        print(' ')
        print('Rmin = ', Rmin)
        print('R = ', R)
        print('Num_Plates = ', Num_Plates)
        print('x_q_TOL = ', x_q_TOL)
        
        del Eqm
    
    else:
        print('Enter All Inputs')
        
    
    
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
                
      xf_In = float(self.e_xf.get())
      xd_In = float(self.e_xd.get())
      xb_In = float(self.e_xb.get())
      
      P_Tot_In = float(self.e_P_Tot.get())
      q_In = float(self.e_q.get())
      Rf_In = float(self.e_Rf.get())
      
                              
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
        tk.Tk.wm_title(self, "ChemEng")

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
        
        
        self.l_xf = ttk.Label(self, text="xA of Feed (%)")
        self.l_xf.grid(row=1, sticky="e", padx=5)
        
        self.l_xd = ttk.Label(self, text="xA of Distillate (%)")
        self.l_xd.grid(row=2, sticky="e", padx=5)
        
        self.l_xb = ttk.Label(self, text="xA of Bottoms (%)")
        self.l_xb.grid(row=3, sticky="e", padx=5)
        
        
        self.l_P_Tot = ttk.Label(self, text="Operating Pressure")
        self.l_P_Tot.grid(row=5, sticky="e", padx=5)
        
        self.l_q = ttk.Label(self, text="q")
        self.l_q.grid(row=6, sticky="e", padx=5)
        
        self.l_Rf = ttk.Label(self, text="R factor")
        self.l_Rf.grid(row=7, sticky="e", padx=5)
        
        ##### Making Entry Boxes #####
        
        self.e_xf = ttk.Entry(self)
        self.e_xf.grid(row=1, column=1)
        
        self.e_xd = ttk.Entry(self)
        self.e_xd.grid(row=2, column=1)
        
        self.e_xb = ttk.Entry(self)
        self.e_xb.grid(row=3, column=1)
        
        
        self.e_P_Tot = ttk.Entry(self)
        self.e_P_Tot.grid(row=5, column=1)
        
        self.e_q = ttk.Entry(self)
        self.e_q.grid(row=6, column=1)
        
        self.e_Rf = ttk.Entry(self)
        self.e_Rf.grid(row=7, column=1)       
        
        
        self.b_Run = ttk.Button(self, text="Click to Run", command=lambda: RUN(self))
        self.b_Run.grid(row=8, column=0, columnspan = 2)  
        
        self.img = imtk.PhotoImage(file="MT.png")
        self.panel = tk.Label(self, image = self.img)
        self.panel.grid(row = 0, column = 2, rowspan = 10) 
    
        self.b_pg1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        self.b_pg1.grid(row = 9, columnspan = 2)
        
        def RUN(self):
        
            To_Print(self)
            
            self.img = imtk.PhotoImage(file="MT.png")
            self.panel = tk.Label(self, image = self.img)
            self.panel.grid(row = 0, column = 2, rowspan = 10) 

    
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="Page One!!!", font=Large_Font)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



if __name__ == '__main__': 
    app = ChemEngApp()
    app.mainloop()