import Tkinter
import datetime
import time

todolistmessage =[]
todolistdatestr = []
todolistdate =[]



popup = Tkinter.Tk()
popup.geometry("370x500")



def leavemini():
    popup.destroy()


        
def seereminder():
    
    def addmessage():
        
        def sendover():
            if(secondentry.get() == "" and newentry.get() == ""):
                warnmessage = Tkinter.Message(newpopup, width = 150, text="Both fields are blank")
                warnmessage.grid(row= 5)
            
            elif(secondentry.get() == ""):
                warnmessage = Tkinter.Message(newpopup, width = 150, text="Input the date/time")
                warnmessage.grid(row =5)
                
            

            elif(newentry.get() == ""):
                warnmessage = Tkinter.Message(newpopup, width = 150, text ="Input the reminder")
                warnmessage.grid(row = 5)
            else:
                
                mylistbox.insert(0,newentry.get())
                my2ndlistbox.insert(0,secondentry.get())
                todolistmessage.append(newentry.get())
                todolistdatestr.append(secondentry.get())
                newentry.delete(0,'end')
                secondentry.delete(0,'end')
                message = Tkinter.Message(newpopup, width = 150, text ="Added Successfully")
                message.grid(row=5)
                
                
           
        
        def leaveaddmessage():
            newpopup.destroy()

        
        
        
        newpopup = Tkinter.Tk()
        newpopup.geometry("370x500")
        newpopup.wm_title("To-Do List GUI")
        newlabel = Tkinter.Label(newpopup, text="Input your reminder", font="Verdana")
        newlabel.grid(row = 0)
        
        newentry = Tkinter.Entry(newpopup, width = 18)
        newentry.grid(row = 0, column = 1)
        
        secondlabel = Tkinter.Label(newpopup, text="Input the date and time\n'Note: format => April 9, 2018'", font="Verdana")
        secondlabel.grid(row =1)
        
        secondentry = Tkinter.Entry(newpopup, width = 18)
        secondentry.grid(row = 1, column = 1)
        Add = Tkinter.Button(newpopup, text="Add",command = sendover)
        Add.grid(row = 2, column = 1,pady=5)
        
        Close = Tkinter.Button(newpopup, text="Close",command = leaveaddmessage)
        Close.grid(row = 3, column = 1,pady=5)
        
    def getrid():
        mylistbox.delete(0)
        my2ndlistbox.delete(0)
        message = Tkinter.Message(spopup, width =150, text="Deleted Successfully")
        message.grid(row=2,column=2)
        
    def leaveaddmessage():
        spopup.destroy()
        
    def clear():
        mylistbox.delete(0,'end')
        my2ndlistbox.delete(0,'end')
        
    spopup = Tkinter.Tk()
    spopup.geometry("370x500")
    spopup.wm_title("To-Do List GUI")
    sleftlabel = Tkinter.Label(spopup, text="Reminder(s)", font="Verdana")
    sleftlabel.grid(row = 0, column = 0)
    mylistbox = Tkinter.Listbox(spopup)
    mylistbox.grid(row = 0, column = 1)
    

    srightlabel = Tkinter.Label(spopup, text="Date(s)", font="Verdana")
    srightlabel.grid(row = 1, column = 0)
    my2ndlistbox = Tkinter.Listbox(spopup)
    my2ndlistbox.grid(row = 1, column = 1)
    for i in todolistmessage:
        mylistbox.insert(0,i)
    for i in todolistdatestr:
        my2ndlistbox.insert(0,i)
   
    Add = Tkinter.Button(spopup, text="Add",command = addmessage)
    Add.grid(row= 2, column = 1,pady=5)
    Del = Tkinter.Button(spopup, text="Delete",command = getrid)
    Del.grid(row = 3, column =1,pady=5)
    Clear = Tkinter.Button(spopup, text="Clear",command = clear)
    Clear.grid(row =4, column = 1,pady=5)
    B = Tkinter.Button(spopup, text="Done", command = leaveaddmessage)
    B.grid(row = 5, column =1,pady=5)
    
    
    
popup.wm_title("To-Do List GUI")
label = Tkinter.Label(popup, text="To-Do List", font="Verdana")
label.pack(pady=15)
B2 = Tkinter.Button(popup, text="Show reminders", command = seereminder)
B2.pack(pady=5)
B = Tkinter.Button(popup,text="close",command=leavemini)
B.pack(pady=5)
popup.mainloop()
