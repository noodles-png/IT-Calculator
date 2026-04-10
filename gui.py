import argparse
import tkinter as tk
from tkinter import ttk
from modules.numbers import to_decimal, from_decimal
from modules.storage import dec_units, bi_units
from modules.network import (size_units,
                             bandwidth_units,
                             time_calc,
                             format_time,
                             size_calc,
                             bandwidth_calc)
from modules.subnetting import (
                                calculate_subnet,
                                ip_to_int,
                                cidr_to_mask
                                )


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

        network_subnb = ttk.Notebook(network_tab)
        network_subnb.pack(expand=True, fill="both", padx=5, pady=5)

        timecalc_tab = ttk.Frame(network_subnb)
        network_subnb.add(timecalc_tab, text="Time calculation")

        size_tab = ttk.Frame(network_subnb)
        network_subnb.add(size_tab, text="Size calculation")

        bandwidth_tab = ttk.Frame(network_subnb)
        network_subnb.add(bandwidth_tab, text="Bandwidth calculation")

        NumbersTab(numbers_tab)
        StorageTab(storage_tab)
        TimeCalcTab(timecalc_tab)
        SizeCalcTab(size_tab)
        BandwidthCalcTab(bandwidth_tab)
        SubnetCalcTab(subnet_tab)


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
        self.base_combo = ttk.Combobox(parent, values=[
            "2",
            "8",
            "16"
        ]
                                       )
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
        self.result_label.config(text=f"Result: {result}{to_factor}")


class TimeCalcTab:
    def __init__(self, parent):
        """ Defines the structure of subtab timecalc_tab in network tab"""
        ttk.Label(parent, text="Value").grid(row=0, column=0)
        self.entry = ttk.Entry(parent)
        self.entry.grid(row=0, column=1)

        ttk.Label(parent, text="Size unit:").grid(row=1, column=0)
        self.size_unit = ttk.Combobox(parent, values=list(size_units.keys()))
        self.size_unit.grid(row=1, column=1)

        ttk.Label(parent, text="Bps value:").grid(row=2, column=0)
        self.bps_size = ttk.Entry(parent)
        self.bps_size.grid(row=2, column=1)

        ttk.Label(parent, text="Bandwidth unit:").grid(row=3, column=0)
        self.bandwidth_unit = ttk.Combobox(parent, values=list(bandwidth_units.keys()))
        self.bandwidth_unit.grid(row=3, column=1)

        ttk.Button(parent, text="Convert", command=self.time_click).grid(row=5, column=1)

        self.result_label = ttk.Label(parent, text="")
        self.result_label.grid(row=7, column=1)

    def time_click(self):
        """ Calls time function from time module """
        value = int(self.entry.get())
        value_unit = self.size_unit.get()
        bandwidth_size = int(self.bps_size.get())
        bandwidth_unit = self.bandwidth_unit.get()
        self.time_result = format_time(time_calc(
                                                 value,
                                                 value_unit,
                                                 bandwidth_size,
                                                 bandwidth_unit
                                                 )
                                       )
        self.result_label.config(text=f"={self.time_result}")


class SizeCalcTab:
    def __init__(self, parent):
        """ Defines the structure of subtab sizecalc_tab in network tab"""
        ttk.Label(parent, text="Time in seconds").grid(row=1, column=0)
        self.time_entry = ttk.Entry(parent)
        self.time_entry.grid(row=1, column=1)

        ttk.Label(parent, text="Bps:").grid(row=2, column=0)
        self.time_bps = ttk.Entry(parent)
        self.time_bps.grid(row=2, column=1)

        ttk.Label(parent, text="Bandwidth unit:").grid(row=3, column=0)
        self.time_bandwidth = ttk.Combobox(parent, values=list(bandwidth_units.keys()))
        self.time_bandwidth.grid(row=3, column=1)

        ttk.Button(parent, text="Convert", command=self.size_click).grid(row=5, column=1)

        self.result_label = ttk.Label(parent, text="")
        self.result_label.grid(row=7, column=1)


    def size_click(self):
        """ Calls size function from size module """
        value = int(self.time_entry.get())
        bandwidth_size = int(self.time_bps.get())
        bandwidth_unit = self.time_bandwidth.get()
        self.result_label.config(text=f"{size_calc(value, bandwidth_size, bandwidth_unit)} bits")


class BandwidthCalcTab:
    def __init__(self, parent):
        """ Defines the structure of subtab bandwidth_tab in network tab"""
        ttk.Label(parent, text="Value").grid(row=0, column=0)
        self.size_entry = ttk.Entry(parent)
        self.size_entry.grid(row=0, column=1)

        ttk.Label(parent, text="Value unit:").grid(row=1, column=0)
        self.size_unit = ttk.Combobox(parent, values=list(size_units.keys()))
        self.size_unit.grid(row=1, column=1)

        ttk.Label(parent, text="Time in seconds:").grid(row=2, column=0)
        self.time_entry = ttk.Entry(parent)
        self.time_entry.grid(row=2, column=1)

        ttk.Button(parent, text="Convert", command=self.bandwidth_click).grid(row=5, column=1)

        self.result_label = ttk.Label(parent, text="")
        self.result_label.grid(row=7, column=1)


    def bandwidth_click(self):
        """ Calls bandwidth function from time module """
        value = float(self.size_entry.get())
        value_unit = self.size_unit.get()
        time_input = float(self.time_entry.get())

        self.result_label.config(text=f"{bandwidth_calc(value, value_unit, time_input):.2f} bits per second")

class SubnetCalcTab:
    def __init__(self, parent):
        """ Defines the structure in network tab"""
        ttk.Label(parent, text="Ip address/CIDR:").grid(row=0, column=0)
        self.ip_address = ttk.Entry(parent)
        self.ip_address.grid(row=0, column=1)

        ttk.Button(parent, text="Convert", command=self.subnet_click).grid(row=1, column=1)

        self.ipresult_label = ttk.Label(parent, text="")
        self.ipresult_label.grid(row=2, column=1)
        self.broadcast_label = ttk.Label(parent, text="")
        self.broadcast_label.grid(row=3, column=1)
        self.subnetmask_label = ttk.Label(parent, text="")
        self.subnetmask_label.grid(row=4, column=1)
        self.hostbegin_label = ttk.Label(parent, text="")
        self.hostbegin_label.grid(row=5, column=1)
        self.hostend_label = ttk.Label(parent, text="")
        self.hostend_label.grid(row=6, column=1)
        self.hostamount_label = ttk.Label(parent, text="")
        self.hostamount_label.grid(row=7, column=1)


    def subnet_click(self):
        """ Calls subnet function from network tab """
        ip_input = self.ip_address.get()
        ip, prefix = ip_input.split("/")
        prefix = int(prefix)
        int_result = ip_to_int(ip)
        mask = cidr_to_mask(prefix)
        result = calculate_subnet(int_result, mask, prefix)

        self.ipresult_label.config(text=f"IP address: {result['network_address']}")
        self.broadcast_label.config(text=f"Broadcast address: {result['broadcast']}")
        self.subnetmask_label.config(text=f"Subnet mask: {result['subnet_mask']}")
        self.hostbegin_label.config(text=f"Host begin address: {result['host_begin']}")
        self.hostend_label.config(text=f"Host end address: {result['host_end']}")
        self.hostamount_label.config(text=f"Amount of hosts: {result['host_amount']}")



if __name__ == "__main__":
    app = App_window()
    app.mainloop()
