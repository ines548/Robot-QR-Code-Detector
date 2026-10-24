# Robot QR Code Detector

Design and construction of a 4-wheel mobile robot controlled by QR codes, using a Raspberry Pi 5 and a USB camera.

## Project Description

The robot receives its movement commands by reading QR codes shown in front of its camera. This approach provides a contactless, easily extensible control interface, unlike conventional remote controls.

The system has three main parts:

- **Processing unit:** Raspberry Pi 5
- **Video acquisition:** USB camera, with QR code detection and decoding via OpenCV
- **Actuators:** 4 DC motors driven by two L298N H-bridges

### QR Commands

| QR Code | Command | Action |
|---|---|---|
| `F` | Forward | Move forward (all motors forward) |
| `B` | Backward | Move backward (all motors backward) |
| `L` | Left | Turn left (left motors reversed) |
| `R` | Right | Turn right (right motors reversed) |
| `S` | Stop | Stop all motors |

## Hardware

- 1 × Raspberry Pi 5 (main processing unit)
- 2 × L298N H-bridge (DC motor drivers)
- 4 × DC motors (wheel drive)
- 1 × USB camera (real-time video acquisition)
- 4-wheel robot chassis, power supply and jumper wires

### Wiring (Raspberry Pi 5 GPIO to L298N)

| Module | L298N pins | GPIO (IN / IN / EN-PWM) | Motor |
|---|---|---|---|
| L298N #1 | IN1 / IN2 / ENA | 24 / 23 / 25 | Motor 1 (front-left) |
| L298N #1 | IN3 / IN4 / ENB | 17 / 27 / 22 | Motor 2 (rear-left) |
| L298N #2 | IN5 / IN6 / ENC | 5 / 6 / 13 | Motor 3 (front-right) |
| L298N #2 | IN7 / IN8 / END | 19 / 26 / 12 | Motor 4 (rear-right) |

Each motor's direction of rotation depends on the logic state of its `IN` pins; speed is set by the duty cycle of the PWM signal on the `EN` pins (50% by default).

## Software

Written in **Python 3** on Raspberry Pi OS, using these libraries:

- `gpiozero`: GPIO and PWM control
- `OpenCV` (`cv2`): video capture, QR code detection and decoding
- `qrcode`: generation of the command QR code images
- `pyzbar`: alternative QR decoding (used in some scripts)

### How It Works

1. Initialize the GPIO, the USB camera and the QR detector
2. Capture images in a loop
3. When a QR code is detected, its value (`F`, `B`, `L`, `R`, `S`) triggers the matching movement function
4. Wait one second to avoid unwanted repeated commands, then go back to capturing

### Repository Files

| File | Purpose |
|---|---|
| `robotfonctionel.py` | Main program: detects QR codes and drives the motor |
| `qr_detec.py` | QR code detection with outline drawing |
| `qr_test.py` | Camera test |
| `qr_creation.py`, `qr_.py` | Generation of the command QR codes |
| `onemotormotion.py` | Keyboard test of a single motor (speed, direction) |

## Installation

```bash
pip install opencv-python pyzbar qrcode gpiozero
```

To generate the QR codes, run `python qr_.py`, then show the images in front of the robot's camera. Quit the program with `q` or the Esc key.

## Challenges

- **Unstable QR detection** in poor lighting: solved by improving the ambient light and increasing the camera resolution.
- **GPIO configuration on Raspberry Pi 5** with `gpiozero`: solved by checking and explicitly configuring the pin factory.
- **Repeated commands** caused by video/motor synchronization: solved by adding a `sleep(1)` delay after each command.

## Future Work

- Integrating YOLO for vision-based detection and gesture recognition
- Distance sensors for obstacle avoidance
- Remote control via SSH


