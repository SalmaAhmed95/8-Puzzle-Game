import tkinter as tk
import time
import turtle

from tkinter import messagebox


class Visualizer:
    def __init__(self, path, side_length, x, y, color):
        self.path = path
        self.current_index = 0
        self.cells = path[self.current_index]
        self.markers = [[None, None, None], [None, None, None], [None, None, None]]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(master=self.root, width=500, height=500)
        self.canvas.pack()
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.tracer(False)
        self.t = turtle.RawTurtle(self.screen, visible=False)
        tk.Button(master=self.root,text="Previous", command=self.previous).pack(side=tk.LEFT)
        tk.Button(master=self.root, text="Next", command=self.next).pack(side=tk.RIGHT)
        self.SIZE = side_length
        self.font = ("Arial", int(0.75 * self.SIZE), "normal")
        self.posX, self.posY = x, y
        self.t.width = 4
        self.t.speed('fastest')
        self.t.color(color, 'white')

    def set_matrix(self, updated_matrix):
        self.cells = updated_matrix

    def draw_square(self, side):
        position = self.t.position()

        self.t.pendown()

        for _ in range(4):
            self.t.forward(side)
            self.t.right(90)

        self.t.penup()
        self.t.goto(position)
        self.t.pendown()

    def draw_board(self):
        for row in range(3):
            for col in range(3):
                self.t.penup()

                topLeftX = self.posX + col * self.SIZE
                topLeftY = self.posY - row * self.SIZE
                self.t.goto(topLeftX, topLeftY)
                self.draw_square(self.SIZE)

                self.t.penup()
                self.t.goto(topLeftX, topLeftY)
                self.t.right(90)
                self.t.forward(self.SIZE)
                self.t.left(90)
                self.t.forward(self.SIZE / 2)

                data = self.cells[row][col] if self.cells[row][col] != 0 else ''
                marker = self.t.clone()
                marker.write(data, align="center", font=self.font)

                self.markers[row][col] = marker

        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()

    def previous(self):
        self.t.color('black', 'white')
        if self.current_index > 0:
            self.current_index = self.current_index - 1
            self.canvas.delete("all")
            self.t.clear()
            self.set_matrix(self.path[self.current_index])
            self.draw_board()

    def next(self):
        if self.current_index < len(self.path) - 1:
            self.current_index = self.current_index + 1
            if self.current_index == len(self.path) - 1:
                self.t.color('red', 'white')
            self.canvas.delete("all")
            self.t.clear()
            self.set_matrix(self.path[self.current_index])
            self.draw_board()

    def play(self):
        self.draw_board()
        time.sleep(1)
        if len(self.path) == 1:
            messagebox.showerror("Error", "Puzzle is not solvable! ")
        self.root.mainloop()


