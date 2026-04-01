import tkinter as tk
from tkinter import ttk
from modules.numbers import to_decimal, from_decimal
from modules.storage import storage_conv, dec_units, bi_units
from modules.network import network_menu
from modules.subnetting import subnet_menu
from modules.helpers import unit_choice


class App_window(tk.Tk):
    def __init__(self):
        """ Defines the tkinter window and tabs"""
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
        """ Defines the structure of numbers tab"""
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

        ttk.Button(parent, text="Convert", command=self.numbers_click).grid(row=3, column=1)

        # Label for result
        self.result_label = ttk.Label(parent, text="", justify="left")
        self.result_label.grid(row=4, column=1)
        self.bin_label = ttk.Label(parent, text="", justify="left")
        self.bin_label.grid(row=5, column=1)
        self.oct_label = ttk.Label(parent, text="", justify="left")
        self.oct_label.grid(row=6, column=1)
        self.hex_label = ttk.Label(parent, text="", justify="left")
        self.hex_label.grid(row=7, column=1)


    def numbers_click(self):
        """ Calls numbers function from numbers module """
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
        """ Defines the structure of storage tab"""
        # Input
        ttk.Label(parent, text="Value:").grid(row=0, column=0)
        self.entry = ttk.Entry(parent)
        self.entry.grid(row=0, column=1)

        ttk.Label(parent, text="Mode:").grid(row=1, column=0)
        self.from_mode = ttk.Combobox(parent, values=["Decimal", "Binary"])
        self.from_mode.bind("<<ComboboxSelected>>", self.update_from_units)
        self.from_mode.grid(row=1, column=1)

        ttk.Label(parent, text="From:").grid(row=2, column=0)
        self.from_combo = ttk.Combobox(parent)
        self.from_combo.grid(row=2, column=1)

        # Output
        ttk.Label(parent, text="Mode:").grid(row=3, column=0)
        self.to_mode = ttk.Combobox(parent, values=["Decimal", "Binary"])
        self.to_mode.bind("<<ComboboxSelected>>", self.update_to_units)
        self.to_mode.grid(row=3, column=1)

        ttk.Label(parent, text="To:").grid(row=4, column=0)
        self.to_combo = ttk.Combobox(parent)
        self.to_combo.grid(row=4, column=1)

        ttk.Button(parent, text="Convert", command=self.storage_click).grid(row=5, column=1)

        self.result_label = ttk.Label(parent, text="")
        self.result_label.grid(row=6, column=1)

    def update_from_units(self, event):
        if self.from_mode.get() == "Decimal":
            self.from_combo["values"] = list(dec_units.keys())
        else:
            self.from_combo["values"] = list(bi_units.keys())
        self.from_combo.set("")

    def update_to_units(self, event):
        if self.to_mode.get() == "Decimal":
            self.to_combo["values"] = list(dec_units.keys())
        else:
            self.to_combo["values"] = list(bi_units.keys())
        self.to_combo.set("")


    def storage_click(self):
        """ Calls storage function from storage module """
        self.result_label.config(text="")

        value = float(self.entry.get())
        from_unit = self.from_combo.get()
        to_unit = self.to_combo.get()

        if self.from_mode.get() == "Decimal":
            from_factor = dec_units[from_unit]
        else:
            from_factor = bi_units[from_unit]

        if self.to_mode.get() == "Decimal":
            to_factor = dec_units[to_unit]
        else:
            to_factor = bi_units[to_unit]

        result = value * from_factor / to_factor
        self.result_label.config(text=f"Result: {result}")


class NetworkTab:
    def __init__(self, parent):
        """ Defines the structure of network tab"""

if __name__ == "__main__":
    app = App_window()
    app.mainloop()
