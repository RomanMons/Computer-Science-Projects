from tkinter import *

root = Tk()
canvas = Canvas(root,width=500,height = 500)
rectangle = [0, 0, 0, 0]

def press_handler(event):
    xpress = event.x
    ypress = event.y
    rectangle[:] = [xpress, ypress, 0, 0]


def release_handler(event):
    xrelease = event.x
    yrelease = event.y
    rectangle[2] = xrelease
    rectangle[3] = yrelease
    canvas.delete('all')
    canvas.create_rectangle(rectangle, fill = 'lime')


if __name__ == "__main__":
    canvas.pack()
    canvas.bind('<Button-1>', press_handler)
    canvas.bind('<ButtonRelease-1>', release_handler)
    root.resizable(width=False, height=False)
    root.mainloop()
