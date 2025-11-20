import qrcode

data = input("Enter your URL or text:").strip()
filename = input("Enter the filename:").strip()
qr = qrcode.QRCode(box_size=10, border=3)
qr.add_data(data)
image = qr.make_image(fill_color="black",back_color="white")
image.save(filename)
print(f'Qrcode saved to {filename}')