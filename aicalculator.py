import tkinter as tk
from tkinter import ttk

class AICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x380")
        # Windows 2000 style gray
        self.root.configure(bg="#c0c0c0")
        self.root.resizable(False, False)
        try:
            self.root.iconbitmap("calculator_icon.ico")
        except Exception:
            pass

        # outer beveled frame
        self.main_frame = tk.Frame(self.root, bg="#c0c0c0", relief="ridge", bd=4)
        self.main_frame.pack(padx=8, pady=8)

        # display area (sunken, dark display like older calculators)
        self.input_frame = tk.Frame(self.main_frame, bg="#d0d0d0", relief="sunken", bd=2)
        self.input_frame.pack(padx=6, pady=(6, 4), fill="x")

        # visual display (black background, green digits)
        self.input_entry = tk.Entry(
            self.input_frame,
            width=16,
            font=("Courier New", 24, "bold"),
            justify="right",
            bd=0,
            bg="#000000",
            fg="#33FF33",
            insertbackground="#33FF33",
            relief="flat"
        )
        self.input_entry.grid(row=0, column=0, padx=8, pady=8, sticky="ew")
        self.input_entry.insert(0, "")
        # make the entry look read-only while still allowing programmatic edits
        # (we'll keep it writable for button input)
        self.input_frame.grid_columnconfigure(0, weight=1)

        # button container with same classic gray
        self.button_frame = tk.Frame(self.main_frame, bg="#c0c0c0")
        self.button_frame.pack(padx=6, pady=(0,6))

        # button layout similar to classic calc
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C"]
        ]

        # Use classic tk.Button to get 3D look like Windows 2000
        btn_cfg = dict(
            font=("Arial", 12, "bold"),
            width=4,
            height=2,
            bd=2,
            bg="#e0e0e0",
            activebackground="#d0d0d0",
            relief="raised",
            takefocus=False
        )

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                btn = tk.Button(self.button_frame, text=label, command=lambda l=label: self.on_click(l), **btn_cfg)
                if label == "C":
                    btn.grid(row=r, column=0, columnspan=4, sticky="nsew", padx=4, pady=6)
                else:
                    btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

        # make columns and rows expand evenly for consistent sizing
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1, minsize=48)
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1, minsize=40)

    def on_click(self, label):
        if label == "C":
            self.input_entry.delete(0, tk.END)
        elif label == "=":
            self.calculate()
        else:
            self.input_entry.insert(tk.END, label)

    def calculate(self):
        expr = self.input_entry.get()
        try:
            # basic eval; runs locally
            result = eval(expr)
            # format integers without decimal point when possible
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, str(result))
        except Exception:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, "Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = AICalculatorApp(root)
    root.mainloop()