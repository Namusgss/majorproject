import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import os

# Sample product data
products = [
    {"name": "Drinks", "price": 60, "image": "images/coke.jpeg", "quantity": 1},
    {"name": "Noodles", "price": 25, "image": "images/waiwai.jpeg", "quantity": 1}
]

# Function to update quantity displayed and update the product's quantity
def update_quantity(product, change):
    # Update the quantity by adding or subtracting
    product["quantity"] = max(1, product["quantity"] + change)  # Prevent going below 1
    # Update the quantity and price labels
    quantity_label.config(text=f"Quantity: {product['quantity']}")
    price_label.config(text=f"Price: NRs {product['price'] * product['quantity']}")  # Update price based on quantity

# Function to generate the QR code with product details
def generate_qr_code(product):
    url = f"Product: {product['name']}\nPrice: {product['price'] * product['quantity']}\nQuantity: {product['quantity']}"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img = img.resize((300, 300))  # Resize for better visibility
    return img

# Function to display the product details when a product is selected
def on_product_click(product):
    global selected_product  # Keep track of the selected product
    selected_product = product  # Store the selected product

    # Hide the product selection screen and show the product details screen
    product_frame.pack_forget()  # Hide product buttons
    back_button.pack()  # Show the "Back" button

    # Load the selected product image
    product_image = Image.open(product["image"])
    product_image = product_image.resize((200, 200))  # Resize image for display
    product_img_tk = ImageTk.PhotoImage(product_image)

    # Update the display with the selected product details (name and image)
    product_image_label.config(image=product_img_tk)
    product_image_label.image = product_img_tk  # Keep reference to avoid garbage collection
    details_label.config(text=f"Selected Product: {product['name']}")

    # Update the quantity and price labels (shown after selecting the product)
    quantity_label.config(text=f"Quantity: {product['quantity']}")
    price_label.config(text=f"Price: NRs{product['price'] * product['quantity']}")

    # Show the quantity buttons (+ and -)
    increase_button.pack(side="left", padx=20, pady=20)
    decrease_button.pack(side="right", padx=20, pady=20)

    # Show the price and quantity labels
    quantity_label.pack(pady=10)
    price_label.pack(pady=10)

    # Show the "Buy Now" button
    buy_now_button.pack(pady=20)

# Function to go back to the product selection screen
def go_back():
    # Hide the details and show the product selection screen
    product_image_label.config(image='')  # Clear product image
    details_label.config(text="Select a product")  # Reset details label
    quantity_label.config(text="")  # Clear quantity label
    price_label.config(text="")  # Clear price label
    increase_button.pack_forget()  # Hide the increase button
    decrease_button.pack_forget()  # Hide the decrease button
    buy_now_button.pack_forget()  # Hide the "Buy Now" button
    back_button.pack_forget()  # Hide the back button

    # Show the product selection screen again
    product_frame.pack()  # Show product buttons
    qr_frame.pack_forget()  # Hide the QR code screen

# Function to handle the "Buy Now" button click
def buy_now(product):
    # Generate the QR code based on the updated price
    qr_img = generate_qr_code(product)

    # Hide the product details screen and show the QR code screen
    product_frame.pack_forget()  # Hide product selection screen
    back_button.pack()  # Show the "Back" button

    # Create label with "Scan to Pay" text
    scan_label = tk.Label(qr_frame, text="Scan to Pay", font=("Arial", 16), bg="#f2f2f2")
    scan_label.pack(pady=10)

    # Convert the QR image to Tkinter format
    qr_img_tk = ImageTk.PhotoImage(qr_img)

    # Create a label to display the QR code
    qr_code_label.config(image=qr_img_tk)
    qr_code_label.image = qr_img_tk  # Keep reference to avoid garbage collection
    qr_code_label.pack(pady=20)

    # Show the QR code frame
    qr_frame.pack()

# Initialize Tkinter window
root = tk.Tk()
root.geometry("800x600")
root.title("Vending Machine")
root.configure(bg="#f2f2f2")  # Light gray background for better visibility

# Label to show the product details (name and price)
details_label = tk.Label(root, text="Select a product", font=("Helvetica", 18, "bold"), bg="#f2f2f2")
details_label.pack(pady=20)

# Frame to hold product images (buttons) and names
product_frame = tk.Frame(root, bg="#f2f2f2")
product_frame.pack()

# Label to display the selected product's image after selection
product_image_label = tk.Label(root, bg="#f2f2f2")
product_image_label.pack(pady=10)

# Label to show the selected product details (price and quantity)
quantity_label = tk.Label(root, text="", font=("Arial", 16), bg="#f2f2f2")
price_label = tk.Label(root, text="", font=("Arial", 16), bg="#f2f2f2")

# Buttons to increase and decrease the quantity
increase_button = tk.Button(root, text="+", command=lambda: update_quantity(selected_product, 1), font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)
decrease_button = tk.Button(root, text="-", command=lambda: update_quantity(selected_product, -1), font=("Arial", 16), bg="#4CAF50", fg="white", relief="solid", width=5)

# "Buy Now" button to generate the QR code for the selected product
buy_now_button = tk.Button(root, text="Buy Now", command=lambda: buy_now(selected_product), font=("Arial", 16), bg="#FF5722", fg="white", relief="solid", width=10)

# Back button to go back to the product selection screen
back_button = tk.Button(root, text="Back", command=go_back, font=("Arial", 14), bg="#FF5722", fg="white", relief="solid", width=10)
back_button.pack_forget()  # Hide it initially

# Frame for QR code generation
qr_frame = tk.Frame(root, bg="#f2f2f2")
qr_code_label = tk.Label(qr_frame, bg="#f2f2f2")

# Loop through products and display images with names only (no price)
for product in products:
    # Check if image exists
    if os.path.exists(product["image"]):
        # Load the product image
        product_image = Image.open(product["image"])
        product_image = product_image.resize((150, 150))  # Resize image for display
        product_img_tk = ImageTk.PhotoImage(product_image)

        # Create a button for each product image along with name only
        product_button = tk.Button(product_frame, image=product_img_tk, text=f"{product['name']}",
                                   compound="top", command=lambda p=product: on_product_click(p), font=("Arial", 12), bg="#4CAF50", fg="white", relief="solid", padx=20, pady=10)
        product_button.image = product_img_tk  # Keep reference to image
        product_button.grid(row=0, column=products.index(product), padx=20, pady=20)
    else:
        print(f"Image not found for {product['name']}")

# Start the Tkinter main loop
root.mainloop()
