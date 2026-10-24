#!/bin/sh
# Lance ce script depuis ce dossier : sh push.sh
git init -b main
git add .
git commit -m "Ajout des scripts du robot détecteur de QR codes"
git remote add origin https://github.com/ines548/Robot-QR-Code-Detector.git
git pull origin main --allow-unrelated-histories --no-edit 2>/dev/null || true
git push -u origin main
