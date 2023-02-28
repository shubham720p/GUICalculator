from tkinter import *
from tkinter import ttk

c1 = "white"
c2 = "#262624"
c3 ="orange"
c4 =" Yellow"

window = Tk()
window.title("Calculator")
photo = PhotoImage(file = "cal.png")
window.iconphoto(False, photo)
window.geometry("235x318")
window.resizable(height =False , width = False)
window.configure(bg = c1)


style = ttk.Style(window)
style.theme_use("clam")


ttk.Separator(window,orient = HORIZONTAL).grid(row = 0 , columnspan =1 , ipadx = 280)

# fr1
frame1 = Frame (window , width=300 , height=56 , bg=c2, pady=0 , padx =0)
frame1.grid(row = 1 , column = 0  ,sticky = NW)
frame_buttons = Frame (window , width=300 , height=340 , bg=c1, pady=0 , padx =0)
frame_buttons.grid(row = 2 , column = 0  ,sticky = NW)
# fun**************
def entvalue(event):
    global all_values

    all_values=all_values+str(event)
    values_text.set(all_values)
def blank():
    global all_values
    all_values = ""
    values_text.set("")

def ans():
    global all_values
    result = str(eval(all_values))
    values_text.set(result)
    all_values = ""
all_values = ""
values_text = StringVar()
# f2
app_scr = Label(frame1 , width=14 , height = 2 ,textvariable=values_text, padx= 7 , anchor = "e" , bd = 0 , justify=RIGHT, font=("ivy 18 bold"),bg = c2,fg = c1)
app_scr.place(x = 0 , y = 0)
c = Button(frame_buttons ,command = blank, text = "C",width = 11 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
c.place(x =0 , y = 0 )

mod = Button(frame_buttons , text = "%", command = lambda:entvalue("%"), width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
mod.place(x =118, y = 0 )

div = Button(frame_buttons , text = "/",command = lambda:entvalue("/"),width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
div.place(x =177 , y = 0 )
# topline
b7 = Button(frame_buttons , text = "7",command = lambda:entvalue("7"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b7.place(x =0 , y = 52 )
b8 = Button(frame_buttons , text = "8",command = lambda:entvalue("8"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b8.place(x =59 , y = 52 )
b9 = Button(frame_buttons , text = "9",command = lambda:entvalue("9"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b9.place(x =118 , y = 52 )
ml = Button(frame_buttons , text = "X",command = lambda:entvalue("X"),width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
ml.place(x =177 , y = 52 )
# middleline
b4 = Button(frame_buttons , text = "4",command = lambda:entvalue("4"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b4.place(x =0 , y =104 )
b5 = Button(frame_buttons , text = "5",command = lambda:entvalue("5"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b5.place(x =59 , y = 104 )
b6 = Button(frame_buttons , text = "6",command = lambda:entvalue("6"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b6.place(x =118 , y = 104 )
su = Button(frame_buttons , text = "-",command = lambda:entvalue("-"),width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
su.place(x =177 , y = 104 )
# bottomline
b1 = Button(frame_buttons , text = "1",command = lambda:entvalue("1"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b1.place(x =0 , y =156 )
b2 = Button(frame_buttons , text = "2",command = lambda:entvalue("2"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b2.place(x =59 , y = 156 )
b3 = Button(frame_buttons , text = "3",command = lambda:entvalue("3"),width = 5 , height = 2, bg =c1, fg = c2 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b3.place(x =118 , y = 156 )
pl = Button(frame_buttons , text = "+",command = lambda:entvalue("+"),width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
pl.place(x =177 , y = 156 )
# bott-bottomline
b0 = Button(frame_buttons , text = "0",command = lambda:entvalue("0"),width = 11 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
b0.place(x =0 , y =208 )
bdot = Button(frame_buttons , text = ".",command = lambda:entvalue("."),width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
bdot.place(x =118 , y = 208 )
eq = Button(frame_buttons , text = "=",command =ans ,width = 5 , height = 2, bg =c1, fg = c3 , font=("ivy 13 bold") ,relief = RAISED,overrelief = RIDGE)
eq.place(x =177, y = 208 )






window.mainloop()
