# DCC-N-JLC

Décodeur DCC pour échelle N, respectant les normes standards NMRA, conçu avec des composants exclusivement disponibles chez JLCPCB.

## Architecture Matérielle (Validée)

- **MCU :** STM32G031G8U6 (UFQFPN-28)
- **Driver Moteur :** AP1511B-MS (SOT-23-6) - 1.2A / 16V
- **Redressement :** 4x B5819WS (SOD-323) - 1.0A / 40V
- **Régulation :** HT7533-1 (SOT-23) - 3.3V / 24V Input
- **Lecture DCC :** MMBT3904 (SOT-23) + Montage discret

## Structure du dépôt

- `hardware/` : Projet KiCad (Schémas et PCB)
- `firmware/` : Code source STM32CubeIDE
- `docs/` : Datasheets et spécifications NMRA

## Workflow KiCad

1.  **Librairies :** Utiliser les empreintes standard KiCad autant que possible.
2.  **Versioning :** Commiter les fichiers `.kicad_sch` et `.kicad_pcb`. Les fichiers `-bak` sont ignorés.
3.  **BOM :** Exportation vers JLCPCB simplifiée via les références LCSC incluses dans les propriétés des composants.
