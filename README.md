# Avertissement : Flux IPTV

## ❗ **IMPORTANT : Le contenu de ce script provient de sources externes.** Nous ne sommes pas responsables des flux IPTV eux-mêmes, de leur qualité ou de leur disponibilité. Ce script est conçu pour vous permettre d'accéder aux flux en utilisant une liste M3U publique. Veuillez vous assurer que vous respectez les droits d'auteur et les conditions d'utilisation associées aux flux que vous consultez.

## Description

Ce script Python vous permet de télécharger une liste de flux IPTV au format M3U, de rechercher des chaînes par nom et d'ouvrir le flux correspondant dans votre lecteur vidéo par défaut via une boîte de dialogue de sélection de programme.

## Prérequis

- Python 3.x
- Bibliothèques Python : `requests`, `difflib`, `re`, `tempfile`, `subprocess`

## Installation

1. Clonez le dépôt ou téléchargez les fichiers du script.
2. Installez les bibliothèques nécessaires si elles ne sont pas déjà installées :
    ```bash
    pip install requests
    ```

## Utilisation

1. Exécutez le script :
    ```bash
    python NepsTV.py
    ```

2. Le script téléchargera la liste M3U, extraira les chaînes disponibles et vous demandera de saisir le nom de la chaîne que vous souhaitez regarder.

3. Après avoir trouvé la chaîne, le script créera un fichier temporaire avec l'URL du flux et ouvrira ce fichier avec le programme par défaut associé aux fichiers `.m3u8` sur votre système.

## Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à soumettre une demande de tirage (pull request).

## Licence

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).
