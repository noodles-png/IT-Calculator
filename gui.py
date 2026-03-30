import tkinter as tk
from tkinter import ttk
from modules.numbers import number_menu, to_decimal, from_decimal
from modules.storage import storage_menu
from modules.network import network_menu
from modules.subnetting import subnet_menu

#
root = tk.Tk()
root.title("IT-Rechner")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create Tabs
numbers_tab = ttk.Frame(notebook)
storage_tab = ttk.Frame(notebook)
network_tab = ttk.Frame(notebook)
subnet_tab = ttk.Frame(notebook)

notebook.add(numbers_tab, text="Numbers")
notebook.add(storage_tab, text="Storage")
notebook.add(network_tab, text="Network")
notebook.add(subnet_tab, text="Subnet")


# Label + Entry for Input
ttk.Label(numbers_tab, text="Number:").grid(row=0, column=0)
entry = ttk.Entry(numbers_tab)
entry.grid(row=0, column=1)

# Dropdown menu
ttk.Label(numbers_tab, text="System:").grid(row=1, column=0)
combo = ttk.Combobox(numbers_tab, values=["Decimal", "Non-Decimal"])
combo.grid(row=1, column=1)

ttk.Label(numbers_tab, text="Base").grid(row=2, column=0)
base_combo = ttk.Combobox(numbers_tab, values=["2", "8", "16"])
base_combo.grid(row=2, column=1)


# Button calls function
def on_click():
    result_label.config(text="")
    bin_label.config(text="")
    oct_label.config(text="")
    hex_label.config(text="")
    if combo.get() == "Decimal":
        value = int(entry.get())
        bin_label.config(text=f"Binär: {from_decimal(value, 2)}")
        oct_label.config(text=f"Oktal: {from_decimal(value, 8)}")
        hex_label.config(text=f"Hex: {from_decimal(value, 16)}")
    elif combo.get() == "Non-Decimal":
        value = entry.get()  # Gets value from entry
        base = int(base_combo.get())
        result = to_decimal(value, int(base_combo.get()))
        result_label.config(text=f"Decimal: {to_decimal(value, base)}")  # Shows result


ttk.Button(numbers_tab, text="convert", command=on_click).grid(row=3, column=1)

# Label for result
result_label = ttk.Label(numbers_tab, text="", justify="left")
result_label.grid(row=4, column=1)
bin_label = ttk.Label(numbers_tab, text="", justify="left")
bin_label.grid(row=5, column=1)
oct_label = ttk.Label(numbers_tab, text="", justify="left")
oct_label.grid(row=6, column=1)
hex_label = ttk.Label(numbers_tab, text="", justify="left")
hex_label.grid(row=7, column=1)

root.mainloop()