from tkinter import *

root =Tk()
root.title("nadu coding")

chkvar=IntVar()
chkbox=Checkbutton(root,text="오늘하루보지않기", variable=chkvar)
chkbox.pack()

chkvar2=IntVar()
chkbox2=Checkbutton(root,text="일주일동안 보지않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())  
btn=Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()

