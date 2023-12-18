from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Drawing Shapes Part - 1")
root.geometry("1300x1300")

canvas = Canvas(root, height=510, width = 1300, bg = "white", highlightbackground="lightgrey")
canvas.pack()

label = Label(root, text = "Choose Colour")
label.place(relx = 0.7, rely = 0.8, anchor = CENTER)

startx = Label(root, text = "StartX")
startx.place(relx = 0.1, rely = 0.7099, anchor = CENTER)

endx = Label(root, text = "EndX")
endx.place(relx = 0.5, rely = 0.7099, anchor = CENTER)

starty = Label(root, text = "StartY")
starty.place(relx = 0.3, rely = 0.7099, anchor = CENTER)

endy = Label(root, text = "EndY")
endy.place(relx = 0.7, rely = 0.7099, anchor = CENTER)

coordinates_values_x = ["- 10", "50", "100", "200", "300", "400", "500", "600", "800", "900"]
selected_cordinates_x = StringVar()
Drop_Cordinates_x = ttk.Combobox(root, state="readonly", values = coordinates_values_x, width = 15)
Drop_Cordinates_x.place(relx = 0.2, rely = 0.7099, anchor = CENTER)

coordinates_values_x_end = ["- 10", "50", "100", "200", "300", "400", "500", "600", "800", "900"]
selected_cordinates_x_end = StringVar()
Drop_Cordinates_x_end = ttk.Combobox(root, state="readonly", values = coordinates_values_x_end, width = 15)
Drop_Cordinates_x_end.place(relx = 0.6, rely = 0.7099, anchor = CENTER)

coordinates_values_y = ["- 10", "50", "100", "200", "300", "400", "500", "600", "800", "900"]
selected_cordinates_y = StringVar()
Drop_Cordinates_y = ttk.Combobox(root, state="readonly", values = coordinates_values_y, width = 15)
Drop_Cordinates_y.place(relx = 0.4, rely = 0.7099, anchor = CENTER)

coordinates_values_y_end = ["- 10", "50", "100", "200", "300", "400", "500", "600", "800", "900"]
selected_cordinates_y_end = StringVar()
Drop_Cordinates_y_end = ttk.Combobox(root, state="readonly", values = coordinates_values_y_end, width = 15)
Drop_Cordinates_y_end.place(relx = 0.8, rely = 0.7099, anchor = CENTER)

Color_list = ["blue", "yellow", "red", "green"]
selected_color = StringVar()
DropDown = ttk.Combobox(root, state="readonly", values = Color_list, width = 15)
DropDown.place(relx = 0.8, rely = 0.8, anchor = CENTER)

root.mainloop()