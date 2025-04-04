ALTERNATIVE_LINKS = [
    "https://backup1.rfof-network.org",
    "https://backup2.rfof-network.org",
    "https://mirror.rfof-network.org",
    "https://slash.rfof-network.org/
]

def get_active_link():
    """Prüft die Verfügbarkeit der Links und gibt den ersten funktionierenden zurück."""
    import requests
    for link in ALTERNATIVE_LINKS:
        try:
            print(f"Prüfe Verbindung zu {link}...")
            response = requests.get(link, timeout=5)
            if response.status_code == 200:
                print(f"Funktionierender Link gefunden: {link}")
                return link
        except requests.RequestException as e:
            print(f"Fehler bei {link}: {e}")
    return None

if __name__ == "__main__":
    active_link = get_active_link()
    if active_link:
        print(f"Website erreichbar unter: {active_link}")
    else:
        print("Keine funktionierenden Links verfügbar.")
