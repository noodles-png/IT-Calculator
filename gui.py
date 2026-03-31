import tkinter as tk
from tkinter import ttk
from modules.numbers import number_menu, to_decimal, from_decimal
from modules.storage import storage_menu
from modules.network import network_menu
from modules.subnetting import subnet_menu


class App_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IT-Rechner")
        self.geometry("500x500")

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")

        numbers_tab = ttk.Frame(notebook)
        storage_tab = ttk.Frame(notebook)
        network_tab = ttk.Frame(notebook)
        subnet_tab = ttk.Frame(notebook)

        notebook.add(numbers_tab, text="Numbers")
        notebook.add(storage_tab, text="Storage")
        notebook.add(network_tab, text="Network")
        notebook.add(subnet_tab, text="Subnet")

        NumbersTab(numbers_tab)
        StorageTab(storage_tab)


class NumbersTab:
    def __init__(self, parent):

        # Label + Entry for Input
        ttk.Label(parent, text="Number:").grid(row=0, column=0)
        self.entry = ttk.Entry(parent)
        self.entry.grid(row=0, column=1)

        # Dropdown menu
        ttk.Label(parent, text="System:").grid(row=1, column=0)
        self.combo = ttk.Combobox(parent, values=["Decimal", "Non-Decimal"])
        self.combo.grid(row=1, column=1)

        ttk.Label(parent, text="Base").grid(row=2, column=0)
        self.base_combo = ttk.Combobox(parent, values=["2", "8", "16"])
        self.base_combo.grid(row=2, column=1)

        ttk.Button(parent, text="convert", command=self.numbers_click).grid(row=3, column=1)

        # Label for result
        self.result_label = ttk.Label(parent, text="", justify="left")
        self.result_label.grid(row=4, column=1)
        self.bin_label = ttk.Label(parent, text="", justify="left")
        self.bin_label.grid(row=5, column=1)
        self.oct_label = ttk.Label(parent, text="", justify="left")
        self.oct_label.grid(row=6, column=1)
        self.hex_label = ttk.Label(parent, text="", justify="left")
        self.hex_label.grid(row=7, column=1)

    # Button calls function
    def numbers_click(self):
        self.result_label.config(text="")
        self.bin_label.config(text="")
        self.oct_label.config(text="")
        self.hex_label.config(text="")
        if self.combo.get() == "Decimal":
            value = int(self.entry.get())
            self.bin_label.config(text=f"Binär: {from_decimal(value, 2)}")
            self.oct_label.config(text=f"Oktal: {from_decimal(value, 8)}")
            self.hex_label.config(text=f"Hex: {from_decimal(value, 16)}")
        elif self.combo.get() == "Non-Decimal":
            value = self.entry.get()  # Gets value from entry
            base = int(self.base_combo.get())
            result = to_decimal(value, int(self.base_combo.get()))
            self.result_label.config(text=f"Decimal: {to_decimal(value, base)}")  # Shows result


class StorageTab:
    def __init__(self, parent):

        ttk.Label(parent, text="Input number:").grid(row=0, column=0)
        self.entry = ttk.Entry(parent)
        self.entry.grid(row=0, column=1)

        ttk.Label(parent, text="Base:").grid(row=1, column=0)
        self.combo = ttk.Combobox(parent, values=["2", "10", "16"])
        self.combo.grid(row=1, column=1)

        ttk.Label(parent, text="Output number:").grid(row=3, column=0)
        self.entry = ttk.Entry(parent)
        self.entry.grid(row=3, column=1)

if __name__ == "__main__":
    app = App_window()
    app.mainloop()
