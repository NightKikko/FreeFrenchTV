import requests
import difflib
import re
import tempfile
import subprocess

M3U_URL = "https://raw.githubusercontent.com/Paradise-91/ParaTV/main/playlists/paratv.m3u"

def download_m3u(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Erreur lors du téléchargement du fichier M3U.")
        exit()
    return response.text

def parse_m3u(content):
    lines = content.splitlines()
    channels = []
    current_title = None

    for line in lines:
        if line.startswith('#EXTINF'):
            title_match = re.search(r',([^,]+)', line)
            if title_match:
                current_title = title_match.group(1).strip().lower()
            else:
                current_title = re.sub(r'#EXTINF:-?\d+(\.\d+)?,?', '', line).strip().lower()
        elif line.startswith('http') or line.startswith('https'):
            if current_title:
                channels.append((current_title, line))
                current_title = None
    return channels

def main():
    m3u_content = download_m3u(M3U_URL)
    channels = parse_m3u(m3u_content)

    print("Chaînes disponibles:")
    for channel in channels:
        print(f"- {channel[0]}")

    channel_name = input("\nEntrez le nom de la chaîne que vous souhaitez regarder: ").strip().lower()

    names = [channel[0] for channel in channels]
    best_match = difflib.get_close_matches(channel_name, names, n=1, cutoff=0.6)

    if best_match:
        selected_channel_name = best_match[0]
        print(f"Chaîne trouvée: {selected_channel_name}")

        for channel in channels:
            if channel[0] == selected_channel_name:
                stream_url = channel[1]
                break

        if stream_url:
            print(f"Ouvrir le flux depuis: {stream_url}")
            with tempfile.NamedTemporaryFile(suffix=".m3u8", delete=False) as temp_file:
                temp_file.write(f"{stream_url}\n".encode())
                temp_file_path = temp_file.name
            subprocess.run(['start', '', temp_file_path], shell=True)
        else:
            print("Aucun flux trouvé pour cette chaîne.")
    else:
        print("Chaîne non trouvée.")

if __name__ == "__main__":
    main()
