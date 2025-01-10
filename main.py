import tkinter as tk
from gui import VendingMachineApp
from product_data import products

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachineApp(root, products)
    root.mainloop()
