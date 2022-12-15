import tkinter as tk
from tkinter import ttk
from ctypes import windll
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frame1 = ttk.Frame(self)
        self.frame1.pack()

        self.frame2 = ttk.Frame(self)
        self.frame2.pack(pady=30)

        self.sep = ttk.Separator(self, orient='horizontal', ).pack(fill='x')

        self.frame3 = ttk.Frame(self)
        self.frame3.pack(pady=30)

        self.frame4 = ttk.Frame(self)
        self.frame4.pack(pady=30)

        self.message = ttk.Label(self.frame1,
                                 text="Enter initial State (Click R,G,B accordingly) ",
                                 font=("Helvetica", 14))  # place a label on the root window
        self.message2 = ttk.Label(self.frame3,
                                  text="Enter Goal State (Click R,G,B accordingly) ",
                                  font=("Helvetica", 14))  # place a label on the root window

        self.b = [[], [], []]
        self.g = [[], [], []]
        self.memoryColors = []
        self.memoryColorsGoal = []
        self.count = 0
        self.count2 = 0
        self.colors = ["red", "green", "blue"]
        self.message.pack()
        self.displayWindow()
        self.message2.pack()

    def button(self, frame):
        return tk.Button(frame, bd=5, width=2, font=('arial', 30, 'bold'))

    def fill(self, i, j):
        self.b[i][j]["bg"] = self.colors[self.count]
        color = Color(i, j, self.colors[self.count])
        self.memoryColors.append(color)
        self.count += 1

        if self.count == 3:
            for i in range(3):
                for j in range(3):
                    self.b[i][j]["state"] = "disabled"

        print(self.memoryColors[-1].i, self.memoryColors[-1].j)

    def fill2(self, i, j):
        self.g[i][j]["bg"] = self.colors[self.count2]
        color2 = Color(i, j, self.colors[self.count2])
        self.memoryColorsGoal.append(color2)
        self.count2 += 1

        if self.count2 == 3:
            for i in range(3):
                for j in range(3):
                    self.g[i][j]["state"] = "disabled"

            InputPopUp(self)

    def draw_puzzleInitial(self):
        for i in range(3):
            for j in range(3):
                self.b[i].append(self.button(self.frame2))
                self.b[i][j].config(command=lambda row=i, col=j: self.fill(row, col))
                self.b[i][j].grid(row=i, column=j)

    def draw_puzzleGoal(self):
        for i in range(3):
            for j in range(3):
                self.g[i].append(self.button(self.frame4))
                self.g[i][j].config(command=lambda row=i, col=j: self.fill2(row, col))
                self.g[i][j].grid(row=i, column=j)

    def displayWindow(self):
        self.title("SE 420 Project - Group 3")

        # center the window
        window_width = 800
        window_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()  # get the screen dimensions
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)  # find the center points
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.draw_puzzleInitial()
        self.draw_puzzleGoal()


class Color:
    def __init__(self, i, j, name):
        self.i = i
        self.j = j
        self.name = name


def colorQueueSubmit():
    msg = f"You entered {input.get()}"
    showinfo(
        title='Information',
        message=msg
    )


class Algorithm:
    def __init__(self, algo):
        self.algo = algo


class InputPopUp:
    def __init__(self, master):
        self.drawPopUp()
        self.selectedRadio = tk.IntVar()
        self.selectedRadio.set(1)
        self.radioText = ""
        self.master = master
        self.close = 0

    def getAlgoOrderInput(self, txt):
        print(txt)
        self.close += 1

    def drawPopUp(self):
        root = tk.Toplevel()
        root.title("Input Frame")
        root.geometry("600x200")
        root.frame = ttk.Frame(root)
        root.frame2 = ttk.Frame(root)
        root.frame.pack()
        root.frame2.pack()

        msg = tk.Label(root.frame, text="Please write the order of the tile moves ex:(RGB, GBR ...)")
        msg.pack()

        root.algoOrder = tk.StringVar()
        entry = ttk.Entry(root.frame, textvariable=root.algoOrder)
        entry.pack(fill='x', expand=True, side=tk.LEFT)
        entry.focus()
        submitButton = ttk.Button(root.frame, text="Submit",
                                  command=lambda: self.getAlgoOrderInput(root.algoOrder.get()))
        submitButton.pack(side=tk.LEFT)

        root.algoChoice = tk.StringVar()
        msg2 = tk.Label(root.frame2, text="Choose which algorithm do you want to choose")
        msg2.pack()
        entry = ttk.Entry(root.frame2, textvariable=root.algoChoice)
        entry.pack(fill='x', expand=True, side=tk.LEFT)
        choiceButton = ttk.Button(root.frame2, text="Submit",
                                  command=lambda: self.getAlgoChoiceInput(root.algoChoice.get(),root))
        choiceButton.pack(side=tk.LEFT)
        """msg2 = tk.Label(root.frame2, text="Choose which algorithm do you want to choose")
        msg2.pack()
        entry = ttk.Entry(root.frame2, textvariable=root.algoChoice)
        entry.pack(fill='x', expand=True, side=tk.LEFT)
        rb1 = ttk.Radiobutton(root.frame2, text='A* search', variable=self.selectedRadio, value=1,
                              command=self.selected)
        rb2 = ttk.Radiobutton(root.frame2, text='Uniform cost search', variable=self.selectedRadio, value=2,
                              command=self.selected)
        rb1.pack()
        rb2.pack()
        choiceButton = ttk.Button(root.frame2, text="Submit",
                                  command=lambda: self.getAlgoChoices())
        choiceButton.pack(side=tk.LEFT)"""

    def selected(self):
        if self.selectedRadio.get() == 0:
            self.radioText = "A*"
        elif self.selectedRadio.get() == 1:
            self.radioText = "Uniform Cost"
        else:
            "do something"

        print(self.selectedRadio)
        print(self.radioText)

    def getAlgoChoiceInput(self, param,root):
        print(param)
        self.close += 1
        if (self.close == 2):
            root.destroy()


windll.shcore.SetProcessDpiAwareness(1)
"""app = App(root)
root.mainloop()  # keeps the window visible on the screen"""
if __name__ == "__main__":
    app = App()
    # frame = MainFrame(app)
    app.mainloop()
