import tkinter as tk
from PIL import Image, ImageTk
from qr_code_generator import generate_qr_code


class VendingMachineApp:
    def __init__(self, root, products):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Vending Machine")
        self.root.configure(bg="#f2f2f2")
        self.products = products
        self.selected_product = None

        # Main layout frames
        self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
        self.left_frame.pack(side="left", fill="y")

        self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
        self.right_frame.pack(side="right", fill="y")

        self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.product_frame.pack()

        self.details_label = tk.Label(self.left_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"), bg="#f2f2f2")
        self.details_label.pack(pady=10)

        self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
        self.product_image_label.pack(pady=10)
        self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
        
        self.quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
        

        self.increase_button = tk.Button(self.left_frame, text="+", command=self.increase_quantity, font=("Arial", 16),
                                         bg="#4CAF50", fg="white", relief="solid", width=5)
        self.decrease_button = tk.Button(self.left_frame, text="-", command=self.decrease_quantity, font=("Arial", 16),
                                         bg="#4CAF50", fg="white", relief="solid", width=5)

        self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
                                        bg="#FF5722", fg="white", relief="solid", width=10)

        self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
                                     bg="#FF5722", fg="white", relief="solid", width=10)
        self.back_button.pack(side="bottom", pady=10)

        self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

        self.load_products()

    def load_products(self):
        for product in self.products:
            image_path = product["image"]
            product_img = Image.open(image_path).resize((150, 150))
            product_img_tk = ImageTk.PhotoImage(product_img)
            button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
                               command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
                               bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
            button.image = product_img_tk
            button.pack(side="left", padx=20, pady=20)

    def on_product_click(self, product):
        self.selected_product = product
        self.product_frame.pack_forget()
        self.details_label.config(text=f"Selected Product: {product['name']}")

        # Display product image
        product_img = Image.open(product["image"]).resize((200, 200))
        product_img_tk = ImageTk.PhotoImage(product_img)
        self.product_image_label.config(image=product_img_tk)
        self.product_image_label.image = product_img_tk

        # Display quantity and price
        self.price_label.pack(pady=10)
        
        self.quantity_label.config(text=f"Quantity: {product['quantity']}")
        self.price_label.config(text=f"Price: NRs {product['price'] * product['quantity']}")
        self.quantity_label.pack(pady=10)
        

        # Display + and - buttons
        self.increase_button.pack(side="left", padx=10, pady=10)
        self.decrease_button.pack(side="left", padx=10, pady=10)

        # Display "Buy Now" button
        self.buy_now_button.pack(pady=20)

    def go_back(self):
        self.product_frame.pack()
        self.details_label.config(text="Smart Vending Machine")
        self.product_image_label.config(image="")
        self.quantity_label.pack_forget()
        self.price_label.pack_forget()
        self.increase_button.pack_forget()
        self.decrease_button.pack_forget()
        self.buy_now_button.pack_forget()
        self.qr_code_label.config(image="")

    def increase_quantity(self):
        self.selected_product["quantity"] += 1
        self.update_details()

    def decrease_quantity(self):
        self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
        self.update_details()

    def update_details(self):
        self.quantity_label.config(text=f"Quantity: {self.selected_product['quantity']}")
        self.price_label.config(text=f"Price: NRs {self.selected_product['price'] * self.selected_product['quantity']}")

    def buy_now(self):
        qr_img = generate_qr_code(self.selected_product)
        qr_img_tk = ImageTk.PhotoImage(qr_img)
        self.qr_code_label.config(image=qr_img_tk)
        self.qr_code_label.image = qr_img_tk
        self.qr_code_label.pack(pady=20)
