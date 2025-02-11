import tkinter as tk
from tkinter import messagebox
from currency_backend import convert_currency

def perform_conversion():
    """Handles conversion when the button is clicked"""
    try:
        amount = float(amount_entry.get())
        base_currency = base_currency_entry.get().upper()
        target_currency = target_currency_entry.get().upper()
        
        result, error = convert_currency(amount, base_currency, target_currency)
        
        if error:
            messagebox.showerror("Error", error)
        else:
            result_label.config(text=f"{amount} {base_currency} = {result:.2f} {target_currency}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")

# GUI Setup for Converter
root = tk.Tk()
root.title("Currency Converter 💰")
root.geometry("400x300")
root.resizable(False, False)

# Labels
tk.Label(root, text="Amount:", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=5)

tk.Label(root, text="From Currency (e.g., USD):", font=("Arial", 12)).pack(pady=5)
base_currency_entry = tk.Entry(root, font=("Arial", 12))
base_currency_entry.pack(pady=5)

tk.Label(root, text="To Currency (e.g., EUR):", font=("Arial", 12)).pack(pady=5)
target_currency_entry = tk.Entry(root, font=("Arial", 12))
target_currency_entry.pack(pady=5)

#Convert Button
convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=perform_conversion)
convert_button.pack(pady=10)

#Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

#Start app
root.mainloop()
