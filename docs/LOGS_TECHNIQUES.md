# Journal des Logs Techniques (Projet DCC-N-JLC)

Ce fichier consigne les décisions techniques majeures et les changements de design.

---

### [2025-02-21] Refonte Ultra-Compacte (v2.0)
**Motif :** Optimisation pour l'échelle N (1:160) - Le design initial (Buck + Gros passifs) était trop volumineux.

**1. Choix du Driver Moteur**
*   **Abandonné :** Pont H discret (trop de composants) / SOIC-8 (trop large).
*   **Validé :** **DRV8876** (Texas Instruments).
    *   **Pourquoi :** Boîtier VQFN 3x3mm (gain de 50% vs SOIC). Tient 37V (Sûr pour DCC 14-22V).
    *   **Bonus :** Pin `IPROPI` (Current Mirror) permet la mesure de courant moteur sans shunt externe complexe.
    *   **Contrainte :** Pad thermique sous le composant (Vias obligatoires).

**2. Stratégie d'Alimentation**
*   **Abandonné :** Buck Converter AP1511B (Inductance trop volumineuse pour <10mm²).
*   **Validé :** Régulateur Linéaire (LDO) **ME6203** (Microne).
    *   **Pourquoi :** Boîtier SOT-23-3 (vs SOT-89 pour HT7533). Courant de repos faible.
    *   **Risque :** Chauffe si consommation 3.3V > 50mA. (MCU + LEDs uniquement = OK).
    *   **Sécurité :** Vérifier version "High Voltage Input" (30V+).

**3. Passifs et Routage**
*   **Passifs :** Passage intégral en **0402** (Condensateurs MLCC / Résistances).
*   **Diodes :** Maintien des **B5819WS** (SOD-323) en discret.
    *   *Raison :* Un pont intégré (MBS) est trop rigide à placer. Les diodes unitaires peuvent se glisser entre les vias.
*   **Agencement Suggéré :**
    *   **TOP :** STM32G031 (Centre) + DRV8876.
    *   **BOTTOM :** LDO, Diodes, MOSFETs Aux (BSS138DW).

**4. Bibliothèques KiCad**
*   Ajout de l'empreinte `VQFN-16_L3.0-W3.0-P0.50-BL-EP` pour DRV8876.
*   Ajout du symbole `ME6203-3.3V` (Pinout SOT-23 standard).
