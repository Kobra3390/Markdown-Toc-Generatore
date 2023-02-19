import re
from rich.console import Console
from rich.style import Style

import time
from rich.progress import Progress

console = Console()

ascii_art = """


    __  ___           __       __                       __________  ______
   /  |/  /___ ______/ /______/ /___ _      ______     /_  __/ __ \/ ____/
  / /|_/ / __ `/ ___/ //_/ __  / __ \ | /| / / __ \     / / / / / / /     
 / /  / / /_/ / /  / ,< / /_/ / /_/ / |/ |/ / / / /    / / / /_/ / /___   
/_/  /_/\__,_/_/  /_/|_|\__,_/\____/|__/|__/_/ /_/    /_/  \____/\____/   
                                                                          


"""

myStyle = Style(color="#78e2a0", bold=True)

console.print(ascii_art, style=myStyle)

# Chiedi all'utente di inserire la path del file .md
file_path = input("Inserisci la path del file .md: ")

# Leggi il contenuto del file .md
with open(file_path, "r") as file:
    content = file.read()

# Controlla se la TOC è già presente nel file
if "## Table of Contents" not in content:
    # Trova tutti gli headers nel contenuto del file
    headers = re.findall(r"(?m)^(#{1,6})\s(.+)$", content)

    # Crea la tabella dei contenuti
    table_of_contents = "## Table of Contents\n\n"
    for header in headers:
        level = len(header[0])
        title = header[1]
        link = re.sub(r"[^\w]+", "-", title.lower())
        table_of_contents += "  " * (level-1) + f"- [{title}](#{link})\n"

    # Inserisci la tabella dei contenuti nel documento
    with open(file_path, "w") as file:
        file.write(table_of_contents + "\n" + content)

    duration = 0.1 # durata in secondi di ogni avanzamento

    with Progress() as progress:
        print("")
        task = progress.add_task("[green]Loading...", total=100)
        for i in range(100):
            time.sleep(duration)
            progress.update(task, advance=1)

    console.print(f"\nSuccess !!\n\tFile Update [ {file_path} ]\n", style=myStyle)

else:
    console.print(f"\nTOC già presente nel file [ {file_path} ]\n", style=myStyle)



