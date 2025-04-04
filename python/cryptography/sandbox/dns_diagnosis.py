import subprocess

def flush_dns_cache():
    """DNS-Cache leeren auf verschiedenen Plattformen."""
    try:
        platform = subprocess.check_output("uname", shell=True).decode().strip()
        if "Linux" in platform:
            subprocess.run("sudo systemd-resolve --flush-caches", shell=True)
            print("DNS-Cache auf Linux geleert.")
        elif "Darwin" in platform:  # macOS
            subprocess.run("sudo dscacheutil -flushcache", shell=True)
            print("DNS-Cache auf macOS geleert.")
        elif "Windows" in platform:
            subprocess.run("ipconfig /flushdns", shell=True)
            print("DNS-Cache auf Windows geleert.")
    except Exception as e:
        print(f"Fehler beim DNS-Cache-Leeren: {e}")

def diagnose_dns(domain):
    """Probleme mit DNS-Auflösung diagnostizieren."""
    try:
        print(f"Prüfe DNS-Auflösung für {domain}...")
        result = subprocess.check_output(f"ping -c 4 {domain}", shell=True).decode().strip()
        print(result)
    except subprocess.CalledProcessError:
        print(f"DNS-Auflösung für {domain} fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler bei DNS-Diagnose: {e}")

if __name__ == "__main__":
    domain = "rfof-network.org"
    flush_dns_cache()
    diagnose_dns(domain)
