from tkinter import *
import socket
import sys
def menu():
    def re():
        j=e1.get()
        t=j.upper()
        name.append(t)
        y5.config(text=name)
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='orange')
    y5=Label(r,text="",font=('times new roman',20,'italic'),pady=15,bg='orange',fg='dark slate blue',anchor=CENTER)
    y5.pack()
    re()
    name.pop()
    p=Label(r,text="////// MENU //////",font=('arial',20,'bold'),pady=15,bg='orange',anchor=CENTER)
    p.pack()
    f=Button(r,text='VEG',fg='white',bg='coral1',width=15,command=veg)
    f.pack(padx=5,pady=15)
    f2=Button(r,text='NON-VEG',fg='white',bg='black',width=15,command=nonveg)
    f2.pack(padx=5,pady=15)
    f3=Button(r,text='DRINKS',fg='white',bg='lightblue3',width=15,command=drinks)
    f3.pack(padx=5,pady=15)
    f4=Button(r,text='ICE-CREAMS',fg='white',bg='BROWN',width=15,command=ice)
    f4.pack(padx=5,pady=15)
    g66=Button(r,text='CART',bg='cornsilk3',width=15,command=cart)
    g66.pack(padx=5,pady=15,side=LEFT)    
    g46=Button(r,text='BILL',bg='grey',width=15,command=bill)
    g46.pack(padx=5,pady=15,side=RIGHT)
    r.mainloop()
def send():
    fp=open('order.txt','a')
    fp.write("Name : "+t+" Table Number : "+table+"\n")
    def count(elements):
        if elements[-1] == '.':
            elements = elements[0:len(elements) - 1]
        if elements in dictionary:
            dictionary[elements] += 1
        else:
            dictionary.update({elements: 1}) 
    dictionary = {}
    for elements in lis:
        count(elements)
    for allkeys in dictionary:
        cost = 0
        cost = result1[allkeys]*dictionary[allkeys]
        fp.write(allkeys+" "*2+"("+str(dictionary[allkeys])+")"+" "*20+str(cost)+"\n")
    fp.close()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='orange')
    port = 60000
    s = socket.socket()
    host = socket.gethostname()
    s.connect((host,port))
    y5=Label(r,text="Connecting to Cheif...Please Wait ",font=('times new roman',20,'italic'),pady=15,bg='orange',fg='dark slate blue',anchor=CENTER)
    y5.pack()
    r.mainloop()
    r.destroy()
    r1=Tk()
    r1.geometry("950x550+300+0")
    r1.configure(background='CadetBlue1')
    y5=Label(r,text="Connected to Cheif,Your Food is being Prepared",font=('times new roman',20,'italic'),pady=15,bg='orange',fg='dark slate blue',anchor=CENTER)
    y5.pack()
    r1.mainloop()
    filename='order.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    s.send(l)
    r1.destroy()
    print('Order Sent')
    s.close()
def deleteall():
        lis=[]
        c=[0,0,0,0,0]
        e=[0,0,0,0]
        a=[0,0,0,0]
        l=[0,0,0,0]
        g=[0,0,0]
        h=[0,0,0,0,0]
        f=[0,0,0,0]
        d=[0,0,0,0,0,0,0]
def bill():
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='cornsilk4')
    y5=Label(r,text='////// BILL //////',font=('arial',20,'bold'),pady=15,bg='cornsilk4',anchor=CENTER)
    y5.pack()
    def count(elements):
        if elements[-1] == '.':
            elements = elements[0:len(elements) - 1]
        if elements in dictionary:
            dictionary[elements] += 1
        else:
            dictionary.update({elements: 1}) 
    dictionary = {}
    indd = 0
    for elements in lis:
        count(elements)
    for allkeys in dictionary:
        cost = 0
        cost = result1[allkeys]*dictionary[allkeys]
        label = Label(r,text=allkeys+" "*2+"("+str(dictionary[allkeys])+")"+" "*20+str(cost),font=('arial',10,'bold'),bg="cornsilk4",anchor=W)
        label.pack()
    g2=Button(r,text='EMPTY CART',bg='cornsilk4',width=15,command=deleteall)
    g2.pack(padx=40,pady=10,side=LEFT)
    g5=Button(r,text='MENU',bg='cornsilk4',width=15,command=menu)
    g5.pack(padx=40,pady=10,side=LEFT)
    g5=Button(r,text='BACK',bg='cornsilk4',width=15,command=r.destroy)
    g5.pack(padx=40,pady=10,side=RIGHT)
    g6=Button(r,text='SEND',bg='cornsilk4',width=15,command=send)
    g6.pack(padx=40,pady=10,side=RIGHT)
    r.mainloop()
def cart():
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='cornsilk4')
    y5=Label(r,text='////// CART //////',font=('arial',20,'bold'),pady=15,bg='cornsilk4',anchor=CENTER)
    y5.pack()
    sc=Scrollbar(root)
    sc.pack(side=RIGHT ,fill= Y)
    myl=Listbox(r,selectbackground='cornsilk4',highlightcolor='cornsilk4',yscrollcommand=sc.set)
    def count(elements):
        if elements[-1] == '.':
            elements = elements[0:len(elements) - 1]
        if elements in dictionary:
            dictionary[elements] += 1
        else:
            dictionary.update({elements: 1})
    dictionary = {}
    indd = 0
    for elements in lis:
        count(elements)
    for allkeys in dictionary:
        indd += 1
        myl.insert(END,str(indd)+"."+allkeys+" "*2+"("+str(dictionary[allkeys])+")")
    myl.pack(fill=BOTH)
    sc.config(command=myl.yview)
    g4=Button(r,text='EMPTY CART',bg='cornsilk4',width=15,command=deleteall)
    g4.pack(padx=40,pady=10,side=LEFT)
    g5=Button(r,text='MENU',bg='cornsilk4',width=15,command=menu)
    g5.pack(padx=40,pady=10,side=LEFT)
    g6=Button(r,text='BACK',bg='cornsilk4',width=15,command=r.destroy)
    g6.pack(padx=40,pady=10,side=RIGHT)
    g46=Button(r,text='BILL',bg='cornsilk4',width=15,command=bill)
    g46.pack(padx=40,pady=15,side=RIGHT)
    r.mainloop()
def startersveg():
    count={"ALOO-65":0,"VEG-MANCHURIA":1,"VEG-65":2,"GOBI-65":3,"GOBI-MANCHURIA":4}
    def additem(i):
        c[count[i]] += 1
        lis.append(i)
        r.destroy()
        startersveg()
    def removeitem(j):
        if(c[count[j]]>0):
            c[count[j]] -=1
            lis.remove(j)
            r.destroy()
            startersveg()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='cyan')
    w=Label(r,text='////// STARTERS-VEG //////',font=('arial',20,'bold'),pady=15,bg='cyan',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='cyan',anchor=W)
    w5.pack()
    w0=Label(r,text='1.ALOO65\t\t\t\t\t190',pady=15,padx=15,bg='cyan',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("ALOO-65")).place(x=700,y=130)
    w00 = Label(r,text=c[0],padx=4,pady=5).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("ALOO-65")).place(x=740,y=130)
    w1=Label(r,text='2.VEG-MANCHURIA\t\t\t\t100',pady=15,padx=15,bg='cyan',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("VEG-MANCHURIA")).place(x=700,y=170)
    w01 = Label(r,text=c[1],padx=4,pady=5).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("VEG-MANCHURIA")).place(x=740,y=170)
    w1=Label(r,text='3.VEG-65\t\t\t\t\t\t100',pady=15,padx=15,bg='cyan',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("VEG-65")).place(x=700,y=210)
    w02 = Label(r,text=c[2],padx=4,pady=5).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("VEG-65")).place(x=740,y=210)
    w1=Label(r,text='4.GOBI-65\t\t\t\t\t100',pady=15,padx=15,bg='cyan',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("GOBI-65")).place(x=700,y=250)
    w03 = Label(r,text=c[3],padx=4,pady=5).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("GOBI-65")).place(x=740,y=250)
    w1=Label(r,text='5.GOBI-MANCHURIA\t\t\t\t100',pady=15,padx=15,bg='cyan',anchor=W).place(x=290,y=280)
    b2 = Button(r,text="+",command=lambda :additem("GOBI-MANCHURIA")).place(x=700,y=290)
    w04 = Label(r,text=c[4],padx=4,pady=5).place(x=720,y=290)
    b3 = Button(r,text="-",command=lambda :removeitem("GOBI-MANCHURIA")).place(x=740,y=290)
    g5=Button(r,text='CART',bg='cyan',width=15,command=cart).place(x=100,y=370)
    g6=Button(r,text='MENU',bg='cyan',width=15,command=menu).place(x=300,y=370)
    g66=Button(r,text='BACK',bg='cyan',width=15,command=r.destroy).place(x=500,y=370)
    g46=Button(r,text='BILL',bg='cyan',width=15,command=bill).place(x=700,y=370)
    r.mainloop()
def soupsveg():
    count={"VEG-MANCHO-SOUP":0,"VEG-CORN-SOUP":1,"VEG-MUSHROOM-SOUP":2,"SWEET-CORN-SOUP":3}
    def additem(i):
        a[count[i]] += 1
        lis.append(i)
        r.destroy()
        soupsveg()
    def removeitem(j):
        if(a[count[j]]>0):
            a[count[j]] -=1
            lis.remove(j)
            r.destroy()
            soupsveg()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='blue')
    w=Label(r,text='////// SOUPS-VEG //////',font=('arial',20,'bold'),pady=15,bg='blue',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='blue',anchor=W)
    w5.pack()
    w0=Label(r,text='1.VEG-MANCHO-SOUP\t\t\t\t180',pady=15,padx=15,bg='blue',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("VEG-MANCHO-SOUP")).place(x=700,y=130)
    w00 = Label(r,text=a[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("VEG-MANCHO-SOUP")).place(x=740,y=130)
    w1=Label(r,text='2.VEG-CORN-SOUP\t\t\t\t160',pady=15,padx=15,bg='blue',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("VEG-CORN-SOUP")).place(x=700,y=170)
    w01 = Label(r,text=a[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("VEG-CORN-SOUP")).place(x=740,y=170)
    w1=Label(r,text='3.VEG-MUSHROOM-SOUP\t\t\t\t160',pady=15,padx=15,bg='blue',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("VEG-MUSHROOM-SOUP")).place(x=700,y=210)
    w02 = Label(r,text=a[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("VEG-MUSHROOM-SOUP")).place(x=740,y=210)
    w1=Label(r,text='4.SWEET-CORN-SOUP\t\t\t\t160',pady=15,padx=15,bg='blue',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("SWEET-CORN-SOUP")).place(x=700,y=250)
    w03 = Label(r,text=a[3],padx=4,pady=4).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("SWEET-CORN-SOUP")).place(x=740,y=250)
    g5=Button(r,text='CART',bg='blue',width=15,command=cart).place(x=100,y=370)
    g6=Button(r,text='MENU',bg='blue',width=15,command=menu).place(x=300,y=370)
    g66=Button(r,text='BACK',bg='blue',width=15,command=r.destroy).place(x=500,y=370)
    g46=Button(r,text='BILL',bg='blue',width=15,command=bill).place(x=700,y=370)
    r.mainloop()
def biryaniveg():
    count={"ALOO-BIRYANI":0,"VEG-BIRYANI":1,"PANEER-BIRYANI":2,"VEG-FRIED-RICE":3}
    def additem(i):
        e[count[i]] += 1
        lis.append(i)
        r.destroy()
        biryaniveg()
    def removeitem(j):
        if(e[count[j]]>0):
            e[count[j]] -=1
            lis.remove(j)
            r.destroy()
            biryaniveg()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='pink')
    w=Label(r,text='////// BIRYANI-VEG //////',font=('arial',20,'bold'),pady=15,bg='pink',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='pink',anchor=W)
    w5.pack()
    w0=Label(r,text='1.ALOO-BIRYANI\t\t\t\t220',pady=15,padx=15,bg='pink',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("ALOO-BIRYANI")).place(x=700,y=130)
    w00 = Label(r,text=e[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("ALOO-BIRYANI")).place(x=740,y=130)
    w1=Label(r,text='2.VEG-BIRYANI\t\t\t\t200',pady=15,padx=15,bg='pink',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("VEG-BIRYANI")).place(x=700,y=170)
    w01 = Label(r,text=e[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("VEG-BIRYANI")).place(x=740,y=170)
    w1=Label(r,text='3.PANEER-BIRYANIt\t\t\t160',pady=15,padx=15,bg='pink',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("PANEER-BIRYANI")).place(x=700,y=210)
    w02 = Label(r,text=e[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("PANEER-BIRYANI")).place(x=740,y=210)
    w1=Label(r,text='4.VEG-FRIED-RICE\t\t\t\t100',pady=15,padx=15,bg='pink',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("VEG-FRIED-RICE")).place(x=700,y=250)
    w03 = Label(r,text=e[3],padx=4,pady=4).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("VEG-FRIED-RICE")).place(x=740,y=250)
    g5=Button(r,text='CART',bg='pink',width=15,command=cart).place(x=100,y=370)
    g6=Button(r,text='MENU',bg='pink',width=15,command=menu).place(x=300,y=370)
    g66=Button(r,text='BACK',bg='pink',width=15,command=r.destroy).place(x=500,y=370)
    g46=Button(r,text='BILL',bg='pink',width=15,command=bill).place(x=700,y=370)
    r.mainloop()
def veg():
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='coral1')
    w=Label(r,text='////// VEG-MENU //////',font=('arial',20,'bold'),pady=15,bg='coral1',anchor=CENTER)
    w.pack()
    g2=Button(r,text='STARTERS',bg='coral1',width=15,command=startersveg)
    g2.pack(padx=5,pady=15)
    g3=Button(r,text='SOUPS',bg='coral1',width=15,command=soupsveg)
    g3.pack(padx=5,pady=15)
    g4=Button(r,text='BIRYANI',bg='coral1',width=15,command=biryaniveg)
    g4.pack(padx=5,pady=15)
    g5=Button(r,text='CART',bg='coral1',width=15,command=cart)
    g5.pack(padx=45,pady=15,side=LEFT)
    g6=Button(r,text='MENU',bg='coral1',width=15,command=menu)
    g6.pack(padx=45,pady=15,side=LEFT)
    g66=Button(r,text='BILL',bg='coral1',width=15,command=bill)
    g66.pack(padx=45,pady=15,side=RIGHT)    
    g46=Button(r,text='BACK',bg='coral1',width=15,command=r.destroy)
    g46.pack(padx=45,pady=15,side=RIGHT)
    r.mainloop()
def startersnonveg():
    count={"CHICK-65":0,"NON-MANCHURIA":1,"NON-65":2,"CHILLI-MANCHURIA":3}
    def additem(i):
        l[count[i]] += 1
        lis.append(i)
        r.destroy()
        startersnonveg()
    def removeitem(j):
        if(l[count[j]]>0):
            l[count[j]] -=1
            lis.remove(j)
            r.destroy()
            startersnonveg()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='grey')
    w=Label(r,text='////// STARTERS-NON-VEG //////',font=('arial',20,'bold'),pady=15,bg='grey',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='grey',anchor=W)
    w5.pack()
    w0=Label(r,text='1.CHICK-65\t\t\t\t\t150',pady=15,padx=15,bg='grey',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("CHICK-65")).place(x=700,y=130)
    w00 = Label(r,text=l[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("CHICK-65")).place(x=740,y=130)
    w1=Label(r,text='2.NON-MANCHURIA\t\t\t\t200',pady=15,padx=15,bg='grey',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("NON-MANCHURIA")).place(x=700,y=170)
    w01 = Label(r,text=l[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("NON-MANCHURIA")).place(x=740,y=170)
    w1=Label(r,text='3.NON-65\t\t\t\t\t150',pady=15,padx=15,bg='grey',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("NON-65")).place(x=700,y=210)
    w02 = Label(r,text=l[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("NON-65")).place(x=740,y=210)
    w1=Label(r,text='4.CHILLI-MANCHURIA\t\t\t\t200',pady=15,padx=15,bg='grey',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("CHILLI-MANCHURIA")).place(x=700,y=250)
    w03 = Label(r,text=l[3],padx=4,pady=4).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("CHILLI-MANCHURIA")).place(x=740,y=250)
    g5=Button(r,text='CART',bg='grey',width=15,command=cart).place(x=100,y=370)
    g6=Button(r,text='MENU',bg='grey',width=15,command=menu).place(x=300,y=370)
    g66=Button(r,text='BACK',bg='grey',width=15,command=r.destroy).place(x=500,y=370)
    g46=Button(r,text='BILL',bg='grey',width=15,command=bill).place(x=700,y=370)
    r.mainloop()
def soupsnonveg():
    count={"NON-MANCHO-SOUP":0,"CHICKEN-SOUP":1,"NON-BONE-SOUP":2,"CHILLI-BONE-SOUP":3}
    def additem(i):
        f[count[i]] += 1
        lis.append(i)
        r.destroy()
        soupsnonveg()
    def removeitem(j):
        if(f[count[j]]>0):
            f[count[j]] -=1
            lis.remove(j)
            r.destroy()
            soupsnonveg()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='orange')
    w=Label(r,text='////// SOUPS-NON-VEG //////',font=('arial',20,'bold'),pady=15,bg='orange',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='orange',anchor=W)
    w5.pack()
    w0=Label(r,text='1.NON-MANCHO-SOUP\t\t\t\t300',pady=15,padx=15,bg='orange',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("NON-MANCHO-SOUP")).place(x=700,y=130)
    w00 = Label(r,text=f[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("NON-MANCHO-SOUP")).place(x=740,y=130)
    w1=Label(r,text='2.CHICKEN-SOUP\t\t\t\t\t250',pady=15,padx=15,bg='orange',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("CHICKEN-SOUP")).place(x=700,y=170)
    w01 = Label(r,text=f[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("CHICKEN-SOUP")).place(x=740,y=170)
    w1=Label(r,text='3.NON-BONE-SOUP\t\t\t\t350',pady=15,padx=15,bg='orange',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("NON-BONE-SOUP")).place(x=700,y=210)
    w02 = Label(r,text=f[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("NON-BONE-SOUP")).place(x=740,y=210)
    w1=Label(r,text='4.CHILLI-BONE-SOUP\t\t\t\t150',pady=15,padx=15,bg='orange',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("CHILLI-BONE-SOUP")).place(x=700,y=250)
    w03 = Label(r,text=f[3],padx=4,pady=4).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("CHILLI-BONE-SOUP")).place(x=740,y=250)
    g5=Button(r,text='CART',bg='orange',width=15,command=cart).place(x=100,y=370)
    g6=Button(r,text='MENU',bg='orange',width=15,command=menu).place(x=300,y=370)
    g66=Button(r,text='BACK',bg='orange',width=15,command=r.destroy).place(x=500,y=370)
    g46=Button(r,text='BILL',bg='orange',width=15,command=bill).place(x=700,y=370)
    r.mainloop()
def biryaninonveg():
    count={"CHICK-BIRYANI":0,"MASALA-BIRYANI":1,"MUTTON-BIRYANI":2}
    def additem(i):
        g[count[i]] += 1
        lis.append(i)
        r.destroy()
        biryaninonveg()
    def removeitem(j):
        if(g[count[j]]>0):
            g[count[j]] -=1
            lis.remove(j)
            r.destroy()
            biryaninonveg()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='khaki4')
    w=Label(r,text='////// BIRYANI-NON-VEG //////',font=('arial',20,'bold'),pady=15,bg='khaki4',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='khaki4',anchor=W)
    w5.pack()
    w0=Label(r,text='1.CHICK-BIRYANI\t\t\t\t\t250',pady=15,padx=15,bg='khaki4',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("CHICK-BIRYANI")).place(x=700,y=130)
    w00 = Label(r,text=g[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("CHICK-BIRYANI")).place(x=740,y=130)
    w1=Label(r,text='2.MASALA-BIRYANI\t\t\t\t200',pady=15,padx=15,bg='khaki4',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("MASALA-BIRYANI")).place(x=700,y=170)
    w01 = Label(r,text=g[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("MASALA-BIRYANI")).place(x=740,y=170)
    w1=Label(r,text='3.MUTTON-BIRYANI\t\t\t\t350',pady=15,padx=15,bg='khaki4',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("MUTTON-BIRYANI")).place(x=700,y=210)
    w02 = Label(r,text=g[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("MUTTON-BIRYANI")).place(x=740,y=210)
    g5=Button(r,text='CART',bg='khaki4',width=15,command=cart).place(x=100,y=370)
    g6=Button(r,text='MENU',bg='khaki4',width=15,command=menu).place(x=300,y=370)
    g66=Button(r,text='BACK',bg='khaki4',width=15,command=r.destroy).place(x=500,y=370)
    g46=Button(r,text='BILL',bg='khaki4',width=15,command=bill).place(x=700,y=370)
    r.mainloop()
def nonveg():
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='black')
    w=Label(r,text='////// NON-VEG-MENU //////',font=('arial',20,'bold'),pady=15,fg='white',bg='black',anchor=CENTER)
    w.pack()
    g2=Button(r,text='STARTERS',width=15,bg='black',fg='white',command=startersnonveg)
    g2.pack(padx=5,pady=15)
    g3=Button(r,text='SOUPS',width=15,bg='black',fg='white',command=soupsnonveg)
    g3.pack(padx=5,pady=15)
    g4=Button(r,text='BIRYANI',width=15,bg='black',fg='white',command=biryaninonveg)
    g4.pack(padx=5,pady=15)
    g5=Button(r,text='CART',width=15,bg='black',fg='white',command=cart)
    g5.pack(padx=45,pady=15,side=LEFT)
    g6=Button(r,text='MENU',width=15,bg='black',fg='white',command=menu)
    g6.pack(padx=45,pady=15,side=LEFT)
    g66=Button(r,text='BILL',width=15,bg='black',fg='white',command=bill)
    g66.pack(padx=45,pady=15,side=RIGHT)    
    g46=Button(r,text='BACK',width=15,bg='black',fg='white',command=r.destroy)
    g46.pack(padx=45,pady=15,side=RIGHT)
    r.mainloop()
def drinks():
    count={"COKE":0,"THUMBS-UP":1,"MAAZA":2,"FROOTI":3,"MOUNTAIN-DEW":4,"MIRINDA":5,"SPRITE":6}
    def additem(i):
        d[count[i]] += 1
        lis.append(i)
        r.destroy()
        drinks()
    def removeitem(j):
        if(d[count[j]]>0):
            d[count[j]] -=1
            lis.remove(j)
            r.destroy()
            drinks()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='black')
    w=Label(r,text='////// DRINKS //////',font=('arial',20,'bold'),pady=15,bg='black',fg='white',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='black',fg='white',anchor=W)
    w5.pack()
    w0=Label(r,text='1.COKE\t\t\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("COKE"),bg='black',fg='white').place(x=700,y=130)
    w00 = Label(r,text=d[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("COKE"),bg='black',fg='white').place(x=740,y=130)
    w1=Label(r,text='2.THUMBS-UP\t\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("THUMBS-UP"),bg='black',fg='white').place(x=700,y=170)
    w01 = Label(r,text=d[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("THUMBS-UP"),bg='black',fg='white').place(x=740,y=170)
    w1=Label(r,text='3.MAAZA\t\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("MAAZA"),bg='black',fg='white').place(x=700,y=210)
    w02 = Label(r,text=d[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("MAAZA"),bg='black',fg='white').place(x=740,y=210)
    w1=Label(r,text='4.FROOTI\t\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("FROOTI"),bg='black',fg='white').place(x=700,y=250)
    w03 = Label(r,text=d[3],padx=4,pady=4).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("FROOTI"),bg='black',fg='white').place(x=740,y=250)
    w1=Label(r,text='5.MOUNTAIN-DEW\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=280)
    b2 = Button(r,text="+",command=lambda :additem("MOUNTAIN-DEW"),bg='black',fg='white').place(x=700,y=290)
    w04 = Label(r,text=d[4],padx=4,pady=4).place(x=720,y=290)
    b3 = Button(r,text="-",command=lambda :removeitem("MOUNTAIN-DEW"),bg='black',fg='white').place(x=740,y=290)
    w1=Label(r,text='6.MIRINDA\t\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=320)
    b2 = Button(r,text="+",command=lambda :additem("MIRINDA"),bg='black',fg='white').place(x=700,y=330)
    w04 = Label(r,text=d[5],padx=4,pady=4).place(x=720,y=330)
    b3 = Button(r,text="-",command=lambda :removeitem("MIRINDA"),bg='black',fg='white').place(x=740,y=330)
    w1=Label(r,text='7.SPRITE\t\t\t\t\t\t35',pady=15,padx=15,bg='black',fg='white',anchor=W).place(x=290,y=360)
    b2 = Button(r,text="+",command=lambda :additem("SPRITE"),bg='black',fg='white').place(x=700,y=370)
    w04 = Label(r,text=d[6],padx=4,pady=4).place(x=720,y=370)
    b3 = Button(r,text="-",command=lambda :removeitem("SPRITE"),bg='black',fg='white').place(x=740,y=370)
    g5=Button(r,text='CART',width=15,bg='black',fg='white',command=cart).place(x=100,y=430)
    g6=Button(r,text='MENU',width=15,bg='black',fg='white',command=menu).place(x=300,y=430)
    g66=Button(r,text='BACK',bg='black',fg='white',width=15,command=r.destroy).place(x=500,y=430)
    g46=Button(r,text='BILL',width=15,bg='black',fg='white',command=bill).place(x=700,y=430)
    r.mainloop()
def ice():
    count={"VANILLA":0,"STRAWBERRY":1,"BUTTER-SCOTCH":2,"MIXED-FRUIT":3,"CHOCOLATE":4}
    def additem(i):
        h[count[i]] += 1
        lis.append(i)
        r.destroy()
        ice()
    def removeitem(j):
        if(h[count[j]]>0):
            h[count[j]] -=1
            lis.remove(j)
            r.destroy()
            ice()
    r=Tk()
    r.geometry("950x550+300+0")
    r.configure(background='SeaGreen4')
    w=Label(r,text='////// ICE-CREAMS //////',font=('arial',20,'bold'),pady=15,bg='SeaGreen4',anchor=CENTER)
    w.pack()
    w5=Label(r,text='ITEMS\t\tRATES',font=('arial',20,'bold'),pady=15,bg='SeaGreen4',anchor=W)
    w5.pack()
    w0=Label(r,text='1.VANILLA\t\t\t\t\t50',pady=15,padx=15,bg='SeaGreen4',anchor=W).place(x=290,y=120)
    b = Button(r,text="+",command=lambda :additem("VANILLA")).place(x=700,y=130)
    w00 = Label(r,text=h[0],padx=4,pady=4).place(x=720,y=130)
    b1 = Button(r,text="-",command=lambda :removeitem("VANILLA")).place(x=740,y=130)
    w1=Label(r,text='2.STRAWBERRY\t\t\t\t\t50',pady=15,padx=15,bg='SeaGreen4',anchor=W).place(x=290,y=160)
    b2 = Button(r,text="+",command=lambda :additem("STRAWBERRY")).place(x=700,y=170)
    w01 = Label(r,text=h[1],padx=4,pady=4).place(x=720,y=170)
    b3 = Button(r,text="-",command=lambda :removeitem("STRAWBERRY")).place(x=740,y=170)
    w1=Label(r,text='3.BUTTER-SCOTCH\t\t\t\t50',pady=15,padx=15,bg='SeaGreen4',anchor=W).place(x=290,y=200)
    b2 = Button(r,text="+",command=lambda :additem("BUTTER-SCOTCH")).place(x=700,y=210)
    w02 = Label(r,text=h[2],padx=4,pady=4).place(x=720,y=210)
    b3 = Button(r,text="-",command=lambda :removeitem("BUTTER-SCOTCH")).place(x=740,y=210)
    w1=Label(r,text='4.MIXED-FRUIT\t\t\t\t\t70',pady=15,padx=15,bg='SeaGreen4',anchor=W).place(x=290,y=240)
    b2 = Button(r,text="+",command=lambda :additem("MIXED-FRUIT")).place(x=700,y=250)
    w03 = Label(r,text=h[3],padx=4,pady=4).place(x=720,y=250)
    b3 = Button(r,text="-",command=lambda :removeitem("MIXED-FRUIT")).place(x=740,y=250)
    w1=Label(r,text='5.CHOCOLATE\t\t\t\t\t75',pady=15,padx=15,bg='SeaGreen4',anchor=W).place(x=290,y=280)
    b2 = Button(r,text="+",command=lambda :additem("CHOCOLATE")).place(x=700,y=290)
    w04 = Label(r,text=h[4],padx=4,pady=4).place(x=720,y=290)
    b3 = Button(r,text="-",command=lambda :removeitem("CHOCOLATE")).place(x=740,y=290)
    g5=Button(r,text='CART',width=15,bg='SeaGreen4',command=cart).place(x=100,y=430)
    g6=Button(r,text='MENU',width=15,bg='SeaGreen4',command=menu).place(x=300,y=430)
    g66=Button(r,text='BACK',width=15,bg='SeaGreen4',command=r.destroy).place(x=500,y=430)
    g46=Button(r,text='BILL',width=15,bg='SeaGreen4',command=bill).place(x=700,y=430)
    r.mainloop()
name=['WELCOME']
c=[0,0,0,0,0]
e=[0,0,0,0]
a=[0,0,0,0]
l=[0,0,0,0]
g=[0,0,0]
h=[0,0,0,0,0]
f=[0,0,0,0]
d=[0,0,0,0,0,0,0]
lis=[]
t=" "
table="FIR2"
result1={"VANILLA":50,"STRAWBERRY":50,"BUTTER-SCOTCH":50,"MIXED-FRUIT":70,"CHOCOLATE":75,"COKE":35,"THUMBS-UP":35,"MAAZA":35,"FROOTI":35,"MOUNTAIN-DEW":35,"MIRINDA":35,"SPRITE":35,"ALOO-65":190,"VEG-MANCHURIA":100,"VEG-65":100,"GOBI-65":100,"GOBI-MANCHURIA":100,"VEG-MANCHO-SOUP":180,"VEG-CORN-SOUP":160,"VEG-MUSHROOM-SOUP":160,"SWEET-CORN-SOUP":160,"ALOO-BIRYANI":220,"VEG-BIRYANI":200,"PANEER-BIRYANI":160,"VEG-FRIED-RICE":100,"CHICK-65":150,"NON-MANCHURIA":200,"NON-65":150,"CHILLI-MANCHURIA":200,"NON-MANCHO-SOUP":300,"CHICKEN-SOUP":250,"NON-BONE-SOUP":350,"CHILLI-BONE-SOUP":150,"CHICK-BIRYANI":250,"MASALA-BIRYANI":200,"MUTTON-BIRYANI":350}
root=Tk()
fr=Frame(root,bg='yellow')
fr.pack(side=TOP)
root.geometry("950x550+300+0")
root.configure(background='YELLOW')
root.title('SMART RESTAURANT')
Label(fr,text=" ",bg='yellow',padx=20,pady=15).grid(row=3,column=1)
Label(fr,text='First Name',bg='yellow',padx=20,pady=15,font=("Times", 15, "bold italic")).grid(row=4,column=1)
e1 = Entry(fr,width=25)
e1.grid(row=4,column=2)
Label(fr,text='Last Name',bg='yellow',padx=20,pady=15,font=("Times", 15, "bold italic")).grid(row=5,column=1)
e2 = Entry(fr,width=25)
e2.grid(row=5,column=2)
Label(fr,text=" ",bg='yellow',pady=20).grid(row=0,column=2)
w=Label(fr,font=('helvetica',25,'bold'),text='WELCOME',bg='YELLOW')
w.grid(row=1,column=2)
Label(fr,text=" ",bg='yellow',padx=20,pady=15).grid(row=6,column=1)
Button(fr,text='SUBMIT',command=menu).grid(row=7,column=2)
root.mainloop()
