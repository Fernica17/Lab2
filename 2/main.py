from tkinter import *

r = 40


def left_click(event):
    x = event.x
    y = event.y
    check = False
    for oval in ovals:
        coord = canvas.coords(oval)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        if x0 - 1 * r < x < x1 + 1 * r and y0 - 1 * r < y < y1 + 1 * r:
            check = True
            break
    if not check:
        ovals.append(canvas.create_oval(x - r, y - r, x + r, y + r, fill="white",width=1.5))
        labels_ovals.append(canvas.create_text((x, y), text=f"{key.get()} \n {value.get()}"))


before_x = -1
before_y = -1


def middle_click(event):
    x = event.x
    y = event.y
    global before_x
    global before_y
    for oval in ovals:
        coord = canvas.coords(oval)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        if x0 < x < x1 and y0 < y < y1:
            if before_x == -1:
                before_x = x0 + r
                before_y = y0 + r
            else:
                found = False
                for line in lines:
                    coord_l = canvas.coords(line)
                    x0_l = coord_l[0]
                    y0_l = coord_l[1]
                    x1_l = coord_l[2]
                    y1_l = coord_l[3]
                    if (x0_l == before_x and y0_l == before_y and x1_l == x0 + r and y1_l == y0 + r) or (
                            x1_l == before_x and y1_l == before_y and x0_l == x0 + r and y0_l == y0 + r):
                        found = True
                        break
                if not found and (before_x != x0 + r and before_y != y0 + r):
                    obj = canvas.create_line(x0 + r, y0 + r, before_x, before_y, width=1.2)
                    labels_lines.append(
                        canvas.create_text((x0 + r + before_x) / 2 + 14, (y0 + r + before_y) / 2 + 14,
                                           text=f"{key.get()} \n {value.get()}"))
                    canvas.lower(obj)
                    lines.append(obj)
                before_x = -1
                before_y = -1


def right_click(event):
    x = event.x
    y = event.y
    for oval in ovals:
        coord = canvas.coords(oval)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        if x0 < x < x1 and y0 < y < y1:
            canvas.delete(labels_ovals[ovals.index(oval)])
            labels_ovals.remove(labels_ovals[ovals.index(oval)])
            canvas.delete(oval)
            ovals.remove(oval)
            if len(lines) != 0:
                line = lines[0]
                coord = 0
                while coord != len(lines) and len(lines) != 0:
                    coord_l = canvas.coords(line)
                    x0_l = coord_l[0]
                    y0_l = coord_l[1]
                    x1_l = coord_l[2]
                    y1_l = coord_l[3]
                    if (x0 < x0_l < x1 and y0 < y0_l < y1) or (x0 < x1_l < x1 and y0 < y1_l < y1):
                        canvas.delete(labels_lines[lines.index(line)])
                        labels_lines.remove(labels_lines[lines.index(line)])
                        canvas.delete(line)
                        lines.remove(line)
                        if coord != 0:
                            coord = coord - 1
                    else:
                        coord = coord + 1
                    if len(lines) < 0:
                        break
                    if coord != len(lines):
                        line = lines[coord]

    for line in lines:
        coord = canvas.coords(line)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        m = (y1 - y0) / (x1 - x0)
        if m * (x - x1) - 10 < y - y1 < m * (x - x1) + 10 and min(x0, x1) < x < max(x0, x1) and min(y0, y1) < y < max(
                y0, y1):
            canvas.delete(labels_lines[lines.index(line)])
            labels_lines.remove(labels_lines[lines.index(line)])
            canvas.delete(line)
            lines.remove(line)


def double_left_click(event):
    x = event.x
    y = event.y
    for oval in ovals:
        coord = canvas.coords(oval)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        if x0 < x < x1 and y0 < y < y1:
            canvas.itemconfig(labels_ovals[ovals.index(oval)], text=f"{key.get()} \n {value.get()}")

    for line in lines:
        coord = canvas.coords(line)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        m = (y1 - y0) / (x1 - x0)
        if m * (x - x1) - 10 < y - y1 < m * (x - x1) + 10 and min(x0, x1) < x < max(x0, x1) and min(y0, y1) < y < max(
                y0, y1):
            canvas.itemconfig(labels_lines[lines.index(line)], text=f"{key.get()} \n {value.get()}")


def left_motion(event):
    x = event.x
    y = event.y
    for oval in ovals:
        coord = canvas.coords(oval)
        x0 = coord[0]
        y0 = coord[1]
        x1 = coord[2]
        y1 = coord[3]
        if x0 < x < x1 and y0 < y < y1:
            found = False
            for oval_i in ovals:
                coord_l = canvas.coords(oval_i)
                x0_l = coord_l[0]
                y0_l = coord_l[1]
                x1_l = coord_l[2]
                y1_l = coord_l[3]
                if oval_i != oval and x0_l - 1 * r-5 < x < x1_l + 1 * r+5 and y0_l - 1 * r-5 < y < y1_l + 1 * r+5:
                    found = True
                    break
            if not found:
                for line in lines:
                    coord_l = canvas.coords(line)
                    x0_l = coord_l[0]
                    y0_l = coord_l[1]
                    x1_l = coord_l[2]
                    y1_l = coord_l[3]
                    if x0_l == x1 - r and y0_l == y1 - r:
                        canvas.coords(line, x, y, x1_l, y1_l)
                        canvas.coords(labels_lines[lines.index(line)], (x + x1_l) / 2 + 14, (y + y1_l) / 2 + 14)
                    elif x1_l == x1 - r and y1_l == y1 - r:
                        canvas.coords(line, x0_l, y0_l, x, y)
                        canvas.coords(labels_lines[lines.index(line)], (x + x0_l) / 2 + 14, (y + y0_l) / 2 + 14)
                canvas.move(oval, x - (x1 - r), y - (y1 - r))
                canvas.move(labels_ovals[ovals.index(oval)], x - (x1 - r), y - (y1 - r))


root = Tk()
root.title("Editor de grafuri")
root.geometry("800x600")

canvas = Canvas(root, width=600, height=400, bg="lightgray")
canvas.pack(pady=20)

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-2>", middle_click)
canvas.bind("<Button-3>", right_click)
canvas.bind("<Double-Button-1>", double_left_click)
canvas.bind("<B1-Motion>", left_motion)

key_lab = Label(root, text="Key", font="Arial 11")
key_lab.pack(pady=10)

key = Entry(root, width=200, bg="white", font="Arial 11")
key.pack(padx=20)
key.insert(0, 'Key:')

value_lab = Label(root, text="Value", font="Arial 11")
value_lab.pack(pady=10)

value = Entry(root, width=200, bg="white", font="Arial 11")
value.pack(padx=20)
value.insert(0, 'Value:')

ovals = []
lines = []
labels_ovals = []
labels_lines = []

root.mainloop()
