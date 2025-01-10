
# # # # # # # import tkinter as tk
# # # # # # # from PIL import Image, ImageTk
# # # # # # # from qr_code_generator import generate_qr_code


# # # # # # # class VendingMachineApp:
# # # # # # #     def __init__(self, root, products):
# # # # # # #         self.root = root
# # # # # # #         self.root.geometry("800x600")
# # # # # # #         self.root.title("Vending Machine")
# # # # # # #         self.root.configure(bg="#f2f2f2")
# # # # # # #         self.products = products
# # # # # # #         self.selected_product = None

# # # # # # #         # Main layout frames
# # # # # # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # # #         self.left_frame.pack(side="left", fill="y")

# # # # # # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # # #         self.right_frame.pack(side="right", fill="y")

# # # # # # #         # Separate frame for the title label
# # # # # # #         self.label_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # # #         self.label_frame.pack(side="top", fill="x")

# # # # # # #         self.details_label = tk.Label(self.label_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"), bg="#f2f2f2")
# # # # # # #         self.details_label.pack(pady=10)

# # # # # # #         # Separate frame for product buttons
# # # # # # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # # # # # #         # Product details section
# # # # # # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # # # # # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")
# # # # # # #         self.quantity_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # # # # # #         self.increase_button = tk.Button(self.left_frame, text="+", command=self.increase_quantity, font=("Arial", 16),
# # # # # # #                                          bg="#4CAF50", fg="white", relief="solid", width=5)
# # # # # # #         self.decrease_button = tk.Button(self.left_frame, text="-", command=self.decrease_quantity, font=("Arial", 16),
# # # # # # #                                          bg="#4CAF50", fg="white", relief="solid", width=5)

# # # # # # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # # # # # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # # # # # #                                      bg="#FF5722", fg="white", relief="solid", width=10)
# # # # # # #         self.back_button.pack(side="bottom", pady=10)

# # # # # # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # # # # # #         self.load_products()

# # # # # # #     def load_products(self):
# # # # # # #         for product in self.products:
# # # # # # #             image_path = product["image"]
# # # # # # #             product_img = Image.open(image_path).resize((150, 150))
# # # # # # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # # #             button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
# # # # # # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # # # # # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # # # # # #             button.image = product_img_tk
# # # # # # #             button.pack(side="left", padx=20, pady=20)

# # # # # # #     def on_product_click(self, product):
# # # # # # #         self.selected_product = product
# # # # # # #         self.product_frame.pack_forget()
# # # # # # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # # # # # #         # Display product image
# # # # # # #         product_img = Image.open(product["image"]).resize((200, 200))
# # # # # # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # # #         self.product_image_label.config(image=product_img_tk)
# # # # # # #         self.product_image_label.image = product_img_tk
# # # # # # #         self.product_image_label.pack(pady=10)

# # # # # # #         # Display quantity and price
# # # # # # #         self.price_label.pack(pady=10)
# # # # # # #         self.quantity_label.config(text=f"Quantity: {product['quantity']}")
# # # # # # #         self.price_label.config(text=f"Price: NRs {product['price'] * product['quantity']}")
# # # # # # #         self.quantity_label.pack(pady=10)

# # # # # # #         # Display + and - buttons
# # # # # # #         self.increase_button.pack(side="left", padx=10, pady=10)
# # # # # # #         self.decrease_button.pack(side="left", padx=10, pady=10)

# # # # # # #         # Display "Buy Now" button
# # # # # # #         self.buy_now_button.pack(pady=20)

# # # # # # #     def go_back(self):
# # # # # # #         self.product_frame.pack()
# # # # # # #         self.details_label.config(text="Smart Vending Machine")
# # # # # # #         self.product_image_label.pack_forget()
# # # # # # #         self.quantity_label.pack_forget()
# # # # # # #         self.price_label.pack_forget()
# # # # # # #         self.increase_button.pack_forget()
# # # # # # #         self.decrease_button.pack_forget()
# # # # # # #         self.buy_now_button.pack_forget()
# # # # # # #         self.qr_code_label.config(image="")

# # # # # # #     def increase_quantity(self):
# # # # # # #         self.selected_product["quantity"] += 1
# # # # # # #         self.update_details()

# # # # # # #     def decrease_quantity(self):
# # # # # # #         self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # # # # # #         self.update_details()

# # # # # # #     def update_details(self):
# # # # # # #         self.quantity_label.config(text=f"Quantity: {self.selected_product['quantity']}")
# # # # # # #         self.price_label.config(text=f"Price: NRs {self.selected_product['price'] * self.selected_product['quantity']}")

# # # # # # #     def buy_now(self):
# # # # # # #         qr_img = generate_qr_code(self.selected_product)
# # # # # # #         qr_img_tk = ImageTk.PhotoImage(qr_img)
# # # # # # #         self.qr_code_label.config(image=qr_img_tk)
# # # # # # #         self.qr_code_label.image = qr_img_tk
# # # # # # #         self.qr_code_label.pack(pady=20)





# # # # # # # # import tkinter as tk
# # # # # # # # from PIL import Image, ImageTk
# # # # # # # # from qr_code_generator import generate_qr_code


# # # # # # # # class VendingMachineApp:
# # # # # # # #     def __init__(self, root, products):
# # # # # # # #         self.root = root
# # # # # # # #         self.root.geometry("800x600")
# # # # # # # #         self.root.title("Vending Machine")
# # # # # # # #         self.root.configure(bg="#f2f2f2")
# # # # # # # #         self.products = products
# # # # # # # #         self.selected_product = None

# # # # # # # #         # Main layout frames
# # # # # # # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # # # #         self.left_frame.pack(side="left", fill="y")

# # # # # # # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # # # #         self.right_frame.pack(side="right", fill="y")

# # # # # # # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # # # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # # # # # # #         self.details_label = tk.Label(self.left_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # # # # # # #                                       bg="#f2f2f2")
# # # # # # # #         self.details_label.pack(pady=10)

# # # # # # # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # # # # # # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # # # # # # #         # Buttons and quantity frame
# # # # # # # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # # # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # # # # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # # # # # # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # # # # # # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # # # # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # # # # # # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # # # # # # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # # # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # # # # # # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # # # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # # # # # # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # # # # # # #         self.load_products()

# # # # # # # #     def load_products(self):
# # # # # # # #         for product in self.products:
# # # # # # # #             image_path = product["image"]
# # # # # # # #             product_img = Image.open(image_path).resize((150, 150))
# # # # # # # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # # # #             button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
# # # # # # # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # # # # # # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # # # # # # #             button.image = product_img_tk
# # # # # # # #             button.pack(side="left", padx=20, pady=20)

# # # # # # # #     def on_product_click(self, product):
# # # # # # # #         self.selected_product = product
# # # # # # # #         self.product_frame.pack_forget()
# # # # # # # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # # # # # # #         # Display product image
# # # # # # # #         product_img = Image.open(product["image"]).resize((200, 200))
# # # # # # # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # # # #         self.product_image_label.config(image=product_img_tk)
# # # # # # # #         self.product_image_label.image = product_img_tk
# # # # # # # #         self.product_image_label.pack(pady=10)

# # # # # # # #         # Display price
# # # # # # # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # # # # # # #         self.price_label.pack(pady=10)

# # # # # # # #         # Display quantity frame
# # # # # # # #         self.quantity_label.config(text=f"{product['quantity']}")
# # # # # # # #         self.quantity_frame.pack(pady=10)
# # # # # # # #         self.increase_button.pack(side="left", padx=10)
# # # # # # # #         self.quantity_label.pack(side="left", padx=10)
# # # # # # # #         self.decrease_button.pack(side="left", padx=10)

# # # # # # # #         # Display "Buy Now" button
# # # # # # # #         self.buy_now_button.pack(pady=20)

# # # # # # # #         # Show Back button
# # # # # # # #         self.back_button.pack(side="bottom", pady=10)

# # # # # # # #     def go_back(self):
# # # # # # # #         self.product_frame.pack()
# # # # # # # #         self.details_label.config(text="Smart Vending Machine")
# # # # # # # #         self.product_image_label.pack_forget()
# # # # # # # #         self.price_label.pack_forget()
# # # # # # # #         self.quantity_frame.pack_forget()
# # # # # # # #         self.buy_now_button.pack_forget()
# # # # # # # #         self.qr_code_label.config(image="")
# # # # # # # #         self.scan_label.pack_forget()

# # # # # # # #         # Hide Back button
# # # # # # # #         self.back_button.pack_forget()

# # # # # # # #     def increase_quantity(self):
# # # # # # # #         self.selected_product["quantity"] += 1
# # # # # # # #         self.update_details()

# # # # # # # #     def decrease_quantity(self):
# # # # # # # #         self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # # # # # # #         self.update_details()

# # # # # # # #     def update_details(self):
# # # # # # # #         self.quantity_label.config(text=f"{self.selected_product['quantity']}")

# # # # # # # #     def buy_now(self):
# # # # # # # #         qr_img = generate_qr_code(self.selected_product)
# # # # # # # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # # # # # # #         # Show "Scan to Pay" label and QR code
# # # # # # # #         self.scan_label.pack(pady=10)
# # # # # # # #         self.qr_code_label.config(image=qr_img_tk)
# # # # # # # #         self.qr_code_label.image = qr_img_tk
# # # # # # # #         self.qr_code_label.pack(pady=20)


# # # # # # # # # # Example product list
# # # # # # # # # products = [
# # # # # # # # #     {"name": "Drinks", "image": "coca_cola.jpg", "price": 60, "quantity": 1},
# # # # # # # # #     {"name": "Chips", "image": "lays.jpg", "price": 100, "quantity": 1},
# # # # # # # # #     {"name": "Candy", "image": "candy.jpg", "price": 50, "quantity": 1},
# # # # # # # # # ]

# # # # # # # # # # Start the app
# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     root = tk.Tk()
# # # # # # # # #     app = VendingMachineApp(root, products)
# # # # # # # # #     root.mainloop()


# # # # # # import tkinter as tk
# # # # # # from PIL import Image, ImageTk
# # # # # # from qr_code_generator import generate_qr_code


# # # # # # class VendingMachineApp:
# # # # # #     def __init__(self, root, products):
# # # # # #         self.root = root
# # # # # #         self.root.geometry("800x600")
# # # # # #         self.root.title("Vending Machine")
# # # # # #         self.root.configure(bg="#f2f2f2")
# # # # # #         self.products = products
# # # # # #         self.selected_product = None

# # # # # #         # Main layout frames
# # # # # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # #         self.left_frame.pack(side="left", fill="y")

# # # # # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # #         self.right_frame.pack(side="right", fill="y")

# # # # # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # # # # #         self.details_label = tk.Label(self.left_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # # # # #                                       bg="#f2f2f2")
# # # # # #         self.details_label.pack(pady=10)

# # # # # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # # # # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # # # # #         # Buttons and quantity frame
# # # # # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # # # # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # # # # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # # # # #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
# # # # # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # # # # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # # # # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # # # # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # # # # #         self.load_products()

# # # # # #     def load_products(self):
# # # # # #         for product in self.products:
# # # # # #             image_path = product["image"]
# # # # # #             product_img = Image.open(image_path).resize((150, 150))
# # # # # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # #             button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
# # # # # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # # # # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # # # # #             button.image = product_img_tk
# # # # # #             button.pack(side="left", padx=20, pady=20)

# # # # # #     def on_product_click(self, product):
# # # # # #         self.selected_product = product
# # # # # #         self.product_frame.pack_forget()
# # # # # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # # # # #         # Display product image
# # # # # #         product_img = Image.open(product["image"]).resize((200, 200))
# # # # # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # #         self.product_image_label.config(image=product_img_tk)
# # # # # #         self.product_image_label.image = product_img_tk
# # # # # #         self.product_image_label.pack(pady=10)

# # # # # #         # Display price
# # # # # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # # # # #         self.price_label.pack(pady=10)

# # # # # #         # Display quantity frame
# # # # # #         self.quantity_label.config(text=f"{product['quantity']}")
# # # # # #         self.quantity_frame.pack(pady=10)
# # # # # #         self.increase_button.pack(side="left", padx=10)
# # # # # #         self.quantity_label.pack(side="left", padx=10)
# # # # # #         self.decrease_button.pack(side="left", padx=10)

# # # # # #         # Display payable amount
# # # # # #         self.update_details()

# # # # # #         # Display "Buy Now" button
# # # # # #         self.buy_now_button.pack(pady=20)

# # # # # #         # Show Back button
# # # # # #         self.back_button.pack(side="bottom", pady=10)

# # # # # #     def go_back(self):
# # # # # #         self.product_frame.pack()
# # # # # #         self.details_label.config(text="Smart Vending Machine")
# # # # # #         self.product_image_label.pack_forget()
# # # # # #         self.price_label.pack_forget()
# # # # # #         self.quantity_frame.pack_forget()
# # # # # #         self.payable_label.pack_forget()
# # # # # #         self.buy_now_button.pack_forget()
# # # # # #         self.qr_code_label.config(image="")
# # # # # #         self.scan_label.pack_forget()

# # # # # #         # Hide Back button
# # # # # #         self.back_button.pack_forget()

# # # # # #     def increase_quantity(self):
# # # # # #         self.selected_product["quantity"] += 1
# # # # # #         self.update_details()

# # # # # #     def decrease_quantity(self):
# # # # # #         self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # # # # #         self.update_details()

# # # # # #     def update_details(self):
# # # # # #         quantity = self.selected_product["quantity"]
# # # # # #         price = self.selected_product["price"]
# # # # # #         total = price * quantity
# # # # # #         self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# # # # # #         self.payable_label.pack(pady=10)

# # # # # #     def buy_now(self):
# # # # # #         qr_img = generate_qr_code(self.selected_product)
# # # # # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # # # # #         # Show "Scan to Pay" label and QR code
# # # # # #         self.scan_label.pack(pady=10)
# # # # # #         self.qr_code_label.config(image=qr_img_tk)
# # # # # #         self.qr_code_label.image = qr_img_tk
# # # # # #         self.qr_code_label.pack(pady=20)



# # # # # # import tkinter as tk
# # # # # # from PIL import Image, ImageTk
# # # # # # from qr_code_generator import generate_qr_code


# # # # # # class VendingMachineApp:
# # # # # #     def __init__(self, root, products):
# # # # # #         self.root = root
# # # # # #         self.root.geometry("800x600")
# # # # # #         self.root.title("Vending Machine")
# # # # # #         self.root.configure(bg="#f2f2f2")
# # # # # #         self.products = products
# # # # # #         self.selected_product = None

# # # # # #         # Main layout frames
# # # # # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # #         self.left_frame.pack(side="left", fill="y")

# # # # # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # # #         self.right_frame.pack(side="right", fill="y")

# # # # # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # # # # #         self.details_label = tk.Label(self.left_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # # # # #                                       bg="#f2f2f2")
# # # # # #         self.details_label.pack(pady=10)

# # # # # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # # # # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # # # # #         # Buttons and quantity frame
# # # # # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # # # # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # # # # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # # # # #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
# # # # # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # # # # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # # # # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # # # # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # # # # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # # # # #         self.load_products()

# # # # # #     def load_products(self):
# # # # # #         for product in self.products:
# # # # # #             image_path = product["image"]
# # # # # #             product_img = Image.open(image_path).resize((150, 150))
# # # # # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # #             button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
# # # # # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # # # # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # # # # #             button.image = product_img_tk
# # # # # #             button.pack(side="left", padx=20, pady=20)

# # # # # #     def on_product_click(self, product):
# # # # # #         self.selected_product = product
# # # # # #         self.product_frame.pack_forget()
# # # # # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # # # # #         # Display product image
# # # # # #         product_img = Image.open(product["image"]).resize((200, 200))
# # # # # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # # # # #         self.product_image_label.config(image=product_img_tk)
# # # # # #         self.product_image_label.image = product_img_tk
# # # # # #         self.product_image_label.pack(pady=10)

# # # # # #         # Display price
# # # # # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # # # # #         self.price_label.pack(pady=10)

# # # # # #         # Display quantity frame
# # # # # #         self.quantity_label.config(text=f"{product['quantity']}")
# # # # # #         self.quantity_frame.pack(pady=10)
# # # # # #         self.increase_button.pack(side="left", padx=10)
# # # # # #         self.quantity_label.pack(side="left", padx=10)
# # # # # #         self.decrease_button.pack(side="left", padx=10)

# # # # # #         # Display payable amount
# # # # # #         self.update_details()

# # # # # #         # Display "Buy Now" button
# # # # # #         self.buy_now_button.pack(pady=20)

# # # # # #         # Show Back button
# # # # # #         self.back_button.pack(side="bottom", pady=10)

# # # # # #     def go_back(self):
# # # # # #         self.product_frame.pack()
# # # # # #         self.details_label.config(text="Smart Vending Machine")
# # # # # #         self.product_image_label.pack_forget()
# # # # # #         self.price_label.pack_forget()
# # # # # #         self.quantity_frame.pack_forget()
# # # # # #         self.payable_label.pack_forget()
# # # # # #         self.buy_now_button.pack_forget()
# # # # # #         self.qr_code_label.config(image="")
# # # # # #         self.scan_label.pack_forget()

# # # # # #         # Hide Back button
# # # # # #         self.back_button.pack_forget()

# # # # # #     def increase_quantity(self):
# # # # # #         if self.selected_product:  # Ensure a product is selected
# # # # # #             self.selected_product["quantity"] += 1
# # # # # #             self.update_details()

# # # # # #     def decrease_quantity(self):
# # # # # #         if self.selected_product:  # Ensure a product is selected
# # # # # #             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # # # # #             self.update_details()

# # # # # #     def update_details(self):
# # # # # #         if self.selected_product:  # Ensure a product is selected
# # # # # #             quantity = self.selected_product["quantity"]
# # # # # #             price = self.selected_product["price"]
# # # # # #             total = price * quantity
# # # # # #             self.quantity_label.config(text=f"{quantity}")
# # # # # #             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# # # # # #             self.payable_label.pack(pady=10)

# # # # # #     def buy_now(self):
# # # # # #         qr_img = generate_qr_code(self.selected_product)
# # # # # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # # # # #         # Show "Scan to Pay" label and QR code
# # # # # #         self.scan_label.pack(pady=10)
# # # # # #         self.qr_code_label.config(image=qr_img_tk)
# # # # # #         self.qr_code_label.image = qr_img_tk
# # # # # #         self.qr_code_label.pack(pady=20)

# # # # # import tkinter as tk
# # # # # from PIL import Image, ImageTk
# # # # # from qr_code_generator import generate_qr_code


# # # # # class VendingMachineApp:
# # # # #     def __init__(self, root, products):
# # # # #         self.root = root
# # # # #         self.root.geometry("800x600")
# # # # #         self.root.title("Vending Machine")
# # # # #         self.root.configure(bg="#f2f2f2")
# # # # #         self.products = products
# # # # #         self.selected_product = None

# # # # #         # Main layout frames
# # # # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # #         self.left_frame.pack(side="left", fill="both", expand=True)

# # # # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # # #         self.right_frame.pack(side="right", fill="both", expand=True)

# # # # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # # # #         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # # # #                                        bg="#f2f2f2")
        
# # # # #         self.details_label = tk.Label(self.left_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # # # #                                        bg="#f2f2f2")
# # # # #         self.details_label.pack(pady=10)

# # # # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # # # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # # # #         # Buttons and quantity frame
# # # # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # # # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # # # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # # # #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
# # # # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # # # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # # # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # # # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # # # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # # # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # # # #         self.load_products()

# # # # #     def load_products(self):
# # # # #         for product in self.products:
# # # # #             image_path = product["image"]
# # # # #             product_img = Image.open(image_path).resize((150, 150))
# # # # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # # # #             button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
# # # # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # # # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # # # #             button.image = product_img_tk
# # # # #             button.pack(side="left", padx=20, pady=20)

# # # # #     def on_product_click(self, product):
# # # # #         self.selected_product = product
# # # # #         self.product_frame.pack_forget()
# # # # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # # # #         # Display product image
# # # # #         product_img = Image.open(product["image"]).resize((200, 200))
# # # # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # # # #         self.product_image_label.config(image=product_img_tk)
# # # # #         self.product_image_label.image = product_img_tk
# # # # #         self.product_image_label.pack(pady=10)

# # # # #         # Display price
# # # # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # # # #         self.price_label.pack(pady=10)

# # # # #         # Display quantity frame
# # # # #         self.quantity_label.config(text=f"{product['quantity']}")
# # # # #         self.quantity_frame.pack(pady=10)
# # # # #         self.increase_button.pack(side="left", padx=10)
# # # # #         self.quantity_label.pack(side="left", padx=10)
# # # # #         self.decrease_button.pack(side="left", padx=10)

# # # # #         # Display payable amount
# # # # #         self.update_details()

# # # # #         # Display "Buy Now" button
# # # # #         self.buy_now_button.pack(pady=20)

# # # # #         # Show Back button
# # # # #         self.back_button.pack(side="bottom", pady=10)

# # # # #     def go_back(self):
# # # # #         self.product_frame.pack()
# # # # #         self.details_label.config(text="Smart Vending Machine")
# # # # #         self.product_image_label.pack_forget()
# # # # #         self.price_label.pack_forget()
# # # # #         self.quantity_frame.pack_forget()
# # # # #         self.payable_label.pack_forget()
# # # # #         self.buy_now_button.pack_forget()
# # # # #         self.qr_code_label.config(image="")
# # # # #         self.scan_label.pack_forget()

# # # # #         # Hide Back button
# # # # #         self.back_button.pack_forget()

# # # # #     def increase_quantity(self):
# # # # #         if self.selected_product:  # Ensure a product is selected
# # # # #             self.selected_product["quantity"] += 1
# # # # #             self.update_details()

# # # # #     def decrease_quantity(self):
# # # # #         if self.selected_product:  # Ensure a product is selected
# # # # #             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # # # #             self.update_details()

# # # # #     def update_details(self):
# # # # #         if self.selected_product:  # Ensure a product is selected
# # # # #             quantity = self.selected_product["quantity"]
# # # # #             price = self.selected_product["price"]
# # # # #             total = price * quantity
# # # # #             self.quantity_label.config(text=f"{quantity}")
# # # # #             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# # # # #             self.payable_label.pack(pady=10)

# # # # #     def buy_now(self):
# # # # #         qr_img = generate_qr_code(self.selected_product)
# # # # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # # # #         # Show "Scan to Pay" label and QR code
# # # # #         self.scan_label.pack(pady=10)
# # # # #         self.qr_code_label.config(image=qr_img_tk)
# # # # #         self.qr_code_label.image = qr_img_tk
# # # # #         self.qr_code_label.pack(pady=20)

# # # # import tkinter as tk
# # # # from PIL import Image, ImageTk
# # # # from qr_code_generator import generate_qr_code


# # # # class VendingMachineApp:
# # # #     def __init__(self, root, products):
# # # #         self.root = root
# # # #         self.root.geometry("800x600")
# # # #         self.root.title("Vending Machine")
# # # #         self.root.configure(bg="#f2f2f2")
# # # #         self.products = products
# # # #         self.selected_product = None

# # # #         # Main layout frames
# # # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # #         self.left_frame.pack(side="left", fill="y")

# # # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # # #         self.right_frame.pack(side="right", fill="y")

# # # #         # Initialize top_frame
# # # #         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # #         self.top_frame.pack(side="top", fill="both", expand=True)

# # # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # # #         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # # #                                       bg="#f2f2f2")
# # # #         self.details_label.pack(pady=10)

# # # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # # #         # Buttons and quantity frame
# # # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # # #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
# # # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # # #         self.load_products()

# # # #     def load_products(self):
# # # #         for product in self.products:
# # # #             image_path = product["image"]
# # # #             product_img = Image.open(image_path).resize((150, 150))
# # # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # # #             button = tk.Button(self.product_frame, image=product_img_tk, text=product['name'], compound="top",
# # # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # # #             button.image = product_img_tk
# # # #             button.pack(side="left", padx=20, pady=20)

# # # #     def on_product_click(self, product):
# # # #         self.selected_product = product
# # # #         self.product_frame.pack_forget()
# # # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # # #         # Display product image
# # # #         product_img = Image.open(product["image"]).resize((200, 200))
# # # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # # #         self.product_image_label.config(image=product_img_tk)
# # # #         self.product_image_label.image = product_img_tk
# # # #         self.product_image_label.pack(pady=10)

# # # #         # Display price
# # # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # # #         self.price_label.pack(pady=10)

# # # #         # Display quantity frame
# # # #         self.quantity_label.config(text=f"{product['quantity']}")
# # # #         self.quantity_frame.pack(pady=10)
# # # #         self.increase_button.pack(side="left", padx=10)
# # # #         self.quantity_label.pack(side="left", padx=10)
# # # #         self.decrease_button.pack(side="left", padx=10)

# # # #         # Display payable amount
# # # #         self.update_details()

# # # #         # Display "Buy Now" button
# # # #         self.buy_now_button.pack(pady=20)

# # # #         # Show Back button
# # # #         self.back_button.pack(side="bottom", pady=10)

# # # #     def go_back(self):
# # # #         self.product_frame.pack()
# # # #         self.details_label.config(text="Smart Vending Machine")
# # # #         self.product_image_label.pack_forget()
# # # #         self.price_label.pack_forget()
# # # #         self.quantity_frame.pack_forget()
# # # #         self.payable_label.pack_forget()
# # # #         self.buy_now_button.pack_forget()
# # # #         self.qr_code_label.config(image="")  # Clear QR code
# # # #         self.scan_label.pack_forget()

# # # #         # Hide Back button
# # # #         self.back_button.pack_forget()

# # # #     def increase_quantity(self):
# # # #         if self.selected_product:  # Ensure a product is selected
# # # #             self.selected_product["quantity"] += 1
# # # #             self.update_details()

# # # #     def decrease_quantity(self):
# # # #         if self.selected_product:  # Ensure a product is selected
# # # #             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # # #             self.update_details()

# # # #     def update_details(self):
# # # #         if self.selected_product:  # Ensure a product is selected
# # # #             quantity = self.selected_product["quantity"]
# # # #             price = self.selected_product["price"]
# # # #             total = price * quantity
# # # #             self.quantity_label.config(text=f"{quantity}")
# # # #             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# # # #             self.payable_label.pack(pady=10)

# # # #     def buy_now(self):
# # # #         qr_img = generate_qr_code(self.selected_product)
# # # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # # #         # Show "Scan to Pay" label and QR code
# # # #         self.scan_label.pack(pady=10)
# # # #         self.qr_code_label.config(image=qr_img_tk)
# # # #         self.qr_code_label.image = qr_img_tk
# # # #         self.qr_code_label.pack(pady=20)

# # # import tkinter as tk
# # # from PIL import Image, ImageTk
# # # from qr_code_generator import generate_qr_code


# # # class VendingMachineApp:
# # #     def __init__(self, root, products):
# # #         self.root = root
# # #         self.root.geometry("800x600")
# # #         self.root.title("Vending Machine")
# # #         self.root.configure(bg="#f2f2f2")
# # #         self.products = products
# # #         self.selected_product = None

# # #         # Main layout frames
# # #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # #         self.left_frame.pack(side="left", fill="y")

# # #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# # #         self.right_frame.pack(side="right", fill="y")

# # #         # Initialize top_frame and center the Smart Vending Machine label
# # #         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # #         self.top_frame.pack(side="top", fill="x")
# # #         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# # #                                       bg="#f2f2f2")
# # #         self.details_label.pack(pady=10, side="top")

# # #         # Create product frame in the center
# # #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # #         self.product_frame.pack(side="top", fill="both", expand=True)

# # #         # Container for centering the images
# # #         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
# # #         self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

# # #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# # #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# # #         # Buttons and quantity frame
# # #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# # #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# # #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# # #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# # #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# # #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
# # #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# # #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# # #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# # #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# # #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# # #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# # #         self.load_products()

# # #     def load_products(self):
# # #         for product in self.products:
# # #             image_path = product["image"]
# # #             product_img = Image.open(image_path).resize((150, 150))
# # #             product_img_tk = ImageTk.PhotoImage(product_img)
# # #             button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
# # #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# # #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# # #             button.image = product_img_tk
# # #             button.pack(side="left", padx=20, pady=20)

# # #     def on_product_click(self, product):
# # #         self.selected_product = product
# # #         self.product_frame.pack_forget()
# # #         self.details_label.config(text=f"Selected Product: {product['name']}")

# # #         # Display product image
# # #         product_img = Image.open(product["image"]).resize((200, 200))
# # #         product_img_tk = ImageTk.PhotoImage(product_img)
# # #         self.product_image_label.config(image=product_img_tk)
# # #         self.product_image_label.image = product_img_tk
# # #         self.product_image_label.pack(pady=10)

# # #         # Display price
# # #         self.price_label.config(text=f"Price: NRs {product['price']}")
# # #         self.price_label.pack(pady=10)

# # #         # Display quantity frame
# # #         self.quantity_label.config(text=f"{product['quantity']}")
# # #         self.quantity_frame.pack(pady=10)
# # #         self.increase_button.pack(side="left", padx=10)
# # #         self.quantity_label.pack(side="left", padx=10)
# # #         self.decrease_button.pack(side="left", padx=10)

# # #         # Display payable amount
# # #         self.update_details()

# # #         # Display "Buy Now" button
# # #         self.buy_now_button.pack(pady=20)

# # #         # Show Back button
# # #         self.back_button.pack(side="bottom", pady=10)

# # #     def go_back(self):
# # #         self.product_frame.pack()
# # #         self.details_label.config(text="Smart Vending Machine")
# # #         self.product_image_label.pack_forget()
# # #         self.price_label.pack_forget()
# # #         self.quantity_frame.pack_forget()
# # #         self.payable_label.pack_forget()
# # #         self.buy_now_button.pack_forget()
# # #         self.qr_code_label.config(image="")  # Clear QR code
# # #         self.scan_label.pack_forget()

# # #         # Hide Back button
# # #         self.back_button.pack_forget()

# # #     def increase_quantity(self):
# # #         if self.selected_product:  # Ensure a product is selected
# # #             self.selected_product["quantity"] += 1
# # #             self.update_details()

# # #     def decrease_quantity(self):
# # #         if self.selected_product:  # Ensure a product is selected
# # #             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# # #             self.update_details()

# # #     def update_details(self):
# # #         if self.selected_product:  # Ensure a product is selected
# # #             quantity = self.selected_product["quantity"]
# # #             price = self.selected_product["price"]
# # #             total = price * quantity
# # #             self.quantity_label.config(text=f"{quantity}")
# # #             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# # #             self.payable_label.pack(pady=10)

# # #     def buy_now(self):
# # #         qr_img = generate_qr_code(self.selected_product)
# # #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# # #         # Show "Scan to Pay" label and QR code
# # #         self.scan_label.pack(pady=10)
# # #         self.qr_code_label.config(image=qr_img_tk)
# # #         self.qr_code_label.image = qr_img_tk
# # #         self.qr_code_label.pack(pady=20)



# # import tkinter as tk
# # from PIL import Image, ImageTk
# # from qr_code_generator import generate_qr_code


# # class VendingMachineApp:
# #     def __init__(self, root, products):
# #         self.root = root
# #         self.root.geometry("800x600")
# #         self.root.title("Vending Machine")
# #         self.root.configure(bg="#f2f2f2")
# #         self.products = products
# #         self.selected_product = None

# #         # Main layout frames
# #         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# #         self.left_frame.pack(side="left", fill="y")

# #         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
# #         self.right_frame.pack(side="right", fill="y")

# #         # Top label for "Smart Vending Machine" at the top center
# #         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# #         self.top_frame.pack(side="top", fill="x")
# #         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
# #                                       bg="#f2f2f2")
# #         self.details_label.pack(pady=10, side="top")

# #         # Create product frame to hold product images
# #         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# #         self.product_frame.pack(side="top", fill="both", expand=True)

# #         # Container to center the images
# #         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
# #         self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

# #         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
# #         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

# #         # Buttons and quantity frame
# #         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
# #         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
# #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
# #         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
# #         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
# #                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# #         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
# #         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
# #                                         bg="#FF5722", fg="white", relief="solid", width=10)

# #         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
# #                                      bg="#FF5722", fg="white", relief="solid", width=10)

# #         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
# #         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

# #         self.load_products()

# #     def load_products(self):
# #         for product in self.products:
# #             image_path = product["image"]
# #             product_img = Image.open(image_path).resize((150, 150))
# #             product_img_tk = ImageTk.PhotoImage(product_img)
# #             button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
# #                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
# #                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
# #             button.image = product_img_tk
# #             button.pack(side="left", padx=20, pady=20)

# #     def on_product_click(self, product):
# #         self.selected_product = product
# #         self.product_frame.pack_forget()
# #         self.details_label.config(text=f"Selected Product: {product['name']}")

# #         # Display product image
# #         product_img = Image.open(product["image"]).resize((200, 200))
# #         product_img_tk = ImageTk.PhotoImage(product_img)
# #         self.product_image_label.config(image=product_img_tk)
# #         self.product_image_label.image = product_img_tk
# #         self.product_image_label.pack(pady=10)

# #         # Display price
# #         self.price_label.config(text=f"Price: NRs {product['price']}")
# #         self.price_label.pack(pady=10)

# #         # Display quantity frame
# #         self.quantity_label.config(text=f"{product['quantity']}")
# #         self.quantity_frame.pack(pady=10)
# #         self.increase_button.pack(side="left", padx=10)
# #         self.quantity_label.pack(side="left", padx=10)
# #         self.decrease_button.pack(side="left", padx=10)

# #         # Display payable amount
# #         self.update_details()

# #         # Display "Buy Now" button
# #         self.buy_now_button.pack(pady=20)

# #         # Show Back button
# #         self.back_button.pack(side="bottom", pady=10)

# #     def go_back(self):
# #         self.product_frame.pack()
# #         self.details_label.config(text="Smart Vending Machine")
# #         self.product_image_label.pack_forget()
# #         self.price_label.pack_forget()
# #         self.quantity_frame.pack_forget()
# #         self.payable_label.pack_forget()
# #         self.buy_now_button.pack_forget()
# #         self.qr_code_label.config(image="")  # Clear QR code
# #         self.scan_label.pack_forget()

# #         # Hide Back button
# #         self.back_button.pack_forget()

# #     def increase_quantity(self):
# #         if self.selected_product:  # Ensure a product is selected
# #             self.selected_product["quantity"] += 1
# #             self.update_details()

# #     def decrease_quantity(self):
# #         if self.selected_product:  # Ensure a product is selected
# #             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
# #             self.update_details()

# #     def update_details(self):
# #         if self.selected_product:  # Ensure a product is selected
# #             quantity = self.selected_product["quantity"]
# #             price = self.selected_product["price"]
# #             total = price * quantity
# #             self.quantity_label.config(text=f"{quantity}")
# #             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
# #             self.payable_label.pack(pady=10)

# #     def buy_now(self):
# #         qr_img = generate_qr_code(self.selected_product)
# #         qr_img_tk = ImageTk.PhotoImage(qr_img)

# #         # Show "Scan to Pay" label and QR code
# #         self.scan_label.pack(pady=10)
# #         self.qr_code_label.config(image=qr_img_tk)
# #         self.qr_code_label.image = qr_img_tk
# #         self.qr_code_label.pack(pady=20)


# import tkinter as tk
# from PIL import Image, ImageTk
# from qr_code_generator import generate_qr_code


# class VendingMachineApp:
#     def __init__(self, root, products):
#         self.root = root
#         self.root.geometry("800x600")
#         self.root.title("Vending Machine")
#         self.root.configure(bg="#f2f2f2")
#         self.products = products
#         self.selected_product = None

#         # Main layout frames
#         self.left_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.left_frame.pack(side="left", fill="y")

#         self.right_frame = tk.Frame(root, bg="#f2f2f2", width=400, height=600)
#         self.right_frame.pack(side="right", fill="y")

#         # Top label for "Smart Vending Machine" at the top center
#         self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.top_frame.pack(side="top", fill="x")
#         self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
#                                       bg="#f2f2f2")
#         self.details_label.pack(pady=10, side="top")

#         # Create product frame to hold product images
#         self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.product_frame.pack(side="top", fill="both", expand=True)

#         # Container to center the images
#         self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
#         self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

#         self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
#         self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

#         # Buttons and quantity frame
#         self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
#         self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
#                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
#         self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
#         self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
#                                          font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

#         self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
#         self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
#                                         bg="#FF5722", fg="white", relief="solid", width=10)

#         self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
#                                      bg="#FF5722", fg="white", relief="solid", width=10)

#         self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
#         self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

#         self.load_products()

#     def load_products(self):
#         for product in self.products:
#             image_path = product["image"]
#             product_img = Image.open(image_path).resize((150, 150))
#             product_img_tk = ImageTk.PhotoImage(product_img)
#             button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
#                                command=lambda p=product: self.on_product_click(p), font=("Arial", 12),
#                                bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
#             button.image = product_img_tk
#             button.pack(side="left", padx=20, pady=20)

#     def on_product_click(self, product):
#         self.selected_product = product
#         self.product_frame.pack_forget()
#         self.details_label.config(text=f"Selected Product: {product['name']}")

#         # Display product image
#         product_img = Image.open(product["image"]).resize((200, 200))
#         product_img_tk = ImageTk.PhotoImage(product_img)
#         self.product_image_label.config(image=product_img_tk)
#         self.product_image_label.image = product_img_tk
#         self.product_image_label.pack(pady=10)

#         # Display price
#         self.price_label.config(text=f"Price: NRs {product['price']}")
#         self.price_label.pack(pady=10)

#         # Display quantity frame
#         self.quantity_label.config(text=f"{product['quantity']}")
#         self.quantity_frame.pack(pady=10)
#         self.increase_button.pack(side="left", padx=10)
#         self.quantity_label.pack(side="left", padx=10)
#         self.decrease_button.pack(side="left", padx=10)

#         # Display payable amount
#         self.update_details()

#         # Display "Buy Now" button
#         self.buy_now_button.pack(pady=20)

#         # Show Back button
#         self.back_button.pack(side="bottom", pady=10)

#     def go_back(self):
#         self.product_frame.pack()
#         self.details_label.config(text="Smart Vending Machine")
#         self.product_image_label.pack_forget()
#         self.price_label.pack_forget()
#         self.quantity_frame.pack_forget()
#         self.payable_label.pack_forget()
#         self.buy_now_button.pack_forget()
#         self.qr_code_label.config(image="")  # Clear QR code
#         self.scan_label.pack_forget()

#         # Hide Back button
#         self.back_button.pack_forget()

#     def increase_quantity(self):
#         if self.selected_product:  # Ensure a product is selected
#             self.selected_product["quantity"] += 1
#             self.update_details()

#             # Hide the QR code if it exists
#             self.qr_code_label.pack_forget()
#             self.scan_label.pack_forget()

#     def decrease_quantity(self):
#         if self.selected_product:  # Ensure a product is selected
#             self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
#             self.update_details()

#             # Hide the QR code if it exists
#             self.qr_code_label.pack_forget()
#             self.scan_label.pack_forget()

#     def update_details(self):
#         if self.selected_product:  # Ensure a product is selected
#             quantity = self.selected_product["quantity"]
#             price = self.selected_product["price"]
#             total = price * quantity
#             self.quantity_label.config(text=f"{quantity}")
#             self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
#             self.payable_label.pack(pady=10)

#     def buy_now(self):
#         qr_img = generate_qr_code(self.selected_product)
#         qr_img_tk = ImageTk.PhotoImage(qr_img)

#         # Show "Scan to Pay" label and QR code
#         self.scan_label.pack(pady=10)
#         self.qr_code_label.config(image=qr_img_tk)
#         self.qr_code_label.image = qr_img_tk
#         self.qr_code_label.pack(pady=20)

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

        # Top label for "Smart Vending Machine" at the top center
        self.top_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.top_frame.pack(side="top", fill="x")
        self.details_label = tk.Label(self.top_frame, text="Smart Vending Machine", font=("Helvetica", 18, "bold"),
                                      bg="#f2f2f2")
        self.details_label.pack(pady=10, side="top")

        # Create product frame to hold product images
        self.product_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.product_frame.pack(side="top", fill="both", expand=True)

        # Container to center the images
        self.product_container = tk.Frame(self.product_frame, bg="#f2f2f2")
        self.product_container.pack(side="top", fill="x", padx=50)  # Padding to avoid tight edges

        self.product_image_label = tk.Label(self.left_frame, bg="#f2f2f2")
        self.price_label = tk.Label(self.left_frame, text="", font=("Arial", 16), bg="#f2f2f2")

        # Buttons and quantity frame
        self.quantity_frame = tk.Frame(self.left_frame, bg="#f2f2f2")
        self.increase_button = tk.Button(self.quantity_frame, text="+", command=self.increase_quantity,
                                         font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
        self.quantity_label = tk.Label(self.quantity_frame, text="1", font=("Arial", 16), bg="#f2f2f2")
        self.decrease_button = tk.Button(self.quantity_frame, text="-", command=self.decrease_quantity,
                                         font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

        self.payable_label = tk.Label(self.left_frame, text="Payable Amount: 60 * 1 = 60", font=("Arial", 14), bg="#f2f2f2")
        self.buy_now_button = tk.Button(self.left_frame, text="Buy Now", command=self.buy_now, font=("Arial", 16),
                                        bg="#FF5722", fg="white", relief="solid", width=10)

        self.back_button = tk.Button(root, text="Back", command=self.go_back, font=("Arial", 14),
                                     bg="#FF5722", fg="white", relief="solid", width=10)

        self.scan_label = tk.Label(self.right_frame, text="Scan to Pay", font=("Arial", 16, "bold"), bg="#f2f2f2")
        self.qr_code_label = tk.Label(self.right_frame, bg="#f2f2f2")

        # Add the "A Major Project" text and details below the images
        self.footer_label = tk.Label(self.product_frame, text="A Major Project by BEI077", font=("Arial", 12, "italic"),
                                     bg="#f2f2f2")
        self.footer_label.pack(pady=10)
        
        self.names_label = tk.Label(self.product_frame, text="Suman Bhandari\tACE077BEI037", 
                                    font=("Arial", 12), bg="#f2f2f2")
        self.names_label.pack(pady=5)

        self.load_products()

    def load_products(self):
        for product in self.products:
            image_path = product["image"]
            product_img = Image.open(image_path).resize((150, 150))
            product_img_tk = ImageTk.PhotoImage(product_img)
            button = tk.Button(self.product_container, image=product_img_tk, text=product['name'], compound="top",
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
        self.product_image_label.pack(pady=10)

        # Display price
        self.price_label.config(text=f"Price: NRs {product['price']}")
        self.price_label.pack(pady=10)

        # Display quantity frame
        self.quantity_label.config(text=f"{product['quantity']}")
        self.quantity_frame.pack(pady=10)
        self.increase_button.pack(side="left", padx=10)
        self.quantity_label.pack(side="left", padx=10)
        self.decrease_button.pack(side="left", padx=10)

        # Display payable amount
        self.update_details()

        # Display "Buy Now" button
        self.buy_now_button.pack(pady=20)

        # Show Back button
        self.back_button.pack(side="bottom", pady=10)

    def go_back(self):
        self.product_frame.pack()
        self.details_label.config(text="Smart Vending Machine")
        self.product_image_label.pack_forget()
        self.price_label.pack_forget()
        self.quantity_frame.pack_forget()
        self.payable_label.pack_forget()
        self.buy_now_button.pack_forget()
        self.qr_code_label.config(image="")  # Clear QR code
        self.scan_label.pack_forget()

        # Hide Back button
        self.back_button.pack_forget()

    def increase_quantity(self):
        if self.selected_product:  # Ensure a product is selected
            self.selected_product["quantity"] += 1
            self.update_details()

            # Hide the QR code if it exists
            self.qr_code_label.pack_forget()
            self.scan_label.pack_forget()

    def decrease_quantity(self):
        if self.selected_product:  # Ensure a product is selected
            self.selected_product["quantity"] = max(1, self.selected_product["quantity"] - 1)
            self.update_details()

            # Hide the QR code if it exists
            self.qr_code_label.pack_forget()
            self.scan_label.pack_forget()

    def update_details(self):
        if self.selected_product:  # Ensure a product is selected
            quantity = self.selected_product["quantity"]
            price = self.selected_product["price"]
            total = price * quantity
            self.quantity_label.config(text=f"{quantity}")
            self.payable_label.config(text=f"Payable Amount: {price} * {quantity} = {total}")
            self.payable_label.pack(pady=10)

    def buy_now(self):
        qr_img = generate_qr_code(self.selected_product)
        qr_img_tk = ImageTk.PhotoImage(qr_img)

        # Show "Scan to Pay" label and QR code
        self.scan_label.pack(pady=10)
        self.qr_code_label.config(image=qr_img_tk)
        self.qr_code_label.image = qr_img_tk
        self.qr_code_label.pack(pady=20)


