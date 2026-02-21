# PROJECT_DCC-N-JLC - Master Document

**Date de mise à jour :** 21 février 2026  
**État :** Phase 2 (Design Hardware) - Routage PCB en cours  
**Responsable :** Clément (@sansors)  
**Assistant :** Ingrid (OpenClaw)

## 📋 Vue d'ensemble

**Objectif :** Conception d'un décodeur DCC moteur + fonctions ultra-compact (< 9x10mm) pour l'échelle N (1:160), compatible fabrication JLCPCB.

**Cycle de vie :** Phase 2/5 (Hardware Design → Firmware → Proto → Test → Release)

## 🎯 Spécifications Techniques

### Dimensions
- **Max :** 9.0 mm (L) × 10.0 mm (l) × 2.6 mm (h)
- **PCB :** 0.8mm FR4, 1oz cuivre, double face

### Électrique
- **Tension DCC :** 12–22V (protection jusqu'à 30V)
- **Courant moteur :** 1.5A continu / 3A pic
- **Sorties auxiliaires :** 2 × 200mA (MOSFET BSS138DW)
- **Interface :** SWD (GND, 3V3, SWDIO, SWCLK)

## 📦 Bill of Materials (BOM) - Version Définitive

| Bloc | Composant | Boîtier | Réf LCSC | Notes |
|------|-----------|---------|----------|-------|
| **MCU** | STM32G031G8U6 | UFQFPN‑28 (4×4mm) | C432211 | Cortex‑M0+, 64 KB Flash, meilleur ratio taille/puissance |
| **Driver moteur** | **DRV8876** (TI) | VQFN‑16 (3×3mm) | C505030 | Driver H‑bridge 37 V, pin IPROPI pour mesure de courant |
| **Régulateur 3.3 V** | ME6203A33M3G | SOT‑23‑3 | C84661 | LDO haute tension (30 V+), faible dropout, compact |
| **Redressement** | B5819WS ×4 | SOD‑323 | C2924 | Diodes Schottky 1 A, pont discret pour placement flexible |
| **Sorties aux.** | BSS138DW | SOT‑363 | C146036 | Double MOSFET‑N 50 V / 200 mA, boîtier 2×2 mm |
| **Transistor lecture** | MMBT3904 | SOT‑23‑3 | – | Étage de lecture DCC discret (gain de place) |
| **Passifs** | R/C | 0402 | – | Condensateurs MLCC X7R/X5R, résistances 1 % |

**Statut des bibliothèques KiCad :**
- ✅ STM32G031G8U6 (présent)
- ❌ **DRV8876** – à créer/importer (VQFN‑16 avec pad thermique)
- ❌ **ME6203** – à créer/importer (SOT‑23‑3 standard)
- ✅ BSS138DW, B5819WS (présents)

## 🔄 Décisions Techniques Clés

### 1. Driver moteur
- **Choix final :** DRV8876 (VQFN‑16, 3×3 mm)
- **Alternatives envisagées :** TB67H450FNG (HSOP‑8), AP1511B‑MS (SOT‑23‑6)
- **Raison :** Ultra‑compact, moderne, mesure de courant intégrée

### 2. Alimentation
- **Choix :** LDO ME6203 (SOT‑23‑3)
- **Raison :** Suppression du buck AP1511B (inductance trop volumineuse)
- **Risque :** Dissipation thermique (consommation estimée < 50 mA → OK)

### 3. Firmware
- **Approche recommandée :** Code natif STM32 (CubeIDE)
- **Alternative :** Arduino Core + bibliothèque NmraDcc
- **Avantage natif :** Performance maximale, consommation optimisée, taille binaire réduite

### 4. PCB
- **Stratégie :** Double face haute densité
- **Placement :**
  - **Top :** MCU + driver moteur côte à côte
  - **Bottom :** LDO, diodes, MOSFETs auxiliaires, passifs
- **Contraintes :** Pistes 0.15 mm (signal) / 0.25 mm (puissance), vias 0.3/0.6 mm

## 📁 Structure du Projet

```
DCC-N-JLC/
├── docs/                    # Documentation technique
│   ├── SPECIFICATIONS_TECHNIQUES.md
│   ├── LOGS_TECHNIQUES.md
│   ├── workflow_kicad.md
│   └── datasheets/         # PDF des composants
├── hardware/               # Conception KiCad
│   ├── libs/              # Bibliothèques LCSC
│   ├── (fichiers .kicad_sch/.kicad_pcb à créer)
│   └── MISSING_COMPONENTS.md
├── firmware/              # Code source (à venir)
│   ├── Core/
│   ├── Drivers/
│   └── README.md
└── README.md              # Présentation générale
```

## 🚀 Prochaines Étapes

### Priorité 1 – Finalisation Hardware
- [ ] Créer les symboles/empreintes manquants (DRV8876, ME6203)
- [ ] Saisir le schéma dans KiCad
- [ ] Routage PCB respectant 9×10 mm
- [ ] Générer les fichiers Gerber + BOM pour JLCPCB

### Priorité 2 – Développement Logiciel
- [ ] Initialiser projet STM32CubeIDE (ou PlatformIO)
- [ ] Intégrer la bibliothèque de décodage DCC (native ou NmraDcc)
- [ ] Implémenter PWM moteur + gestion des fonctions auxiliaires

### Priorité 3 – Prototypage
- [ ] Commander les PCB chez JLCPCB
- [ ] Assembler les composants (SMT + manuel)
- [ ] Tester la réception DCC et la commande moteur

## 📝 Notes de Workflow

### Discord
- **Canal principal :** `#discussion-dcc`
- **Recherche :** `#veille-et-recherche-dcc`
- **Logs techniques :** `#logs-techniques-v2`
- **Cahier des charges :** `#cahier-des-charges-v2`
- **Archives :** `🗄️ ARCHIVES PROJET` (à consolider)

### Git
- **Dépôt :** https://github.com/sansors/DCC-N-JLC
- **Branche par défaut :** `main`
- **Commits :** Préfixes `[HW]`, `[FW]`, `[DOC]`, `[BOM]`

### Automatisation
- **Cron OpenClaw :** `memory:daily-digest` (04:00 UTC)
- **Backup :** `./backup.sh` avant toute modification critique

## 🧠 Mémoire du Projet

- **2026‑02‑21 :** Validation BOM définitive – choix du DRV8876 et ME6203
- **2026‑02‑21 :** Recherche architecture firmware (L'Éclaireur)
- **2026‑02‑20 :** Installation serveurs MCP (jlcpcb, google, monitoring)
- **2026‑02‑19 :** Initialisation du projet et configuration Discord

---

**Dernière mise à jour :** 21 février 2026, 23:30 UTC  
**Maintenu par :** Ingrid (via OpenClaw)  
**Contact :** Clément (@sansors) sur Discord