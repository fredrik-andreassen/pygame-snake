## pygame-snake

![forhåndsvisning](media/demo.png)

### Avhengigheter
- [`pygame`](https://www.pygame.org/wiki/GettingStarted)

### Kjør spillet
Én spiller: `python main.py`

#### Startargumenter
- `-d` / `--debug`: Kjører med feilsøkingsmodus.
- `-w` / `--width`: Vindusbredde 1920 piksler. Ignoreres hvis ikke delbar på 20.
- `-h` / `--height`: Vindushøyde 1080 piksler. Ignoreres hvis ikke delbar på 20.
- `-p` / `--players`: Antall spillere. Ignoreres hvis ikke mellom 1 og 4.

Eksempler:

- `python main.py -w 3840 -h 2160 -p 4` starter spill i 4K med fire spillere.
- `python main.py -d 10 -w 300 -h 200` starter spill i feilsøkingsmodus med 10 bilder per sekund og 300x200 oppløsning.

### Kontroller
Spiller 1: <kbd>↑</kbd>  <kbd>←</kbd>  <kbd>↓</kbd>  <kbd>→</kbd>

Spiller 2: <kbd>W</kbd>  <kbd>A</kbd>  <kbd>S</kbd>  <kbd>D</kbd>

Spiller 3: <kbd>T</kbd>  <kbd>F</kbd>  <kbd>G</kbd>  <kbd>H</kbd>

Spiller 4: <kbd>I</kbd>  <kbd>J</kbd>  <kbd>K</kbd>  <kbd>L</kbd>

Flere tilkoblede tastatur anbefales med >2 spillere.
