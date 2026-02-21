# DCC-N-JLC 🚂

Décodeur DCC ultra-miniature pour échelle N, respectant les normes standards NMRA, conçu avec des composants exclusivement disponibles chez JLCPCB.

## 📊 État du Projet
- **Phase actuelle :** Phase 2 (Design Hardware / Routage PCB)
- **Dernière mise à jour :** 2026-02-21
- **Objectif :** Créer le décodeur le plus petit possible tout en étant performant et robuste.

## 🧱 Architecture Matérielle (Validée)

### Composants Principaux
| Fonction | Référence | Boîtier | Lien LCSC |
| :--- | :--- | :--- | :--- |
| **Cerveau (MCU)** | STM32G031G8U6 | UFQFPN-28 | [C432211](https://jlcpcb.com/partdetail/C432211) |
| **Driver Moteur** | AP1511B-MS | SOT-23-6 | [C19272816](https://jlcpcb.com/partdetail/C19272816) |
| **Pont de Diodes** | 4x B5819WS (1A) | SOD-323 | [C39831953](https://jlcpcb.com/partdetail/C39831953) |
| **Régulateur 3.3V** | HT7533-1 (24V In) | SOT-23 | [C5379078](https://jlcpcb.com/partdetail/C5379078) |
| **Dual MOSFET** | BSS138DW (2 Fonctions) | SOT-363 | [C154900](https://jlcpcb.com/partdetail/C154900) |
| **Lecture DCC** | MMBT3904 | SOT-23 | [C20526](https://jlcpcb.com/partdetail/C20526) |

### 📐 Configuration des Pins (STM32)
- **PA0 :** Entrée DCC (Signal)
- **PA1 / PA2 :** Commande Moteur (PWM IN1/IN2)
- **PA3 / PA4 :** Sorties Fonctions 1 et 2 (Lumières)

## 📁 Structure du dépôt
- `hardware/` : Projet KiCad (Schémas, PCB, Libs LCSC importées)
- `firmware/` : Code source STM32 (À venir)
- `docs/` : Datasheets PDF et guides de workflow

## 🛠️ Workflow KiCad
Le dépôt contient déjà toutes les librairies nécessaires dans `hardware/libs`.
1. Faire un `git pull`.
2. Utiliser la librairie **"LCSC_Components"** pour le schéma.
3. Les empreintes et modèles 3D sont déjà liés.
