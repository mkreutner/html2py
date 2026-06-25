#!/usr/bin/env python3
import os
import sys
from weasyprint import HTML


def generate_pdf(html_path, output_path=None):
    # 1. Vérification que le fichier HTML existe
    if not os.path.exists(html_path):
        print(f"❌ Erreur : Le fichier '{html_path}' n'existe pas.")
        sys.exit(1)

    # 2. Détermination du dossier parent (base_url) pour résoudre les chemins relatifs (CSS, images)
    base_dir = os.path.dirname(os.path.abspath(html_path))

    # 3. Détermination du nom du fichier de sortie si non fourni
    if not output_path:
        filename_without_ext = os.path.splitext(os.path.basename(html_path))[0]
        output_path = os.path.join(base_dir, f"{filename_without_ext}.pdf")

    print(f"🔄 Analyse du fichier HTML : {html_path}")
    print(f"📂 Répertoire racine (base_url) : {base_dir}")
    print("⏳ Génération du PDF en cours...")

    try:
        # L'argument magique 'base_url' permet à WeasyPrint de lier le HTML, le CSS et le dossier img/
        html_doc = HTML(filename=html_path, base_url=base_dir)

        # Génération effective du PDF
        html_doc.write_pdf(output_path)

        print(f"✅ PDF généré avec succès : {output_path}")

    except Exception as e:
        print(f"❌ Une erreur est survenue lors de la génération : {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Permet d'utiliser le script en ligne de commande : ./html2pdf.py document.html
    if len(sys.argv) < 2:
        print(
            "ℹ️ Usage : python3 html2pdf.py <chemin_vers_le_html> [chemin_de_sortie_pdf]"
        )
        sys.exit(1)

    html_input = sys.argv[1]
    pdf_output = sys.argv[2] if len(sys.argv) > 2 else None

    generate_pdf(html_input, pdf_output)
