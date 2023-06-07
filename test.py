import time
import calendar
from ttkbootstrap import *

cal = calendar.month(2008,5)
print(type(cal))

root = Window()

t1 = Label(root)
t1.configure(text=cal)
t1.pack(anchor='ne')

root.mainloop()