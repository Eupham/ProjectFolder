import tkinter as tk

class CalculatorButton:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ScientificButton(CalculatorButton):
    pass

class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.display = tk.StringVar()
        self.display_entry = tk.Entry(self.parent, textvariable=self.display)
        self.display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        self.create_button_tree(parent, self.get_tokens(), 1, 0)

        for i in range(20):
            self.parent.columnconfigure(i, weight=1)
        for i in range(10):
            self.parent.rowconfigure(i, weight=1)

    def get_tokens(self):
        return {
            "Input signal (x)": {
                "Basic operations": {
                    "+": '+',
                    "-": '-',
                    "x": '*',
                    "/": '/',
                    "^": '^'
                },
                "Trigonometric functions": {
                    "sin": 'sin',
                    "cos": 'cos',
                    "tan": 'tan'
                },
                "Logarithmic functions": {
                    "log": 'log',
                    "ln": 'ln'
                },
                "Statistical functions": {
                    "mean": 'mean',
                    "variance": 'variance',
                    "standard deviation": 'standard deviation'
                },
                "Fourier transforms": {
                    "FFT": 'FFT',
                    "IFFT": 'IFFT'
                },
                "Filtering": {
                    "high-pass": 'high-pass',
                    "low-pass": 'low-pass',
                    "band-pass": 'band-pass'
                }
            },
            "Output signal (y)": 'y'
        }


    def create_button_tree(self, parent, node, row, col):
        if isinstance(node, list):
            for index, item in enumerate(node):
                self.create_button_tree(parent, item, row + index, col)
        elif isinstance(node, dict):
            for index, (key, value) in enumerate(node.items()):
                tk.Button(parent, text=key,
                      command=lambda v=value: self.create_button_tree(parent, v, row + index, col + 1)).grid(row=row + index,
                                                                                                                column=col)
                self.create_button_tree(parent, value, row + index, col + 1)
        else:
            tk.Button(parent, text=node, command=lambda v=node: self.append_to_display(v)).grid(row=row, column=col)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Acoustics Calculator")
    root.geometry("500x400")

    display = tk.StringVar()
    display_entry = tk.Entry(root, textvariable=display)
    display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)
    calculator = Calculator(root)

    root.mainloop()