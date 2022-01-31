# Import Required Library
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
# Create Object
root = Tk()
# Set geometry
root.geometry("280x455")
root.wm_iconbitmap("Computer_icon.ico")
root.minsize(220,400)
root.maxsize(300,470)
root.title("Change Mouse Cursor")

# List of cursors
cursors =[
		"Arrow","Circle","Cross","Dotbox","Exchange","Fleur","Heart",
		"Mouse","Plus","Sizing","Spider","Spraycan","Star","Target","Tcross"
]
# Add image file
bg = PhotoImage(file="Bg_Color1.png")
# Create Canvas
canvas1 = Canvas(root, width=400,height=400)
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,anchor="nw")

style = Style()
style.configure('TButton', font =('calibri', 12, 'bold'),borderwidth = '3')
style.map('TButton', foreground = [('active', '!disabled', 'red')],background = [('active', 'black')])

# Iterate through all cursors
for cursor in cursors:
	button1= Button(canvas1,text=cursor,cursor=cursor).pack()
# Execute Tkinter
root.mainloop()
