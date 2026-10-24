# Robot QR Code Detector

Conception et réalisation d'un robot mobile à 4 roues commandé par QR codes, via un Raspberry Pi 5 et une caméra USB.

Projet réalisé lors d'un stage au **Centre de Recherche en Technologies Industrielles (CRTI), Cherraga, Alger**, dans le cadre de la formation *Robotique et Systèmes Intelligents* (Département Automatique, Faculté de Génie Électrique, USTHB), année universitaire 2025–2026.



## Description du projet

Le robot reçoit ses ordres de déplacement en lisant des QR codes présentés devant sa caméra. Cette approche offre une interface de contrôle sans contact et facilement extensible, contrairement aux télécommandes classiques.

Le système se compose de trois parties :

- **Unité de traitement :** Raspberry Pi 5
- **Acquisition vidéo :** caméra USB, avec détection et décodage des QR codes via OpenCV
- **Actionneurs :** 4 moteurs DC pilotés par deux ponts en H L298N

### Commandes QR

| QR Code | Commande | Action |
|---|---|---|
| `F` | Forward | Avance (tous les moteurs vers l'avant) |
| `B` | Backward | Recule (tous les moteurs vers l'arrière) |
| `L` | Left | Tourne à gauche (moteurs gauche inversés) |
| `R` | Right | Tourne à droite (moteurs droite inversés) |
| `S` | Stop | Arrêt complet de tous les moteurs |

## Matériel utilisé

- 1 × Raspberry Pi 5 (unité de traitement centrale)
- 2 × pont en H L298N (contrôle des moteurs DC)
- 4 × moteurs DC (entraînement des roues)
- 1 × caméra USB (acquisition vidéo en temps réel)
- Châssis robot 4 roues, alimentation et fils de connexion

### Câblage (GPIO du Raspberry Pi 5 vers L298N)

| Module | Broches L298N | GPIO (IN / IN / EN-PWM) | Moteur |
|---|---|---|---|
| L298N #1 | IN1 / IN2 / ENA | 24 / 23 / 25 | Moteur 1 (avant-gauche) |
| L298N #1 | IN3 / IN4 / ENB | 17 / 27 / 22 | Moteur 2 (arrière-gauche) |
| L298N #2 | IN5 / IN6 / ENC | 5 / 6 / 13 | Moteur 3 (avant-droit) |
| L298N #2 | IN7 / IN8 / END | 19 / 26 / 12 | Moteur 4 (arrière-droit) |

La direction de rotation de chaque moteur dépend de l'état logique des broches `IN` ; la vitesse est réglée par le rapport cyclique du signal PWM sur les broches `EN` (50 % par défaut).

## Logiciel

Développé en **Python 3** sur Raspberry Pi OS, avec les bibliothèques :

- `gpiozero` : gestion des GPIO et du PWM
- `OpenCV` (`cv2`) : capture vidéo, détection et décodage des QR codes
- `qrcode` : génération des images QR codes de commande
- `pyzbar` : décodage QR alternatif (utilisé dans certains scripts)

### Fonctionnement

1. Initialisation des GPIO, de la caméra USB et du détecteur QR
2. Capture d'une image en boucle
3. Si un QR code est détecté, sa valeur (`F`, `B`, `L`, `R`, `S`) déclenche la fonction de mouvement correspondante
4. Pause d'une seconde pour éviter les répétitions involontaires, puis retour à la capture

### Fichiers du dépôt

| Fichier | Rôle |
|---|---|
| `robotfonctionel.py` | Programme principal : détecte les QR codes et commande le moteur |
| `qr_detec.py` | Détection de QR codes avec tracé du contour |
| `qr_test.py` | Test de la caméra |
| `qr_creation.py`, `qr_.py` | Génération des QR codes de commande |
| `onemotormotion.py` | Test d'un moteur au clavier (vitesse, sens) |

## Installation

```bash
pip install opencv-python pyzbar qrcode gpiozero
```

Pour générer les QR codes : `python qr_.py`, puis présenter les images devant la caméra du robot. Quitter le programme avec `q` ou la touche Échap.

## Difficultés rencontrées

- **Détection QR instable** en mauvais éclairage : amélioration de l'éclairage et augmentation de la résolution de la caméra.
- **Configuration GPIO sur Raspberry Pi 5** avec `gpiozero` : vérification et configuration explicite du pin factory.
- **Répétition de commandes** due à la synchronisation vidéo/moteur : ajout d'un délai `sleep(1)` après chaque commande.

## Perspectives

- Intégration de YOLO pour la détection par vision et la reconnaissance gestuelle
- Capteurs de distance pour l'évitement d'obstacles
- Commande à distance via SSH

Ces améliorations n'ont pas pu être réalisées faute d'équipements disponibles au CRTI.
