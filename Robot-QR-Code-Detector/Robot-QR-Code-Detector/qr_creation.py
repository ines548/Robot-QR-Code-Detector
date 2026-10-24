# qr_directions.py
import qrcode

# Exemple de direction
direction = "Gauche"  # change en "Droite" ou "Tout droit"

# Générer le QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(direction)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("direction_qr.png")

print("QR code généré ! Ouvre direction_qr.png pour le scanner.")