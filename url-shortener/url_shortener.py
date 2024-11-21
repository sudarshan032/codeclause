# Import the libraries
from tkinter import *
import pyshorteners

# Create the main
root = Tk()
root.title("Simple URL Shortener App")
width = 400
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)
root.config(bg="white")


# Function for URL shortening
def urlshortend():
    s = pyshorteners.Shortener().tinyurl.short(URL.get())
    RESULT.set(s)
    URL.set("")


# Variables and frames for GUI elements
URL = StringVar()
RESULT = StringVar()

Top = Frame(root, width=400, bd=1, relief=SOLID)
Top.pack(side=TOP)

BottomTitle = Frame(root, width=400, bd=1, relief=SOLID)
BottomTitle.pack(side=TOP, pady=10)

BottomForm = Frame(root, width=400, bg="white")
BottomForm.pack(side=TOP)

# GUI elements - labels, entry fields, and button
lbl_title = Label(Top, text=" URL SHORTENER APP", width=400, font=('arial', 18))
lbl_title.pack(fill=X)

lbl1 = Label(BottomForm, text="Enter your URL", font=('arial', 12))
lbl1.grid(row=0, columnspan=5, column=0)

myurl = Entry(BottomForm, textvariable=URL, width=50)
myurl.grid(row=1, column=1)

result_txt = Entry(BottomForm, textvariable=RESULT, font=('arial', 10), width=50, bd=0)
result_txt.grid(row=4, columnspan=5, column=0)

btn = Button(BottomForm, text="Shorten", width=20, fg="black", bg="white", command=urlshortend)
btn.grid(row=2, columnspan=5, column=0, pady=10)

# Start the main event loop
if __name__ == '__main__':
    root.mainloop()
