import tkinter as tk
import random
import time


class SimonGame:
    def __init__( self, master ):
        self.master = master
        self.master.title("Simon Game")
        self.master.geometry("500x500")
        self.master.config(bg='white')

        self.colors = ["#ff0000", "#0000ff", "#00ff00", "#ffff00"]
        self.light_colors = ["#ff8080", "#8080ff", "#80ff80", "#ffff80"]
        self.sequence = []
        self.player_sequence = []
        self.round_number = 1

        self.status_label = tk.Label(self.master, text="Start the game!", font=("Arial", 16), bg='white')
        self.status_label.pack(pady=20)

        self.play_button = tk.Button(self.master, text="Play", font=("Arial", 16), command=self.play_game)
        self.play_button.pack(pady=20)

        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=20)

        self.buttons = []
        for i in range(4):
            button = tk.Button(button_frame, bg=self.colors[i], height=100 // 5, width=100 // 5)
            button.grid(row=i // 2, column=i % 2)
            self.buttons.append(button)

    def display_sequence( self, sequence ):
        for color_index in sequence:
            button = self.buttons[color_index]
            button.config(bg=self.light_colors[color_index])
            self.master.update()
            time.sleep(1)
            button.config(bg=self.colors[color_index])
            self.master.update()
            time.sleep(0.5)

    def check_sequence( self, player_sequence, sequence ):
        if player_sequence == sequence:
            return True
        else:
            return False

    def click_button( self, color_index ):
        self.player_sequence.append(color_index)
        if len(self.player_sequence) == len(self.sequence):
            if self.check_sequence(self.player_sequence, self.sequence):
                self.status_label.config(text="Correct! Get ready for round {}".format(self.round_number + 1))
                self.round_number += 1
                self.player_sequence = []
                self.sequence.append(random.randint(0, 3))
                self.display_sequence(self.sequence)
                self.play_button.config(state='normal')
            else:
                self.status_label.config(text="Wrong answer! Game Over")
                self.play_button.config(state='normal')
                self.sequence = []
                self.player_sequence = []
                self.round_number = 1

    def play_game( self ):
        self.play_button.config(state='disabled')
        self.status_label.config(text="Get ready for round 1")
        self.sequence.append(random.randint(0, 3))
        self.display_sequence(self.sequence)


if __name__ == '__main__':
    root = tk.Tk()
    SimonGame(root)
    root.mainloop()