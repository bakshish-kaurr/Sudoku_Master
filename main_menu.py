from tkinter import *
import subprocess
root=Tk()
def open4():    
    try:
        subprocess.run(['py','sudoku_4x4.py'])
    except subprocess.CalledProcessError as e:
        print(f'Error running script: {e}')
def open9():
    try:
        subprocess.run(['py','sudoku_9x9.py'])
    except subprocess.CalledProcessError as e:
        print(f'Error running script: {e}')        
root.title('Sudoku')
root.geometry('300x300')
root.resizable(False,False)
clr1='#2b6777'
clr2='#c8d8e4'
clr3='#52ab98'
clr4='#f2f2f2'
clr5='#ffffff'
f1=('Helvetica',25,'bold')
f2=('Helvetica',14)
f3=('Helvetica',10)
root.configure(bg=clr4)
l1=Label(text='Sudoku Master',font=f1,bg=clr4,fg=clr1)
l1.pack(pady=20)
b1=Button(text='4x4 Quest',font=f2,width=12,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=open4)
b2=Button(text='9x9 Challenge',font=f2,width=12,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=open9)
b3=Button(text='Exit',font=f3,width=5,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=root.destroy)
b1.pack(padx=20,pady=10)
b2.pack(padx=20,pady=10)
b3.pack(padx=(180,0),pady=30)
mainloop()