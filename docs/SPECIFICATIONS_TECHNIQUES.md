# Spécifications Techniques : Décodeur DCC Ultra-Compact (N-Scale)

**Objectif :** Conception d'un décodeur DCC moteur + fonctions de taille minimale (< 10mm x 10mm) pour l'échelle N (1/160).
**Stratégie :** PCB Double Face haute densité, composants modernes (QFN/DFN), suppression des étages de puissance superflus.

## 1. Caractéristiques Cibles
*   **Dimensions Max :** 9.0 mm (L) x 10.0 mm (l) x 2.6 mm (h)
*   **Tension Rail (DCC) :** 12V - 22V (Protection jusqu'à 30V+)
*   **Courant Moteur :** 1.5A Continu / 3A Pic
*   **Fonctions Auxiliaires :** 2x Sorties amplifiées (F0 Avant / F0 Arrière ou Aux1/2) - 200mA max chacune.
*   **Interface :** Pads de programmation SWD (GND, 3V3, SWDIO, SWCLK) sur la tranche ou via connecteur propriétaire.

## 2. Bill of Materials (BOM) Sélectionnée

| Bloc Fonctionnel | Composant | Boîtier | Réf. LCSC (Suggérée) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Microcontrôleur** | **STM32G031G8U6** | UFQFPN-28 (4x4mm) | C432211 | Cortex-M0+, 64KB Flash. Le meilleur ratio taille/puissance. |
| **Driver Moteur** | **DRV8876** (TI) | VQFN-16 (3x3mm) | C505030 | Remplaçant moderne du DRV8870. Tiens 37V. Pin IPROPI pour mesure courant. |
| **Régulateur 3.3V** | **ME6203A33M3G** | SOT-23-3 | C84661 | LDO Faible chute, High Voltage Input (30V+). Bien plus petit que SOT-89. |
| **Redressement** | **B5819WS** (x4) | SOD-323 | C2924 | Schottky 1A. En pont discret pour flexibilité de placement. |
| **Sorties Aux** | **BSS138DW** | SOT-363 | C146036 | Double MOSFET-N 50V 200mA dans un boîtier 2x2mm. |
| **Protection** | **TVS Diode** | SOD-323 / 0603 | Cxxxxx | Optionnel mais recommandé sur l'entrée Rail (ex: SMAJ24A si place dispo). |
| **Passifs** | R / C | **0402** | - | Condensateurs MLCC X7R/X5R impératifs. Résistances 1%. |

## 3. Contraintes de Design (PCB)
*   **Épaisseur PCB :** 0.8mm ou 0.6mm (FR4)
*   **Cuivre :** 1oz (35µm)
*   **Largeur Piste Min :** 0.15mm (Signal) / 0.25mm (Puissance Moteur/Rail)
*   **Via Min :** 0.3mm / 0.6mm (Drill/Pad)
*   **Placement Suggéré :**
    *   **TOP :** STM32G031 (Centre) + DRV8876 (Côte à côte). Connecteur SWD.
    *   **BOTTOM :** Pont de diodes (4x SOD-323), LDO (SOT-23), MOSFET Aux (SOT-363) et Passifs de découplage.

## 4. Statut des Bibliothèques
*   `STM32G031G8U6` : ✅ Présent (LCSC_Components)
*   `DRV8876` : ❌ À créer/importer (VQFN-16 avec Pad Thermique)
*   `ME6203` : ❌ À créer/importer (SOT-23-3 standard)
*   `BSS138DW` : ✅ Présent
*   `B5819WS` : ✅ Présent
