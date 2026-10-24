import qrcode

commands = {
    "forward": "F",
    "backward": "B",
    "left": "L",
    "right": "R",
    "stop": "S"
}

for name, value in commands.items():
    img = qrcode.make(value)
    img.save(f"{name}.png")

print("QR codes générés !")