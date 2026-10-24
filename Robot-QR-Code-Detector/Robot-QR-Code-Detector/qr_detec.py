
#CODE DE DETECTION DE QR CODE 
import cv2
from pyzbar import pyzbar

# Ouvrir la caméra
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Erreur caméra")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Détection des QR codes
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # Afficher les données du QR
        print("QR détecté:", obj.data.decode("utf-8"))
        # Dessiner un rectangle autour du QR
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(points)
            points = list(map(tuple, hull))
        for i in range(len(points)):
            cv2.line(frame, points[i], points[(i+1) % len(points)], (0,255,0), 3)

    cv2.imshow("QR Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

