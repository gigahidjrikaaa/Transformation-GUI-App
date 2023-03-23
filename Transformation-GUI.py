### GIGA HIDJRIKA AURA ADKHY ###
### 21/479228/TK/552833 ###
### Berantakan, tapi bisa jalan ###

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import random
import math

# create a class for the coordinate system
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# input window class
class InputWindow(tk.Tk):
    def __init__(self, points):
        tk.Tk.__init__(self)
        self.geometry("500x300")
        self.title("Input Coordinates")

        # create a frame to hold the fields
        frame = ttk.Frame(self)
        frame.pack()

        # create a label for the first point
        ttk.Label(frame, text="Point A").grid(row=0, column=0, padx=5, pady=5)

        # create a label for the x coordinate of the first point
        ttk.Label(frame, text="X:").grid(row=1, column=0, padx=5, pady=5)

        # create a field for the x coordinate of the first point
        self.x_a = ttk.Entry(frame)
        self.x_a.grid(row=1, column=1, padx=5, pady=5)

        # create a label for the y coordinate of the first point
        ttk.Label(frame, text="Y:").grid(row=1, column=2, padx=5, pady=5)

        # create a field for the y coordinate of the first point
        self.y_a = ttk.Entry(frame)
        self.y_a.grid(row=1, column=3, padx=5, pady=5)

        # create a label for the second point
        ttk.Label(frame, text="Point B").grid(row=2, column=0, padx=5, pady=5)

        # create a label for the x coordinate of the second point
        ttk.Label(frame, text="X:").grid(row=3, column=0, padx=5, pady=5)

        # create a field for the x coordinate of the second point
        self.x_b = ttk.Entry(frame)
        self.x_b.grid(row=3, column=1, padx=5, pady=5)

        # create a label for the y coordinate of the second point
        ttk.Label(frame, text="Y:").grid(row=3, column=2, padx=5, pady=5)

        # create a field for the y coordinate of the second point
        self.y_b = ttk.Entry(frame)
        self.y_b.grid(row=3, column=3, padx=5, pady=5)

        # create a label for the third point
        ttk.Label(frame, text="Point C").grid(row=4, column=0, padx=5, pady=5)

        # create a label for the x coordinate of the third point
        ttk.Label(frame, text="X:").grid(row=5, column=0, padx=5, pady=5)

        # create a field for the x coordinate of the third point
        self.x_c = ttk.Entry(frame)
        self.x_c.grid(row=5, column=1, padx=5, pady=5)

        # create a label for the y coordinate of the third point
        ttk.Label(frame, text="Y:").grid(row=5, column=2, padx=5, pady=5)

        # create a field for the y coordinate of the third point
        self.y_c = ttk.Entry(frame)
        self.y_c.grid(row=5, column=3, padx=5, pady=5)

        # create a label for the fourth point
        ttk.Label(frame, text="Point D").grid(row=6, column=0, padx=5, pady=5)

        # create a label for the x coordinate of the fourth point
        ttk.Label(frame, text="X:").grid(row=7, column=0, padx=5, pady=5)

        # create a field for the x coordinate of the fourth point
        self.x_d = ttk.Entry(frame)
        self.x_d.grid(row=7, column=1, padx=5, pady=5)

        # create a label for the y coordinate of the fourth point
        ttk.Label(frame, text="Y:").grid(row=7, column=2, padx=5, pady=5)

        # create a field for the y coordinate of the fourth point
        self.y_d = ttk.Entry(frame)
        self.y_d.grid(row=7, column=3, padx=5, pady=5)

        # set default values for the fields
        self.x_a.insert(0, "0")
        self.x_b.insert(0, "100")
        self.x_c.insert(0, "100")
        self.x_d.insert(0, "0")
        self.y_a.insert(0, "0")
        self.y_b.insert(0, "0")
        self.y_c.insert(0, "-100")
        self.y_d.insert(0, "-100")

        # create a button to create the transformation window
        ttk.Button(self, text="Create Transformation Window", command=lambda: self.create_window(points)).pack()

    def assign_numbers(self, points):
        # assign the values of the fields to the points
        points[0].x = self.x_a.get()
        points[1].x = self.x_b.get()
        points[2].x = self.x_c.get()
        points[3].x = self.x_d.get()
        points[0].y = self.y_a.get()
        points[1].y = self.y_b.get()
        points[2].y = self.y_c.get()
        points[3].y = self.y_d.get()

    # function to create transformation window top level window
    def create_window(self, points):
        # check if the values of the fields are numbers
        if not self.is_number(self.x_a.get()) or not self.is_number(self.x_b.get()) or not self.is_number(self.x_c.get()) or not self.is_number(self.x_d.get()) or not self.is_number(self.y_a.get()) or not self.is_number(self.y_b.get()) or not self.is_number(self.y_c.get()) or not self.is_number(self.y_d.get()):
            tk.messagebox.showerror("Error", "Please enter numbers for the coordinates")
            return
        self.assign_numbers(points)
        print("====================================")
        print("==== NEW TRANSFORMATION WINDOW =====")
        print("====================================")
        transformationWindow = TransformationWindow(self, points)
        transformationWindow.mainloop()

    # function to check if the values of the fields are numbers
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

# create a class for the main window
class TransformationWindow(tk.Toplevel):
    def __init__(self, parent, points):
        tk.Toplevel.__init__(self, parent)
        self.geometry("900x700")
        self.title("Transformation Window")

        original_points = [Coordinate(0, 0), Coordinate(0, 0), Coordinate(0, 0), Coordinate(0, 0)]

        # make the points values as integers
        for i, point in enumerate(points):
            point.x = int(point.x)
            point.y = int(point.y)
            original_points[i].x = point.x
            original_points[i].y = point.y

        CANVASWIDTH = 1000
        CANVASHEIGHT = 500

        # create a canvas
        self.canvas = tk.Canvas(self, width=CANVASWIDTH, height=CANVASHEIGHT, bg="white")
        self.canvas.configure(scrollregion=(-1000, -1000, 1000, 1000))

        # Zoom in and out when pressing Ctrl + mouse wheel
        self.canvas.bind("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
        self.canvas.bind("<Control-MouseWheel>", lambda event: self.canvas.xview_scroll(int(-1*(event.delta/120)), "units"))

        # Center to scroll region to origin when window is opened
        self.canvas.xview("moveto", 0.25)
        self.canvas.yview("moveto", 0.375)

        self.canvas.pack()

        # create a frame for the buttons
        frame = ttk.Frame(self)
        frame.pack()

        # create 2 input fields for the translation
        self.x = ttk.Entry(frame)
        self.x.grid(row=0, column=1, padx=5, pady=5)
        self.y = ttk.Entry(frame)
        self.y.grid(row=0, column=3, padx=5, pady=5)

        # set default values for the fields
        self.x.insert(0, "0")
        self.y.insert(0, "0")

        # create a button to translate the points
        ttk.Button(frame, text="Translate", command=lambda: self.translation(points, self.x.get(), self.y.get(), frame)).grid(row=0, column=4, padx=5, pady=5)

        # create 2 input fields for the rotation
        self.angle = ttk.Entry(frame)
        self.angle.grid(row=1, column=1, padx=5, pady=5)

        # create 2 input fields for the origin of the rotation
        self.x_origin = ttk.Entry(frame)
        self.x_origin.grid(row=1, column=2, padx=5, pady=5)
        self.y_origin = ttk.Entry(frame)
        self.y_origin.grid(row=1, column=3, padx=5, pady=5)

        # set default values for the fields
        self.angle.insert(0, "0")
        self.x_origin.insert(0, "0")
        self.y_origin.insert(0, "0")

        # create a button to rotate the points
        ttk.Button(frame, text="Rotate", command=lambda: self.rotation(points, self.angle.get(), frame, self.x_origin.get(), self.y_origin.get())).grid(row=1, column=4, padx=5, pady=5)

        # create 2 input fields for the scaling
        self.x_scale = ttk.Entry(frame)
        self.x_scale.grid(row=2, column=1, padx=5, pady=5)
        self.y_scale = ttk.Entry(frame)
        self.y_scale.grid(row=2, column=3, padx=5, pady=5)

        # set default values for the fields
        self.x_scale.insert(0, "1")
        self.y_scale.insert(0, "1")

        # create a button to scale the points
        ttk.Button(frame, text="Scale", command=lambda: self.scaling(points, self.x_scale.get(), self.y_scale.get(), frame)).grid(row=2, column=4, padx=5, pady=5)

        # create a button to reset the points
        ttk.Button(frame, text="Reset", command=lambda: self.reset(points, frame, original_points)).grid(row=3, column=4, padx=5, pady=5)

        self.update_points(points, frame)

    def reset(self, points, frame, original_points):
        print("Resetting points: ")
        for i, point in enumerate(points):
            point.x = original_points[i].x
            point.y = original_points[i].y
            print("x: " + str(point.x) + " y: " + str(point.y))
        self.update_points(points, frame)

    def translation(self, points, x, y, frame):
        if(not self.check_input(x, y)):
            return False
        else:
            for point in points:
                point.x += int(x)
                point.y += int(y)

            print("Translated points: ")
            for point in points:
                print("x: " + str(point.x) + " y: " + str(point.y))

            self.update_points(points, frame)

    # Rotate the pointes around the origin
    def rotation(self, points, angle, frame, origin_x, origin_y):
        if(not self.check_input(angle, origin_x, origin_y)):
            return False
        else:
            # translate the points to the origin
            self.translation(points, -int(origin_x), -int(origin_y), frame)
            # convert the angle to radians
            angle = int(angle)
            angle = math.radians(angle)

            # calculate the sine and cosine of the angle
            sine = math.sin(angle)
            cosine = math.cos(angle)

            # rotate the points
            for point in points:
                x = point.x * cosine - point.y * sine
                y = point.x * sine + point.y * cosine
                point.x = x
                point.y = y
                # round the points to the nearest integer
                point.x = round(point.x)
                point.y = round(point.y)

            # translate the points back to the original position
            self.translation(points, origin_x, origin_y, frame)

            print("Rotated points: ")
            for point in points:
                print("x: " + str(point.x) + " y: " + str(point.y))

            self.update_points(points, frame)


    def scaling(self, points, x, y, frame):
        if(not self.check_input(x, y)):
            return False
        else:
            for point in points:
                point.x *= int(x)
                point.y *= int(y)
            for point in points:
                print("x: " + str(point.x) + " y: " + str(point.y))

            self.update_points(points, frame)

            print("Scaled points: ")
            for point in points:
                print("x: " + str(point.x) + " y: " + str(point.y))

    def draw_points(self, points):
        # draw the points
        for point in points:
            self.canvas.create_oval(point.x-2.5, point.y-2.5, point.x + 2.5, point.y + 2.5, fill="red")
        self.draw_xy_line()

    def draw_shape(self, points):
        # draw the shape
        self.canvas.create_line(points[0].x, points[0].y, points[1].x, points[1].y, fill="black")
        self.canvas.create_line(points[1].x, points[1].y, points[2].x, points[2].y, fill="black")
        self.canvas.create_line(points[2].x, points[2].y, points[3].x, points[3].y, fill="black")
        self.canvas.create_line(points[3].x, points[3].y, points[0].x, points[0].y, fill="black")

    def update_points(self, points, frame):
        self.canvas.delete("all")
        self.draw_shape(points)
        self.draw_points(points)
        self.coord_info(frame, points)
        self.print_numbers_on_axis()
    
    def draw_xy_line(self):
        self.canvas.create_line(0, -1000, 0, 1000, fill="black")
        self.canvas.create_line(-1000, 0, 1000, 0, fill="black")

    # print the numbers on the axis with a step of 50
    def print_numbers_on_axis(self):
        for i in range(0, 2000, 50):
            self.canvas.create_text(i, 0, text=str(i), fill="black")
            self.canvas.create_text(-i, 0, text=str(-i), fill="black")
            self.canvas.create_text(0, -i, text=str(-i), fill="black")
            self.canvas.create_text(0, i, text=str(i), fill="black")

    def coord_info(self, frame, points):
        # create a label that shows the current coordinates of the points

        self.label = ttk.Label(frame, text="Current coordinates: ")
        self.label.grid(row=0, column=5, padx=5, pady=5)

        self.label = ttk.Label(frame, text="A: x: " + str(points[0].x) + " y: " + str(points[0].y))
        self.label.grid(row=1, column=5, padx=5, pady=5)

        self.label = ttk.Label(frame, text="B: x: " + str(points[1].x) + " y: " + str(points[1].y))
        self.label.grid(row=2, column=5, padx=5, pady=5)

        self.label = ttk.Label(frame, text="C: x: " + str(points[2].x) + " y: " + str(points[2].y))
        self.label.grid(row=1, column=6, padx=5, pady=5)

        self.label = ttk.Label(frame, text="D: x: " + str(points[3].x) + " y: " + str(points[3].y))
        self.label.grid(row=2, column=6, padx=5, pady=5)

    # function to check if input is empty. If it is empty, fill it with 0
    def check_input(self, *args):
        # check if the arguments are empty
        for arg in args:
            if arg == "":
                messagebox.showerror("Error", "Please fill in all the fields")
                return False
        # check if the arguments are numbers
        for arg in args:
            if not self.is_number(arg):
                messagebox.showerror("Error", "Please fill in all the fields with numbers")
                return False
        return True
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


# main process
if __name__ == "__main__":
    points = [Coordinate(0, 0), Coordinate(0, 0), Coordinate(0, 0), Coordinate(0, 0)]
    print("  ####### ######     #    #     #  #####  ####### ####### ######  #     #    #    ####### ### ####### #     #    ######  ######  #######  #####  ######     #    #     # ")
    print("     #    #     #   # #   ##    # #     # #       #     # #     # ##   ##   # #      #     #  #     # ##    #    #     # #     # #     # #     # #     #   # #   ##   ## ")
    print("     #    #     #  #   #  # #   # #       #       #     # #     # # # # #  #   #     #     #  #     # # #   #    #     # #     # #     # #       #     #  #   #  # # # # ")
    print("     #    ######  #     # #  #  #  #####  #####   #     # ######  #  #  # #     #    #     #  #     # #  #  #    ######  ######  #     # #  #### ######  #     # #  #  # ")
    print("     #    #   #   ####### #   # #       # #       #     # #   #   #     # #######    #     #  #     # #   # #    #       #   #   #     # #     # #   #   ####### #     # ")
    print("     #    #    #  #     # #    ## #     # #       #     # #    #  #     # #     #    #     #  #     # #    ##    #       #    #  #     # #     # #    #  #     # #     # ")
    print("     #    #     # #     # #     #  #####  #       ####### #     # #     # #     #    #    ### ####### #     #    #       #     # #######  #####  #     # #     # #     # ")
    inputWindow = InputWindow(points)
    inputWindow.mainloop()