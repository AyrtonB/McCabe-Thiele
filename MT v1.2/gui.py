import tkinter as tk
from tkinter import ttk

from PIL import ImageTk as imtk, Image as im


Large_Font = ("Verdana", 12)
Label_Font = ("Verdana", 10)


def To_Print(self):
    
    import Eqm as Eqm
    
    def Outputs(self, x):
        
        if x == 'Num_Plates':
            x = Eqm.Outputs('Num_Plates')
            
        elif x == 'R':
            x = Eqm.Outputs(self,'R')
            
        elif x == 'Rmin':
            x = Eqm.Outputs('Rmin')
                    
        elif x == 'x_q_TOL':
            x = float(Eqm.Outputs('x_q_TOL'))
    
        return x
    
    #Num_Plates = Outputs('Num_Plates')
    #Rmin = Outputs('Rmin')
    R = Outputs(self, 'R')
    #x_q_TOL = Outputs('x_q_TOL')
    
    if Inputs_Entered(self) == 'y':
        xf = Extract_Inputs(self,'xf')
        xd = Extract_Inputs(self,'xd')
        print('xf = ', xf)
        print('xd = ', xd)
        print('R = ', R)
    
    else:
        print('Enter All Inputs')
    
def Inputs_Entered(self):
    
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


class ChemEngApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self,default='clienticon.ico')
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
        
        
        self.b_Run = ttk.Button(self, text="Click to Run", command=lambda: To_Print(self))
        self.b_Run.grid(row=8, column=0, columnspan = 2)   
        
        self.img = imtk.PhotoImage(im.open("x.png"))
        self.panel = tk.Label(self, image = self.img)
        self.panel.grid(row = 0, column = 2, rowspan = 10) 
    
        self.b_pg1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        self.b_pg1.grid(row = 9, columnspan = 2)

    
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