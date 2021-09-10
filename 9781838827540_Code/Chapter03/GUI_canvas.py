'''
Created on May 3, 2019

@author: Burkhard A. Meier
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox


#===================================================================
class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)           # bind mouse events
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):                       
        self.show_tooltip()
        
    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()                          # get widget top-left coordinates
            y_top = self.widget.winfo_rooty() - 18                      # place tooltip above widget or it flickers
            
            self.tip_window = tk.Toplevel(self.widget)                  # create Toplevel window; parent=widget
            self.tip_window.overrideredirect(True)                      # remove surrounding toolbar window
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))        # position tooltip 
    
            label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT,
                          background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                          font=("tahoma", "8", "normal"))
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()       

#===================================================================


# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # 
tabControl.add(tab2, text='Tab 2')      # Add a second tab
tab3 = ttk.Frame(tabControl)            # 
tabControl.add(tab3, text='Tab 3')      # Add a third tab

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# Adding a Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Spinbox callback 
def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')
     
# Adding a Spinbox widget
spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=_spin) # using range
spin.grid(column=0, row=2)

# Add a Tooltip
ToolTip(spin, 'This is a Spin control')
 
# Using a scrolled Text control    
scrol_w  = 30
scrol_h  =  3
scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    

# Add a Tooltip to the ScrolledText widget 
ToolTip(scrol, 'This is a ScrolledText widget') 

# Tab Control 2 refactoring  ---------------------------------------------------------
# We are creating a container frame to hold all other widgets -- Tab2
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])  # zero-based
    elif radSel == 1: win.configure(background=colors[1])  # using list
    elif radSel == 2: win.configure(background=colors[2])

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):                             
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=6, sticky=tk.W)             # row=6

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7)        
 
# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 


# Tab Control 3 -------------------------------
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)
    

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Display a Message Box
def _msgBox():
    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')  
    
# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
menu_bar.add_cascade(label="Help", menu=help_menu)

# Change the main windows icon
win.iconbitmap('pyc.ico')

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
