import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")
        self.root.config(bg="#f2f2f2")

        self.expression = ""

        # Display
        self.display = tk.Entry(self.root, font=("Arial", 24), bg="#fff", borderwidth=2, relief="solid")
        self.display.pack(expand=True, fill="both")

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            tk.Button(button_frame, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(button)

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
