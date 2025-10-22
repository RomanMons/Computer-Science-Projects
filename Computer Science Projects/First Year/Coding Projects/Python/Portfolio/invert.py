from tkinter import *

root = Tk()
canvas = Canvas(root,width=500,height = 500)
og_points = [150, 0, 350, 0, 250, 500]
points = og_points.copy()
def invert_triangle(event):
    global points
    if points == og_points:
        points[1] = og_points[5]
        points[3] = og_points[5]
        points[5] = og_points[1]
    else:
        points = og_points.copy()
    canvas.delete("all")
    canvas.create_polygon(points, fill='magenta')
if __name__ == "__main__":
    canvas.pack(side = 'bottom')
    canvas.create_polygon(points,fill = 'magenta')
    button = Button(root,text = 'Invert')
    button.pack(fill = X)
    button.bind('<Button-1>',invert_triangle)
    root.resizable(width=False, height=False)
    root.mainloop()
