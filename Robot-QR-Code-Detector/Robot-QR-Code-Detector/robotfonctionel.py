import RPi.GPIO as GPIO
import cv2
from pyzbar.pyzbar import decode
from time import sleep

# === GPIO SETUP ===
in1 = 24
in2 = 23
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

p = GPIO.PWM(en, 1000)
p.start(50)  # vitesse moyenne

# === CAMERA SETUP ===
cap = cv2.VideoCapture(0)

print("QR Robot Ready 🚀")

# === FUNCTIONS ===
def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    print("Forward")

def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    print("Backward")

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    print("Stop")

def left():
    print("Left")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    sleep(0.5)
    stop()

def right():
    print("Right")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    sleep(0.5)
    stop()

# === MAIN LOOP ===
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        qr_codes = decode(frame)

        for qr in qr_codes:
            data = qr.data.decode('utf-8')
            print("QR Detected:", data)

            if data == "FORWARD":
                forward()

            elif data == "BACKWARD":
                backward()

            elif data == "LEFT":
                left()

            elif data == "RIGHT":
                right()

            elif data == "STOP":
                stop()

            sleep(1)  # éviter répétition rapide

        # affichage caméra (optionnel)
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    p.stop()
    GPIO.cleanup()
    print("Clean exit")