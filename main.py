from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubblesort
from quick_sort import quicksort
from merge_sort import merge_sort

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry('900x600+200+80')
root.config(bg='black')

data = []

def drawData(data,colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width/(len(data)+1)
    offset = 10
    spacing_bet_rect = 10
    nomalize_data = [i/max(data) for i in data]

    for i,height in enumerate(nomalize_data):
        x0 = i*x_width+offset+spacing_bet_rect
        y0 = canvas_height-height*400

        x1 = (i+1)*x_width
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("Arial",15,"italic bold"),fill="orange")

    root.update_idletasks()

def StartAlgorithm():
    global data
    if not data:
        return 
    if algo_menu.get()=="Quick Sort":
        quicksort(data,0,len(data)-1,drawData,speedscale.get())
        

    elif algo_menu.get()=="Bubble Sort":
        bubblesort(data,drawData,speedscale.get())

    elif algo_menu.get() == "Merge Sort":
        merge_sort(data,drawData,speedscale.get())

    drawData(data,["green" for x in range(len(data))])

    
def Generate():
    global data
    print("Selected Algorithm: "+selected_algorithm.get())
    # data = [1,8,6,4,5,12,50,19,42,50,3]
    
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeivalue = int(sizevalue.get())

    data = []

    for _ in range(sizeivalue):
        # we will add speed scaled by appending it
        data.append(random.randrange(minivalue,maxivalue+1))
    drawData(data,["red" for x in range(len(data))])


selected_algorithm = StringVar()

# label,button speed scale
mainlabel = Label(root,text="Algorithm: ",font=("Arial",16,"italic bold"),bg="white",width=10,fg="black",relief=GROOVE,bd=5)
mainlabel.place(x=0,y=0)


algo_menu = ttk.Combobox(root,width=15,font=("Arial",19,"italic bold"),textvariable=selected_algorithm,values=["Bubble Sort","Merge Sort","Quick Sort"])
algo_menu.place(x=145,y=0)
algo_menu.current(0) # by default bubble sort

random_generate = Button(root,text="Generate",bg="black",fg='white',font=("Arial",16,"italic bold"),relief=SUNKEN,activebackground="white",activeforeground="black",bd=5,width=10,command=Generate)
random_generate.place(x=750,y=60)


sizevaluelabel = Label(root,text="Size",font=("Arial",16,"italic bold"),bg="white",width=10,fg="black",relief=GROOVE,bd=5,height=2)
sizevaluelabel.place(x=0,y=60)

sizevalue = Scale(root,from_=0,to=30,resolution=1,orient=HORIZONTAL,font=("Arial",14,"italic bold"),relief=GROOVE,bd=1,width=10)
sizevalue.place(x=120,y=60)


minvaluelabel = Label(root,text="Min Value",font=("Arial",16,"italic bold"),bg="white",width=10,fg="black",relief=GROOVE,bd=5,height=2)
minvaluelabel.place(x=250,y=60)

minvalue = Scale(root,from_=0,to=10,resolution=1,orient=HORIZONTAL,font=("Arial",14,"italic bold"),relief=GROOVE,bd=1,width=10)
minvalue.place(x=370,y=60)


maxvaluelabel = Label(root,text="Max Value",font=("Arial",16,"italic bold"),bg="white",width=10,fg="black",relief=GROOVE,bd=5,height=2)
maxvaluelabel.place(x=500,y=60)

maxvalue = Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL,font=("Arial",14,"italic bold"),relief=GROOVE,bd=1,width=10)
maxvalue.place(x=620,y=60)


start = Button(root,text="Start",bg="black",fg='white',font=("Arial",16,"italic bold"),relief=SUNKEN,activebackground="white",activeforeground="black",bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=0)

speedlabel = Label(root,text="Speed: ",font=("Arial",16,"italic bold"),bg="white",width=10,fg="black",relief=GROOVE,bd=5)
speedlabel.place(x=400,y=0)

speedscale = Scale(root,from_=0.1,to=5.0,resolution=0.2,length=200,digits=2,orient=HORIZONTAL,font=("Arial",14,"italic bold"),relief=GROOVE,bd=1,width=10)
speedscale.place(x=520,y=0)


canvas = Canvas(root,width=870,height=450,bg="black")
canvas.place(x=10,y=130)

root.mainloop()