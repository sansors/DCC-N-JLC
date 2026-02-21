# Workflow KiCad - Règles de Contribution

Ce document décrit le workflow de travail pour la conception hardware du projet DCC-N-JLC.

## 🛠 Environnement Requis
- **KiCad** : Version 7.0 ou supérieure (8.0 recommandée)
- **Librairies** : `LCSC_Components.kicad_sym` (incluse dans le dépôt)
- **Plugins** : Aucun plugin externe requis

## 📁 Structure des Fichiers
```
hardware/
├── DCC-N-JLC.kicad_pro          # Projet principal KiCad
├── DCC-N-JLC.kicad_sch          # Schéma principal
├── boards/                      # Versions PCB (v1, v2, etc.)
├── libs/                        # Librairies locales
│   ├── LCSC_Components.kicad_sym  # Symboles des composants
│   ├── LCSC_Components.pretty/    # Empreintes
│   └── LCSC_Components.3dshapes/  # Modèles 3D
├── sym-lib-table               # Configuration bibliothèques symboles
└── fp-lib-table                # Configuration bibliothèques empreintes
```

## 🔄 Workflow de Conception

### 1. Ajout d'un Nouveau Composant
1. Identifier le **LCSC ID** sur [JLCPCB.com](https://jlcpcb.com)
2. Télécharger la librairie avec `easyeda2kicad` :
   ```bash
   easyeda2kicad --lcsc_id C123456 --full --output hardware/libs/LCSC_Components.kicad_sym --overwrite
   ```
3. Vérifier que le symbole et l'empreinte sont corrects
4. Ajouter le composant à la BOM dans `docs/SPECIFICATIONS_TECHNIQUES.md`

### 2. Modification du Schéma
1. Ouvrir `hardware/DCC-N-JLC.kicad_pro` dans KiCad
2. Ajouter/modifier les composants dans le schéma
3. **Vérifier les connexions** avec le pinout défini dans `PROJECT_DCC-N-JLC.md`
4. Générer la netlist pour vérifier les erreurs

### 3. Routage PCB
1. Créer une nouvelle version dans `hardware/boards/` (ex: `v1/`)
2. Importer la netlist du schéma
3. Respecter les contraintes :
   - **Dimensions** : 9mm × 10mm maximum
   - **Pistes** : 0.15mm (signal), 0.25mm (puissance)
   - **Vias** : 0.3mm / 0.6mm (drill/pad)
   - **Couches** : Double face uniquement
4. Exécuter les vérifications DRC (Design Rule Check)

### 4. Génération des Fichiers de Production
1. **Gerber** : Fichiers pour fabrication PCB
2. **BOM** : Liste des composants (format JLCPCB)
3. **Pick & Place** : Positions des composants
4. Vérifier que tous les fichiers sont dans `hardware/boards/<version>/`

## 🧪 Vérifications Obligatoires
- **Avant commit** : Exécuter `git status` pour vérifier les fichiers modifiés
- **DRC** : Aucune erreur dans le routage
- **ERC** : Aucune erreur dans le schéma
- **BOM** : Cohérence avec `docs/SPECIFICATIONS_TECHNIQUES.md`

## 📊 Gestion des Versions
- **Schéma** : Garder une seule version active (`DCC-N-JLC.kicad_sch`)
- **PCB** : Une version par révision majeure dans `hardware/boards/`
- **Commit** : Préfixes `[HW]`, `[SCH]`, `[PCB]`, `[LIB]`

## 🔧 Dépannage

### Problèmes de Librairies
```
Erreur : Symbole non trouvé
Solution : Vérifier sym-lib-table et recharger les bibliothèques dans KiCad
```

### Problèmes d'Empreintes
```
Erreur : Empreinte non trouvée
Solution : Vérifier que l'empreinte existe dans LCSC_Components.pretty/
```

## 📝 Notes
- Toujours utiliser les **composants disponibles chez JLCPCB** (Basic/Extended)
- Préférer les **boîtiers CMS** (SOT-23, SOD-323, QFN, etc.)
- Documenter les décisions de conception dans `docs/LOGS_TECHNIQUES.md`

---

**Dernière mise à jour** : 21 février 2026  
**Responsable** : Clément (@sansors)  
**Assistant** : Ingrid (OpenClaw)