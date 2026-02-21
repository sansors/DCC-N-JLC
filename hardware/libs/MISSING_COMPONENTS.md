# Composants Manquants (Hardware Libs)

La BOM a été mise à jour avec des composants plus récents pour optimiser l'espace.
Veuillez importer les empreintes suivantes dans `hardware/libs/LCSC_Components.pretty` et `hardware/libs/LCSC_Components.kicad_sym`.

## 1. Driver Moteur : DRV8876
*   **Fabricant :** Texas Instruments
*   **Ref :** DRV8876 (Option: DRV8876N)
*   **Boîtier :** VQFN-16 (3.00mm x 3.00mm)
*   **Pad Thermique :** OUI (Connecté au GND)
*   **Source recommandée :** SnapEDA / UltraLibrarian ou créer manuellement (Pitch 0.5mm).

## 2. Régulateur LDO : ME6203
*   **Fabricant :** Microne (Nanjing Micro One)
*   **Ref :** ME6203A33M3G (3.3V)
*   **Boîtier :** SOT-23-3 (Standard)
*   **Pinout :**
    1.  GND
    2.  VOUT
    3.  VIN (High Voltage Input)
*   **Note :** Vérifier l'empreinte SOT-23 existante. Si le pinout diffère du standard (GND/OUT/IN), créer une variante `ME6203_SOT23`.
