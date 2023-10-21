import tkinter as tk

# Function to perform mathematical operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operator"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# Tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Entry fields for numbers
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)
entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=2)

# Label and variable for the operator
operator_var = tk.StringVar()
operator_label = tk.Label(window, text="Operator:")
operator_label.grid(row=0, column=1)
operator_dropdown = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_dropdown.grid(row=0, column=3)

# Button to calculate
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=4)

# Label to display the result
result_label = tk.Label(window, text="Result:")
result_label.grid(row=2, column=0, columnspan=4)

# Start the Tkinter event loop
window.mainloop()
