from tkinter import *

from matplotlib import pyplot as plt
from ttkbootstrap import *
from tkinter import filedialog, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import calendar
import os
import datetime

flag = False
filePath = 'user.txt'
if os.path.exists(filePath):
    flag = True
print(flag)

allEvents = []
if flag:
    try:
        with open('events.tnx', 'r') as file:
            lines = file.readlines()
            loaded_data = []
            for line in lines:
                item = line.strip().split(',')
                loaded_data.append((item[0], item[1]))
        print("Data loaded from the file:")
        print(loaded_data)
        allEvents = loaded_data
    except FileNotFoundError:
        print("The file does not exist.")
stateList = []
done = 0
total = 1
filepath = ''
print(time.strftime('%D'))

def showDate():
    date = ttk.LabelFrame(root, text='Date', bootstyle=WARNING, width=150)
    e41 = ttk.Label(date, text=str(time.strftime('%d-%m-%y')), font=['Time', 10, 'bold'], bootstyle=LIGHT)
    e42 = ttk.Label(date, text=str(time.strftime('%H : %M')), font=['Time', 25, 'bold'], bootstyle=LIGHT)
    date.place(x=824, y=72, width=153, height=116)
    e42.pack(padx=10, pady=5)
    e41.pack(padx=10, pady=5)

def schedule_function():
    showDate()  # Call the function
    root.after(5000, schedule_function)

def updateMeter():
    cnt = 0
    for i in todoLabelFrame.winfo_children():
        print(i.state())
        if i.state() == ('selected',):
            cnt += 1
            print(('yvgbh'))
    global done
    global total
    done = cnt
    total = len(todoLabelFrame.winfo_children())
    print(done, total)
    homePage()


def homePage():
    # image
    # image = Image.open(filepath)
    # image = image.resize((102, 102), Image.LANCZOS)
    # # Create a circular mask image
    # mask = Image.new("L", image.size, 0)
    # draw = ImageDraw.Draw(mask)
    # draw.ellipse((0, 0, image.width, image.height), fill=255)
    # # Apply the mask to the image
    # rounded_image = Image.new("RGBA", image.size, '#332D2D')
    # rounded_image.paste(image, (0, 0), mask=mask)
    # # Create an ImageTk object from the rounded image
    # image_tk = ImageTk.PhotoImage(rounded_image)
    # # Create a Label widget to display the rounded image
    # image_label = Label(left, image=image_tk)
    # image_label.pack(pady=50)

    # today
    today = []
    for i in allEvents:
        if i[0] == time.strftime('%D'): today.append(i[1])
    eventList = ttk.LabelFrame(root, text='Today (' + str(len(today)) + ')', bootstyle=WARNING)
    e1 = []
    for i in today:
        l1 = ttk.Label(eventList, text=i, bootstyle=(INVERSE, INFO), width=15, font=['', 10, 'normal'])
        e1.append(l1)

    # upcoming
    upcoming = []
    for i in allEvents:
        if i[0] > time.strftime('%D'): upcoming.append(i[1])
    eventList2 = ttk.LabelFrame(root, text='Upcoming', bootstyle=WARNING, width=150)
    e2 = []
    for i in upcoming:
        l2 = ttk.Label(eventList2, text=i, bootstyle=(INVERSE, SECONDARY), width=15, font=['', 10, 'normal'])
        e2.append(l2)

    # motivation
    motiv = ttk.LabelFrame(root, text='Motivation', bootstyle=(SUCCESS))
    e31 = ttk.Label(motiv, text='You Deserve\nEverything', bootstyle=LIGHT, font=['Time', 12, 'bold'])

    # date
    showDate()

    # progress
    progressBox = ttk.LabelFrame(root, text='Meter', bootstyle=LIGHT)
    m1 = Meter(progressBox, amountused=int((done / total) * 100), amounttotal=100, meterthickness=7, textright='%',
               subtext='progress', textfont=['Times', 10, 'bold'], subtextfont=['Times', 8, 'normal'],
               metersize=100, bootstyle=WARNING, arcoffset=90)

    # barchart
    for it in barChart.winfo_children(): it.destroy()
    xLabels = []
    yLabels = []
    for i in range(7):
        xLabels.append((datetime.date.today() + datetime.timedelta(days=i)).strftime('%D'))
        tCount = 0
        for j in allEvents:
            if j[0] == xLabels[len(xLabels)-1]:
                tCount += 1
        yLabels.append(tCount)
        t = xLabels[i]
        xLabels[i] = t[3:5]
    print(xLabels)
    print(yLabels)

    fig = Figure(figsize=(5, 3), dpi=100)
    fig.set_facecolor('#424242')
    ax = fig.add_subplot(111)

    # Plot the bar graph
    ax.bar(xLabels, yLabels)

    # Create a FigureCanvasTkAgg object to display the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=barChart)
    canvas.draw()
    canvas.get_tk_widget().pack()
    barChart.place(x=242, y=219, width=542, height=322)

    clndr.place(x=282, y=5557, width=652, height=442)
    task.place(x=282, y=5557)
    if flag:
        info = []
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                info.append(line.strip())
        print(info)
        nameLvl.configure(text=info[0])
        mailLvl.configure(text=info[1])
    else:
        nameLvl.configure(text=str(name.get()))  ###
        mailLvl.configure(text=str(mail.get()))  ###
        try:
            with open('user.txt', 'w') as file:
                file.write(str(name.get()) + "\n")
                file.write(str(mail.get()) + "\n")
            print("Lines written to the file.")
        except IOError:
            print("Error writing to the file.")
    left.place(x=0, y=0, width=206, height=575)
    nameLvl.pack(pady=(70,10))
    mailLvl.pack(pady=10)
    home.pack(padx=15, pady=15)
    calendarButton.pack(padx=15, pady=15)
    taskButton.pack(padx=15, pady=15)
    event.pack(padx=15, pady=15)
    todo.pack(padx=15, pady=15)
    logOutButton.place(x=65, y=508, width=120, height=33)
    deleteButton.place(x=21, y=508, width=40, height=33)

    eventList.place(x=242, y=72, width=150, height=116)
    for i in e1:
        i.pack(padx=10, pady=3)
        print(44)
    eventList2.place(x=436, y=72, width=150, height=116)
    for i in e2: i.pack(padx=10, pady=3)
    motiv.place(x=630, y=72, width=150, height=116)
    e31.pack(pady=10)

    todoFrame.place(x=824, y=72, width=153, height=116)
    allEventsFrame.place(x=824, y=720, width=153, height=116)
    progressBox.place(x=824, y=222, width=153, height=319)
    m1.pack()
    landFrame.pack(pady=2000)


def todoPage():
    task.place(x=282, y=5557, width=652, height=442)
    clndr.place(x=282, y=720, width=652, height=442)
    name.pack(pady=2000)
    allEventsFrame.place(x=824, y=720, width=153, height=116)
    barChart.place(x=242, y=999, width=542, height=322)

    for i in todoLabelFrame.winfo_children(): i.destroy()

    eventState = [(x[1], 0) for x in allEvents if x[0] == time.strftime('%D')]
    stateList.clear()
    for i in eventState:
        var = tk.BooleanVar(value=False)
        xx = Checkbutton(todoLabelFrame, text=i[0], width=542, bootstyle=DANGER, variable=var)
        xx.pack(padx=20, pady=3)
        stateList.append(xx)
    todoFrame.place(x=242, y=219, width=550, height=400)
    todoLabelFrame.pack()
    updateButton.pack()


def calendarPage():
    task.place(x=282, y=5557)
    clndr.place(x=242, y=219, width=542, height=332)
    allEventsFrame.place(x=824, y=720, width=153, height=116)
    barChart.place(x=242, y=999, width=542, height=322)

    v1.set(int(time.strftime('%m')))
    v2.set(int(time.strftime('%Y')))
    rr()
    name.pack(pady=2000)
    todoFrame.place(x=824, y=72, width=153, height=116)


def showEvents():
    task.place(x=282, y=5557, width=652, height=442)
    clndr.place(x=282, y=720, width=652, height=442)
    todoFrame.place(x=824, y=720, width=153, height=116)
    barChart.place(x=242, y=999, width=542, height=322)
    name.pack(pady=2000)

    for i in allEventsFrame.winfo_children(): i.destroy()
    allEventsFrame.place(x=242, y=219, width=550, height=550)
    for i in allEvents:
        if i[0] >= time.strftime('%D'):
            Label(allEventsFrame, text=str(i[0] + ' : ' + i[1]), bootstyle=(INVERSE, DARK), width=50,font=('Arial', 12, 'normal')).pack(pady=5, padx=10)


def addEvent():
    clndr.place(x=282, y=720, width=652, height=442)
    name.pack(pady=2000)
    todoFrame.place(x=824, y=72, width=153, height=116)
    allEventsFrame.place(x=824, y=720, width=153, height=116)
    barChart.place(x=242, y=999, width=542, height=322)

    task.place(x=282, y=250)
    eventDate.pack(padx=20, pady=5)
    eventDescription.pack(padx=20, pady=5)
    addBtn.pack(padx=20, pady=5)


def rr():
    cal = calendar.month(int(s2.get()), int(s1.get()))
    l1.configure(text=cal)
    l1.pack(padx=20)
    s1.pack(side='left', padx=20)
    s2.pack(side='right', padx=20)


def addingTask():
    s1 = eventDescription.get()
    d1 = str(eventDate.entry.get())
    allEvents.append((d1, s1))
    allEvents.sort()
    homePage()


def upload():
    types = [('jpg', '*.jpg'), ('jpg', '*.png')]
    global filepath
    filepath = tk.filedialog.askopenfilename()
    print(filepath)


def saveEvents():
    try:
        with open('events.tnx', 'w') as f:
            for i in allEvents:
                f.write(f"{i[0]},{i[1]}\n")
        print("Data written to the file.")
    except IOError:
        print("Error writing to the file.")
    root.destroy()


def deleteUser():
    result = messagebox.askyesno("Confirmation", "Are you sure you want to delete the User?")
    if result == True:
        os.remove('user.txt')
        os.remove('events.tnx')
        root.destroy()
    else:
        # User clicked 'No' or closed the window
        # Do nothing or handle accordingly
        pass


def on_close():
    pass

root = Window(themename='darkly')
root.geometry('1010x575')
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)
schedule_function()

################################################  HOME  ######################################################################
# left
left = ttk.Frame(root, bootstyle=DARK)
nameLvl = ttk.Label(left, text='Demo name', font=['Time', 10, 'bold'])
mailLvl = ttk.Label(left, text='demo123@gmial.com', font=['Time', 8, 'normal'])
home = ttk.Button(left, text='🏠   Home', bootstyle=(SUCCESS), width=22, command=homePage)
calendarButton = ttk.Button(left, text='📆 Calender', bootstyle=(SUCCESS), width=22, command=calendarPage)
taskButton = ttk.Button(left, text='✔ All Events', bootstyle=(SUCCESS), width=22, command=showEvents)
event = ttk.Button(left, text='🎬 Add Event', bootstyle=(SUCCESS), width=22, command=addEvent)
todo = ttk.Button(left, text='📃 To Do', bootstyle=(SUCCESS), width=22, command=todoPage)
logOutButton = Button(left, text='📤 Close', bootstyle=(WARNING, OUTLINE), command=saveEvents)
deleteButton = Button(left, text='❌', bootstyle=(DANGER), command=deleteUser, padding=0)
barChart = LabelFrame(root, text='Week Summary',  bootstyle=INFO)


################################################  Calendar  ######################################################################
clndr = ttk.Frame(root, bootstyle=DARK)
v1 = IntVar(clndr)
s1 = Spinbox(clndr, values=[x for x in range(1, 13)], width=5, command=rr, textvariable=v1, bootstyle=INFO)
v2 = IntVar(clndr)
s2 = Spinbox(clndr, values=[x for x in range(1990, 2099)], width=5, command=rr, textvariable=v2, bootstyle=INFO)
l1 = Label(clndr, text='', bootstyle=(DARK, INVERSE), font=['Arial', 15, 'bold'])

################################################  show all events  ######################################################################
allEventsFrame = Frame(root)
# todoLabelFrame = LabelFrame(allEventsFrame, text='Today\'s tasks', bootstyle=LIGHT, width=20, height=322)

################################################  Add task  ######################################################################
task = Frame(root)
eventDate = DateEntry(task, bootstyle=INFO, dateformat='%m/%d/%y')
eventDescription = Entry(task, bootstyle=INFO, width=25)
addBtn = Button(task, bootstyle=(OUTLINE, SUCCESS), text='Add Event', command=addingTask)

################################################  To Do List  ######################################################################
todoFrame = Frame(root)
todoLabelFrame = LabelFrame(todoFrame, text='Today\'s tasks', bootstyle=LIGHT, width=20, height=322)
updateButton = Button(todoFrame, text='Update', bootstyle=(OUTLINE, SUCCESS), width=20, command=updateMeter)

########################################### landing page  ############################################
# photo = Button(root, text='Add Image', command=upload)
# #photo.pack()
landFrame = Frame(root, width=1010, height=575)
landFrame.pack()
nl = Label(landFrame, text='Name', font=('Arial', 10, 'normal'))
ml = Label(landFrame, text='Email', font=('Arial', 10, 'normal'))
nvar = StringVar
name = Entry(landFrame, textvariable=nvar, width=45)
nvar2 = StringVar
mail = Entry(landFrame, textvariable=nvar2, width=45)
create = Button(landFrame, text='Create User', command=homePage)

if flag:
    homePage()
else:
    nl.place(x=288, y=119)
    name.place(x=282, y=155)
    ml.place(x=288, y=234)
    mail.place(x=282, y=270)
    create.place(x=411, y=385)

root.mainloop()
