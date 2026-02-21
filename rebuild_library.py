#!/usr/bin/env python3
"""
Reconstruction complète de la bibliothèque KiCad depuis LCSC.
Télécharge tous les composants de la BOM définitive.
"""

import subprocess
import os
import sys

# BOM définitive avec IDs LCSC
BOM_COMPONENTS = [
    ("STM32G031G8U6", "C432211"),
    ("DRV8876RGTR", "C1852100"),
    ("ME6203A33M3G", "C87842"),
    ("B5819WS", "C39831953"),
    ("BSS138DW", "C154900"),
    ("MMBT3904", "C20526"),
]

def run_command(cmd):
    """Exécute une commande shell et retourne la sortie"""
    print(f"  Exécution: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ❌ Erreur: {result.stderr}")
        return False
    print(f"  ✅ Succès")
    return True

def rebuild_library():
    """Reconstruit la bibliothèque KiCad"""
    
    lib_file = "hardware/libs/LCSC_Components.kicad_sym"
    lib_dir = "hardware/libs"
    
    print("🔧 Reconstruction de la bibliothèque KiCad...")
    print(f"Bibliothèque cible: {lib_file}")
    print()
    
    # Créer un fichier vide pour démarrer
    with open(lib_file, 'w') as f:
        f.write('(kicad_symbol_lib (version 20211014)\n')
        f.write('  (generator "easyeda2kicad")\n')
        f.write(')\n')
    
    # Télécharger chaque composant
    for name, lcsc_id in BOM_COMPONENTS:
        print(f"📦 Téléchargement: {name} (LCSC: {lcsc_id})")
        
        cmd = f"easyeda2kicad --lcsc_id {lcsc_id} --full --output {lib_file} --overwrite"
        if not run_command(cmd):
            print(f"Échec du téléchargement de {name}")
            return False
    
    print("\n✅ Bibliothèque reconstruite avec succès!")
    print(f"Composants intégrés: {len(BOM_COMPONENTS)}")
    
    # Vérification finale
    print("\n🔍 Vérification des symboles...")
    with open(lib_file, 'r') as f:
        content = f.read()
    
    for name, lcsc_id in BOM_COMPONENTS:
        # Le nom du symbole dans la bibliothèque peut être différent
        # On vérifie juste que l'ID LCSC est présent
        if lcsc_id in content:
            print(f"  ✓ {name} présent")
        else:
            print(f"  ⚠ {name} non trouvé (ID: {lcsc_id})")
    
    return True

def clean_old_footprints():
    """Nettoie les empreintes obsolètes"""
    
    print("\n🧹 Nettoyage des empreintes obsolètes...")
    
    # Empreintes à conserver (celles utilisées par la BOM)
    keep_footprints = [
        "UFQFPN-28_L4.0-W4.0-P0.50-BL",
        "VFQFN-16_L3.0-W3.0-P0.50-BL-EP1.7",
        "SOT-23-3_L2.9-W1.3-P1.90-LS2.4-BR",
        "SOD-323_L1.7-W1.3-LS2.5-RD",
        "SOT-23-6_L2.9-W1.6-P0.95-LS2.8-BR",
    ]
    
    pretty_dir = "hardware/libs/LCSC_Components.pretty"
    if not os.path.exists(pretty_dir):
        print(f"  ⚠ Répertoire non trouvé: {pretty_dir}")
        return
    
    # Lister toutes les empreintes
    for filename in os.listdir(pretty_dir):
        if filename.endswith(".kicad_mod"):
            footprint_name = filename[:-10]  # Enlever .kicad_mod
            
            # Vérifier si l'empreinte est utilisée
            used = False
            for keep in keep_footprints:
                if keep in footprint_name:
                    used = True
                    break
            
            if not used:
                filepath = os.path.join(pretty_dir, filename)
                print(f"  🗑️ Suppression: {filename}")
                os.remove(filepath)
            else:
                print(f"  ✓ Conservé: {filename}")
    
    print("  ✅ Nettoyage terminé")

if __name__ == "__main__":
    try:
        if not rebuild_library():
            sys.exit(1)
        
        clean_old_footprints()
        
        print("\n🎯 Reconstruction terminée avec succès!")
        print("La bibliothèque est prête pour le projet DCC-N-JLC.")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)