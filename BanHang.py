from tkinter import *

a=0
b=0
c=0
d=0
e=0
cc =0

def oktrasua():
    global a
    if var1.get() == 1:
        enttrasua.config(state =NORMAL)
        a=1
    if var1.get() == 0:
        enttrasua.delete(0,END)
        enttrasua.config(state =DISABLED)
        a=0

def oktradao():
    global b
    if var2.get() == 1:
        enttradao.config(state =NORMAL)
        b=1
    if var2.get() == 0:
        enttradao.delete(0,END)
        enttradao.config(state =DISABLED)
        b=0

def okcafe():
    global c
    if var3.get() == 1:
        entcafe.config(state =NORMAL)
        c=1
    if var3.get() == 0:
        entcafe.delete(0,END)
        entcafe.config(state = DISABLED)
        c=0

def oklatte():
    global d
    if var4.get() == 1:
        entlatte.config(state =NORMAL)
        d=1
    if var4.get() == 0:
        entlatte.delete(0,END)
        entlatte.config(state = DISABLED)
        d=0

def okwater():
    global e
    if var5.get() == 1:
        entwater.config(state = NORMAL)
        e=1
    if var5.get() == 0:
        entwater.delete(0,END)
        entwater.config(state = DISABLED)
        e=0

def okcoca():
    global cc
    if var6.get() == 1:
        entcoca.config(state =NORMAL)
        cc=1
    if var6.get() == 0:
        entcoca
        entcoca.delete(0,END)
        entcoca.config(state = DISABLED)
        cc=0

def thanhtoan():
    global tiendon,receipt,tien, total

    f=open("hoadon.txt", "w+", encoding = 'utf-8')
    f.write("Hóa đơn")
    f.write("\n")
    f.write("\n")
    f.write('Sản phẩm \t \t Giá \t \tSL \t Tổng tiền')
    
    tiendon = 0
    tien = 0
    receipt.config(state = 'normal')
    receipt.delete("1.0", "end")
    
    receipt.config(font = ('Arial', 11, 'bold'))
    receipt.insert(END, 'Sản phẩm \t \t Giá \t \tSL \t Tổng tiền')
    if a == 1:
        sla = int(enttrasua.get())
        tiendon = int(tiendon)
        tiendon = 30000*sla
        tiendon = str(tiendon)
        tien = tien + 30000*sla
        receipt.insert(END, '\nTrà sữa \t \t 30 000 \t \t' + enttrasua.get() + ' \t '+ tiendon)
        f.write('\nTrà sữa \t \t 30 000 \t' + enttrasua.get() + ' \t '+ tiendon)
    if b == 1:
        tiendon = int(tiendon)
        slb = int(enttradao.get())
        tien = tien + 30000*slb
        tiendon = 30000*slb
        tiendon = str(tiendon)
        receipt.insert(END, '\nTrà đào \t \t 30 000 \t \t' + enttradao.get() + ' \t '+ tiendon)
        f.write('\nTrà đào \t \t 30 000 \t' + enttradao.get() + ' \t '+ tiendon)
    if c == 1:
        tiendon = int(tiendon)
        slc = int(entcafe.get())
        tien = tien + 35000*slc
        tiendon = 35000*slc
        tiendon = str(tiendon)
        receipt.insert(END, '\nCà phê \t \t 35 000 \t \t' + entcafe.get() + ' \t '+ tiendon)
        f.write('\nCà phê  \t \t 35 000 \t ' + entcafe.get() + ' \t '+ tiendon)
    if d == 1:
        tiendon = int(tiendon)
        sld = int(entlatte.get())
        tiendon = 40000*sld
        tien = tien + 40000*sld
        tiendon = str(tiendon)
        receipt.insert(END, '\nLatte \t \t 40 000 \t \t' + entlatte.get() + ' \t '+ tiendon)
        f.write('\nLatte  \t \t \t 40 000  \t' + entlatte.get() + ' \t '+ tiendon)
    if e == 1:
        tiendon = int(tiendon)
        sle = int(entwater.get())
        tiendon = 15000*sle
        tien = tien + 15000*sle
        tiendon = str(tiendon)
        receipt.insert(END, '\nNước lọc \t \t 40 000 \t \t' + entwater.get() + ' \t '+ tiendon)
        f.write('\nNước lọc  \t \t 40 000  \t' + entwater.get() + ' \t '+ tiendon)
    if cc == 1:
        tiendon = int(tiendon)
        slf = int(entcoca.get())
        tien = tien + 20000*slf
        tiendon = 20000*slf
        tiendon = str(tiendon)
        receipt.insert(END, '\nCoca Cola \t \t 20 000 \t \t' + entcoca.get() + ' \t '+ tiendon)
        f.write('\nCoca Cola \t \t 20 000  \t' + entcoca.get() + ' \t '+ tiendon)
    receipt.insert(END, '\nTổng \t \t \t \t \t '+str(tien)+ ' đồng')
    f.write('\nTổng \t \t \t \t \t \t '+str(tien)+ ' đồng')
    receipt.config(state='disabled')
    totalstr = "Tổng tiền: " + str(tien) + " đồng"
    total.config(text = totalstr)
    f.close

screen = Tk()
screen.geometry("1000x650")
screen.title("Người bán")

money = Tk()
money.geometry("450x100")
money.title("Người mua")

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)

#Checkbox
cbtrasua = Checkbutton(screen)
cbtrasua.place(x=25, y = 150)
cbtrasua.config(text = "Trà sữa", font = ("ArialBold",25),variable=var1, command = oktrasua)

cbtradao = Checkbutton(screen)
cbtradao.place(x=25, y = 200)
cbtradao.config(text = "Trà đào", font = ("ArialBold",25),variable=var2, command = oktradao)

cbcafe = Checkbutton(screen)
cbcafe.place(x=25,y=250)
cbcafe.config(text = "Cà phê", font=("Arialbold",25),variable=var3, command = okcafe)

cblatte= Checkbutton(screen)
cblatte.place(x=25,y=300)
cblatte.config(text = "Latte", font=("Arialbold",25),variable=var4, command = oklatte)

cbwater= Checkbutton(screen)
cbwater.place(x=25,y=350)
cbwater.config(text = "Nước lọc", font=("Arialbold",25),variable=var5, command = okwater)

cbcoca= Checkbutton(screen)
cbcoca.place(x=25,y=400)
cbcoca.config(text = "Coca Cola", font=("Arialbold",25),variable=var6, command = okcoca)

#Entry
enttrasua = Entry(screen)
enttrasua.place(x=250, y = 150)
enttrasua.config(font=("Arial", 23), width = 5, state=DISABLED)

enttradao = Entry(screen)
enttradao.place(x=250, y = 200)
enttradao.config(font=("Arial", 23), width = 5, state=DISABLED)

entcafe = Entry(screen)
entcafe.place(x=250, y = 250)
entcafe.config(font=("Arial", 23), width = 5, state=DISABLED)

entlatte = Entry(screen)
entlatte.place(x=250, y = 300)
entlatte.config(font=("Arial", 23), width = 5, state=DISABLED)

entwater = Entry(screen)
entwater.place(x=250, y = 350)
entwater.config(font=("Arial", 23), width = 5, state=DISABLED)

entcoca = Entry(screen)
entcoca.place(x=250, y = 400)
entcoca.config(font=("Arial", 23), width = 5, state=DISABLED)

done = Button(screen)
done.config(text = "Thanh toán", font=("Arial",25), command = thanhtoan)
done.place(x=100, y = 500)

receipt = Text(screen)
receipt.config(width = 60, state='disabled', bg='white', fg='black', font = ('Arial', 11))
receipt.place(x=400, y=150)

name = Label(screen)
name.config(text = "Phần mềm bán hàng", font = ("", 45))
name.place(x=125, y = 50)

total = Label(money)
total.config(text = "Tổng tiền: 0 đồng", font = ("", 25))
total.place(x=10, y = 10)

screen.mainloop()
