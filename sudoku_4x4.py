from tkinter import *
from tkinter import ttk
import random,copy
import subprocess
root1=Tk()
selected_cell=[None,None]
original_puzzle=[]
curr_puzzle=[]
solution=[]
moves=[]
def open9():
    try:
        root1.destroy()
        subprocess.run(['py','sudoku_9x9.py'])
       
    except subprocess.CalledProcessError as e:
        print(f'Error running script: {e}')
def check(board,r,c,num):
    for i in range(4):
        if board[r][i]==num or board[i][c]==num:
            return False
    st_r=r//2*2
    st_c=c//2*2
    for i in range(2):
        for j in range(2):
            if board[st_r+i][st_c+j]==num:
                return False
    return True
def solve(board):
    for i in range(4):
        for j in range(4):
            if board[i][j]==0:
                nums=list(range(1,5))
                random.shuffle(nums)
                for num in nums:
                    if check(board,i,j,num):
                        board[i][j]=num
                        if solve(board):
                            return True
                        board[i][j]=0
                return False
    return True
def full_board():
    board=[[0]*4 for _ in range(4)]
    solve(board)
    return board
def copy_board(full_board,level):
    puzzle=copy.deepcopy(full_board)
    remove={'Easy':4,'Medium':8,'Hard':12}
    count=remove.get(level,8)
    while count>0:
        i=random.randint(0,3)
        j=random.randint(0,3)
        if puzzle[i][j]!=0:
            puzzle[i][j]=0
            count-=1
    return puzzle
def select_cell(i, j):
    if original_puzzle[i][j]==0:
        selected_cell[0]=i
        selected_cell[1]=j
def fill_cell(n):
    i,j=selected_cell
    if i!=None and original_puzzle[i][j]==0:
        prev_val=curr_puzzle[i][j]
        curr_puzzle[i][j] = n
        grid_btn[i][j].config(text=str(n))
        moves.append((i,j,prev_val))
        win()
def undo():
    if moves:
        i,j,prev_val=moves.pop()
        curr_puzzle[i][j]=prev_val
        grid_btn[i][j].config(text=str(prev_val) if prev_val!=0 else '')
def show():
    for i in range(4):
        for j in range(4):
            grid_btn[i][j].config(text=str(solution[i][j]))
def reset():
    moves.clear()
    for i in range(4):
        for j in range(4):
            val=original_puzzle[i][j]
            curr_puzzle[i][j]=val
            grid_btn[i][j].config(text=str(val) if val!=0 else '',state='disabled' if val!=0 else 'normal',command=lambda i=i,j=j:select_cell(i,j))
def generate():
    global original_puzzle,curr_puzzle,solution
    level=lvl_var.get() if lvl_var.get() in ['Easy','Medium','Hard'] else 'Medium'
    full=full_board()
    puzzle=copy_board(full,level)
    original_puzzle=copy.deepcopy(puzzle)
    curr_puzzle=copy.deepcopy(puzzle)
    solution=copy.deepcopy(full)
    moves.clear()
    for i in range(4):
        for j in range(4):
            val=puzzle[i][j]
            btn=grid_btn[i][j]
            btn.config(text=str(val) if val!=0 else '',state='disabled' if val!=0 else 'normal',command=lambda i=i, j=j:select_cell(i,j))
def hint():
    for i in range(4):
        for j in range(4):
            if curr_puzzle[i][j]==0:
                correct_val=solution[i][j]
                curr_puzzle[i][j]=correct_val
                grid_btn[i][j].config(text=str(correct_val))
                moves.append((i,j,0))
                win()
                return
def win():
    for i in range(4):
        for j in range(4):
            if curr_puzzle[i][j]!=solution[i][j]:
                return
    top=Toplevel(root1)
    top.title("Congratulations!")
    top.geometry("300x150")
    top.config(bg=clr4)
    Label(top,text="Sudoku Solved!",font=f3,bg=clr4,fg=clr1).pack(pady=30)
    Button(top,text="Close",command=top.destroy,bg=clr3,fg=clr5,font=f2).pack()
root1.title('Sudoku')
root1.geometry('1000x700')
root1.resizable(False,False)
clr1='#2b6777'
clr2='#c8d8e4'
clr3='#52ab98'
clr4='#f2f2f2'
clr5='#ffffff'
f1=('Helvetica',36,'bold')
f2=('Helvetica',16)
f3=('Helvetica',16,'bold')
f4=('Helvetica',22)
root1.configure(bg=clr4)
l1=Label(text='Sudoku: The 4x4 Quest',font=f1,bg=clr4,fg=clr1)
l1.pack(pady=20)
con=Frame(bg=clr4)
con.pack(padx=10,pady=10)
grid_f=Frame(con,bg=clr1,padx=4,pady=4)
grid_f.grid(row=0,column=0,padx=(10,90),pady=5)
grid_btn=[]
for i in range(4):
    row=[]
    for j in range(4):
        x=(4,2)if j%2==0 else (2,4)
        y=(4,2)if i%2==0 else(2,4)
        cell_f=Frame(grid_f,bg=clr1)
        cell_f.grid(row=i,column=j,padx=x,pady=y)
        btn=Button(cell_f,text='',font=f4,width=4,height=2,relief='flat',bg=clr5,fg=clr1,bd=1)
        btn.pack()
        row.append(btn)
    grid_btn.append(row)
side_f=Frame(con,bg=clr4)
side_f.grid(row=0,column=1,sticky='n',pady=(20,0))
lvl_f=Frame(side_f,bg=clr4)
lvl_f.grid(row=0,column=0,columnspan=2,pady=(0,40))
l2=Label(lvl_f,text='Difficulty Level: ',font=f2,bg=clr4,fg=clr1)
l2.pack(side='left')
lvl_var=StringVar()
lvl_cb=ttk.Combobox(lvl_f,textvariable=lvl_var,values=['Easy','Medium','Hard'],state='readonly',width=12,font=f2)
lvl_var.set('Medium')
lvl_cb.bind("<<ComboboxSelected>>", lambda e: generate())
lvl_cb.pack(side='left',padx=10,pady=20)
b1=Button(side_f,text='Hint',font=f3,width=10,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=hint)
b2=Button(side_f,text='Undo',font=f3,width=10,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=undo)
b3=Button(side_f,text='Show',font=f3,width=10,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=show)
b4=Button(side_f,text='Reset',font=f3,width=10,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=reset)
b5=Button(side_f,text='Exit',font=f3,width=10,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=root1.destroy)
b6=Button(side_f,text='9x9 Challenge',font=f3,width=20,height=1,bg=clr3,activebackground=clr1,fg=clr5,command=open9)
b1.grid(row=1,column=0,padx=20,pady=10)
b2.grid(row=1,column=1,padx=20,pady=10)
b3.grid(row=2,column=0,padx=20,pady=10)
b4.grid(row=2,column=1,padx=20,pady=10)
b5.grid(row=3,column=0,columnspan=2,pady=10,padx=10)
b6.grid(row=4,column=0,columnspan=2,pady=20,padx=10)
num_f=Frame(bg=clr4)
num_f.pack(pady=10)
l3=Label(num_f,text='Choose a number and place it in the grid.',font=f2,bg=clr4,fg=clr1)
l3.pack(pady=5)
num=StringVar()
for n in range(1,5):
    btn=Button(num_f,text=str(n),font=f3,width=3,height=1,bg=clr1,activebackground=clr3,fg=clr5,command=lambda n=n:fill_cell(n))
    btn.pack(side='left',padx=((80,5) if n==1 else 5))
generate()
mainloop()