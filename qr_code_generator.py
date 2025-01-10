import qrcode
from PIL import Image

def generate_qr_code(product):
    data = f"Product: {product['name']}\nPrice: {product['price'] * product['quantity']}\nQuantity: {product['quantity']}"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white").resize((300, 300))
    return img
