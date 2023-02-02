import tkinter as tk
import random
import time


class WhackAMole:
    def __init__(self, master):
        self.master = master
        self.master.title("Whack-A-Mole")
        self.master.geometry("400x400+0+0")

        # Add a legend to show the score values for each mole
        self.legend = tk.Label(self.master, text="Mole Color Legend\nRed: 1 point\nGreen: 2 points\nBlue: 3 points",
                               font=("Arial", 12), fg="black")
        self.legend.pack()

        self.score = 0
        self.score_label = tk.Label(self.master, text="Score: 0", font=("Arial", 20), fg="red")
        self.score_label.pack()

        self.misses = 0
        self.misses_label = tk.Label(self.master, text="Misses: 0", font=("Arial", 20), fg="blue")
        self.misses_label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack()

        # 5 by 5 grid
        self.grid = tk.Frame(self.master)
        self.grid.pack()

        self.moles = []
        colors = ['red', 'green', 'blue']
        for i in range(25):
            mole = tk.Button(self.grid, text="*", font=("Arial", 20), height=2, width=4, state="disable")
            mole.grid(row=i // 5, column=i % 5)
            mole.color = random.choice(colors)
            self.moles.append(mole)

        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.score = 0
            self.update_score()
            self.popup_moles()

    def stop( self ):
        self.running = False

    def popup_moles( self ):
        if self.running:
            mole = random.choice(self.moles)
            mole["state"] = "normal"
            mole["text"] = "Mole!"
            mole["bg"] = mole.color
            mole.bind("<Button-1>", self.whack)

            # Check if the mole has been clicked before the next mole appears
            if self.misses == 0:
                self.misses += 1
                self.update_misses()

            self.master.after(1000, self.popdown_moles, mole)

    def popdown_moles( self, mole ):
        if self.running:
            mole["state"] = "disable"
            mole["text"] = "*"
            mole["bg"] = "grey"
            mole.unbind("<Button-1>")
            self.master.after(900, self.popup_moles)

    def whack( self, event ):
        if event.widget.color == 'red':
            self.score += 1
        elif event.widget.color == 'green':
            self.score += 2
        else:
            self.score += 3
        self.update_score()
        self.update_misses()
        event.widget["state"] = "disable"
        event.widget["text"] = "*"
        event.widget["bg"] = "grey"

    def update_score( self ):
        self.score_label["text"] = "Score: {}".format(self.score)

    def update_misses( self ):
        self.misses_label["text"] = "Misses: {}".format(self.misses)


if __name__ == "__main__":
    root = tk.Tk()
    whack = WhackAMole(root)
    root.mainloop()