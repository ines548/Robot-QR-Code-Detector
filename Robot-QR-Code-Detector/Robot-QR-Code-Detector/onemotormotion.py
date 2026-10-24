import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

p = GPIO.PWM(en, 1000)
p.start(25)

print("\n")
print("Default: LOW speed & Forward direction")
print("Commands:")
print("r-run | s-stop | f-forward | b-backward | l-low | m-medium | h-high | e-exit")
print("\n")

try:
    while True:
        x = input("Enter command: ").lower()

        if x == 'r':
            print("Run")
            if temp1 == 1:
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                print("Forward")
            else:
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                print("Backward")

        elif x == 's':
            print("Stop")
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)

        elif x == 'f':
            print("Forward")
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            temp1 = 1

        elif x == 'b':
            print("Backward")
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            temp1 = 0

        elif x == 'l':
            print("Low speed")
            p.ChangeDutyCycle(25)

        elif x == 'm':
            print("Medium speed")
            p.ChangeDutyCycle(50)

        elif x == 'h':
            print("High speed")
            p.ChangeDutyCycle(75)

        elif x == 'e':
            print("Exiting...")
            break

        else:
            print("<<< Wrong input >>>")

finally:
    p.stop()
    GPIO.cleanup()
    print("GPIO Cleaned up")