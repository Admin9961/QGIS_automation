import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import subprocess
import urllib.request

print("Autore: Christopher Zonta")
print("Email: czonta1996@outlook.it")

# Funzione per ottenere informazioni da un sito con header personalizzato
def ottieni_informazioni_da_sito(url):
    try:
        # Specifica l'header desiderato (in questo caso, User-Agent)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
        # Effettua la richiesta HTTP con l'header specificato
        response = requests.get(url, headers=headers)
        
        # Verifica se l'URL è https://www.naturalearthdata.com
        if "https://www.naturalearthdata.com" in url:
            # Analizza il contenuto HTML della pagina
            soup = BeautifulSoup(response.text, 'html.parser')

            # Puoi stampare ulteriori informazioni in base alle tue esigenze
            print(f"Informazioni dal sito {url}:")
            print(f"  - Titolo: {soup.title.text}")
            print(f"  - URL: {url}")
        else:
            # Se l'URL non è https://www.naturalearthdata.com, stampa solo il titolo e l'URL
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"Informazioni dal sito {url}:")
            print(f"  - Titolo: {soup.title.text}")
            print(f"  - URL: {url}")
    except Exception as e:
        print(f"Errore nell'ottenere informazioni da {url}: {e}")

# Funzione per scaricare un file mostrando una barra di avanzamento
def scarica_file_con_barra(url, destinazione):
    with requests.get(url, stream=True) as response:
        # Ottieni la dimensione totale del file in bytes
        dimensione_totale = int(response.headers.get('content-length', 0))

        # Percorso della cartella "Downloads" utilizzando la variabile di ambiente %userprofile%
        downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')

        # Percorso completo del file nella cartella "Downloads"
        destinazione_file = os.path.join(downloads_path, destinazione)

        # Crea una barra di avanzamento con tqdm
        with tqdm(total=dimensione_totale, unit='B', unit_scale=True, unit_divisor=1024) as barra:
            with open(destinazione_file, 'wb') as file:
                for parte in response.iter_content(chunk_size=1024):
                    lunghezza = len(parte)
                    file.write(parte)
                    barra.update(lunghezza)

# Itera attraverso la lista di siti e ottieni informazioni con header personalizzato
siti_geospaziali = ["https://www.naturalearthdata.com"]
for sito in siti_geospaziali:
    ottieni_informazioni_da_sito(sito)


print("\nQuale dei seguenti pacchetti desidera scaricare?")
print("1. SHP (576 MB)")
print("2. SQLite (414 MB)")
print("3. Geopackage (426 MB)")
print("4. Grayscale shading based on Prisma artistic filtering (17.16 MB)")


scelta_pacchetto = input("Inserisci il numero corrispondente al pacchetto desiderato: ")


if scelta_pacchetto == "1":
    print("Hai scelto di scaricare il pacchetto SHP (576 MB).")
    # URL del pacchetto SHP
    url_pacchetto_shp = "https://naciscdn.org/naturalearth/packages/natural_earth_vector.zip"
    
    # Percorso completo del file nella cartella "Downloads"
    destinazione_file = "natural_earth_vector.zip"
    
    # Scarica il pacchetto SHP e salvalo nella cartella "Downloads" mostrando la barra di avanzamento
    scarica_file_con_barra(url_pacchetto_shp, destinazione_file)
    
    print(f"Pacchetto SHP scaricato nella cartella 'Downloads'.")
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    subprocess.run(['explorer', downloads_path])
elif scelta_pacchetto == "2":
    print("Hai scelto di scaricare il pacchetto SQLite (414 MB).")
    # URL del pacchetto SQLite
    url_pacchetto_sqlite = "https://naciscdn.org/naturalearth/packages/natural_earth_vector.sqlite.zip"
    
    # Percorso completo del file nella cartella "Downloads"
    destinazione_file = "natural_earth_vector.sqlite.zip"
    
    # Scarica il pacchetto SQLite e salvalo nella cartella "Downloads" mostrando la barra di avanzamento
    scarica_file_con_barra(url_pacchetto_sqlite, destinazione_file)
    
    print(f"Pacchetto SQLite scaricato nella cartella 'Downloads'.")
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    subprocess.run(['explorer', downloads_path])
elif scelta_pacchetto == "3":
    print("Hai scelto di scaricare il pacchetto Geopackage (426 MB).")
    # URL del pacchetto Geopackage
    url_pacchetto_geopackage = "https://naciscdn.org/naturalearth/packages/natural_earth_vector.gpkg.zip"
    
    # Percorso completo del file nella cartella "Downloads"
    destinazione_file = "natural_earth_vector.gpkg.zip"
    
    # Scarica il pacchetto Geopackage e salvalo nella cartella "Downloads" mostrando la barra di avanzamento
    scarica_file_con_barra(url_pacchetto_geopackage, destinazione_file)
    
    print(f"Pacchetto Geopackage scaricato nella cartella 'Downloads'.")
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    subprocess.run(['explorer', downloads_path])
elif scelta_pacchetto == "4":
    print("Hai scelto di scaricare il pacchetto Grayscale shading based on Prisma artistic filtering (17.16 MB).")
    url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/raster/PRISMA_SR_50M.zip"
destinazione_file = "PRISMA_SR_50M.zip"

try:
    # Ottieni la dimensione totale del file in bytes
    with requests.head(url) as response:
        dimensione_totale = int(response.headers.get('content-length', 0))

    # Percorso della cartella "Downloads" utilizzando la variabile di ambiente %userprofile%
    downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')

    # Percorso completo del file nella cartella "Downloads"
    destinazione_file = os.path.join(downloads_path, destinazione_file)

    # Crea una barra di avanzamento con tqdm
    with tqdm(total=dimensione_totale, unit='B', unit_scale=True, unit_divisor=1024, desc="Download") as barra:
        # Intestazioni simulate per emulare il comportamento di un browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.naturalearthdata.com/',
            'Upgrade-Insecure-Requests': '1',
        }

        # Effettua la richiesta HTTP con le intestazioni simulate
        with requests.get(url, headers=headers, stream=True) as response:
            # Verifica se la richiesta è andata a buon fine
            response.raise_for_status()

            # Salva il contenuto del file
            with open(destinazione_file, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    barra.update(len(chunk))

    print(f"\nFile scaricato con successo: {destinazione_file}")

    # Apre la cartella "Downloads"
    subprocess.run(['explorer', downloads_path])

except requests.exceptions.RequestException as e:
    print(f"Errore durante il download: {e}")
else:
    print("Finito: grazie per avermi usato =)")
