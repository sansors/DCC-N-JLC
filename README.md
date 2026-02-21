# DCC-N-JLC : Décodeur DCC Ultra-Compact

Un projet de décodeur DCC moteur + éclairage pour le modélisme ferroviaire à l'échelle N (1:160). Conçu avec KiCad et optimisé pour la fabrication chez JLCPCB.

## 🎯 Objectifs
*   **Ultra-Compact :** Dimensions max de 9mm x 10mm (double face).
*   **Haute Tension :** Supporte le DCC (14-22V) sans chauffe excessive.
*   **Moderne :** Basé sur STM32G0 + Driver DRV8876 (VQFN 3x3mm).
*   **Open Source :** Schémas et Routage disponibles (Licence CERN-OHL-S).

## 🛠 Spécifications Techniques
*   **MCU :** STM32G031G8U6 (4x4mm UFQFPN-28) - 64MHz, 64KB Flash.
*   **Driver Moteur :** DRV8876 (3x3mm VQFN-16) - 1.5A Continu / 3A Pic (Mesure de courant intégrée).
*   **Régulateur :** ME6203A33M3G (SOT-23) - LDO 3.3V Ultra Low Dropout.
*   **Sorties Auxiliaires :** 2x MOSFET 200mA (BSS138DW) pour feux avant/arrière (LEDs).
*   **Protection :** Pont redresseur Schottky discret (B5819WS x4) et condensateurs MLCC X7R.

## 📂 Structure du Dépôt
*   `docs/` : Datasheets, spécifications techniques et notes de design.
*   `hardware/` : Fichiers KiCad (Schéma `.kicad_sch`, PCB `.kicad_pcb`).
*   `firmware/` : Code source (PlatformIO / CubeMX) - *À venir*.

## 🚀 Commencer
1.  Cloner le dépôt : `git clone https://github.com/sansors/DCC-N-JLC.git`
2.  Ouvrir `hardware/DCC-N-JLC.kicad_pro` avec KiCad (v7 ou v8 recommandé).
3.  Vérifier les bibliothèques manquantes dans `hardware/libs/MISSING_COMPONENTS.md`.

## 🤝 Contribution
Voir `docs/workflow_kicad.md` pour les règles de contribution.
Ce projet est hébergé par [OpenClaw](https://openclaw.ai) et la communauté DCC.
