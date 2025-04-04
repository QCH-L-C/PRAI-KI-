#!/usr/bin/env python3
import subprocess
import platform

def flush_dns_cache():
    current_os = platform.system()
    try:
        if current_os == "Linux":
            subprocess.run("sudo systemd-resolve --flush-caches", shell=True, check=True)
            return "DNS-Cache auf Linux geleert."
        elif current_os == "Darwin":
            subprocess.run("sudo dscacheutil -flushcache", shell=True, check=True)
            return "DNS-Cache auf macOS geleert."
        elif current_os == "Windows":
            subprocess.run("ipconfig /flushdns", shell=True, check=True)
            return "DNS-Cache auf Windows geleert."
        else:
            return "Unbekanntes Betriebssystem. DNS-Cache konnte nicht geleert werden."
    except Exception as e:
        return f"Fehler beim Leeren des DNS-Caches: {str(e)}"

def diagnose_domain(domain):
    try:
        # Für Linux/macOS: benutze ping -c, Windows verwendet -n; hier wird Linux/Mac angenommen.
        result = subprocess.check_output(f"ping -c 4 {domain}", shell=True, stderr=subprocess.STDOUT)
        return result.decode()
    except subprocess.CalledProcessError as e:
        return f"DNS-Auflösung für {domain} fehlgeschlagen:\n{e.output.decode()}"

def troubleshooting_instructions():
    instructions = (
        "DNS Troubleshooting Instructions:\n"
        "1. DNS-Cache leeren:\n"
        "   - Windows: Öffne die Eingabeaufforderung als Administrator und führe 'ipconfig /flushdns' aus.\n"
        "   - macOS: Öffne das Terminal und führe 'sudo dscacheutil -flushcache' aus.\n"
        "   - Linux: Führe 'sudo systemd-resolve --flush-caches' aus.\n"
        "2. DNS-Server ändern:\n"
        "   - Verwende öffentliche DNS-Server wie 8.8.8.8 (Google) oder 1.1.1.1 (Cloudflare).\n"
        "3. Router neu starten:\n"
        "   - Trenne den Router für einige Minuten vom Stromnetz und schalte ihn wieder ein.\n"
        "4. Domain-Konfiguration überprüfen:\n"
        "   - Stelle sicher, dass der A-Record korrekt auf Deine Server-IP zeigt.\n"
    )
    return instructions

if __name__ == "__main__":
    domain = "rfof-network.org"
    print("Flushing DNS Cache...")
    print(flush_dns_cache())
    print("\nDNS Diagnosis:")
    print(diagnose_domain(domain))
    print("\nTroubleshooting Instructions:")
    print(troubleshooting_instructions())
