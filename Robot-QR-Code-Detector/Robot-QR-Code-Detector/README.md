# Robot QR Code Detector

Robot Raspberry Pi piloté par QR codes (FORWARD, BACKWARD, LEFT, RIGHT, STOP).

| Fichier | Rôle |
|---|---|
| `robotfonctionel.py` | Programme principal : détecte les QR codes et commande le moteur (L298N) |
| `qr_detec.py` | Détection de QR codes avec tracé du contour |
| `qr_test.py` | Test de la caméra |
| `qr_creation.py` / `qr_.py` | Génération des QR codes de commande |
| `onemotormotion.py` | Test du moteur au clavier |

## Dépendances
`pip install opencv-python pyzbar qrcode RPi.GPIO`
