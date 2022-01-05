# Assignment 
Aus Stromverbrauchsdaten ein Gebäude wählen und die Daten sinnvoll vorverarbeiten und folgende Grafiken erzeugen.
- Beispielwoche Sommer und Winter
- Durchschnittswoche gesamt
- Durchschnittswoche über einen Zeitraum (Zusatzaufgabe)
- Jahresdauerlinie
- Zusatzaufgabe: Nutzung eines GIT-Repositories

# Anleitung
Zunächst im Code '1.0-fbu-load-initial-data' das gewünschte Gebäude auswählen. Eine Tabelle des gewünschten Gebäudes wird erstellt. 

Auf jene Tabelle wird im Code '1.0-fbu-visualize-data' zugegriffen. 
Bei der Ausführung des zweiten Codes werden Plots erstellt und in den jeweiligen Ordnern abgespeichert.  

# Ordnerstruktur

+-- Datenbankstruktur        <-  Zusatzaufgabe, Vorschlag einer Datenbankstruktur (nicht relevant für Code)

+-- data                     <-  Used Data
-  +-- processed             <-  Verarbeitete Daten zur Erstellung der plots
-   +-- raw                  <-  Originale Rohdaten
  

+-- images
-   +-- HTML                 <-  Plots der Grafiken im Dateiformat .html
-   +-- PDF                  <-  Plots der Grafiken im Dateiformat .pdf
-   +-- SVG                  <-  Plots der Grafiken im Dateiformat .svg  
  
+-- src                      <-  Code zur Erstellung der Plots im .ipynb Format

+-- .gitignore

+-- READ.ME

+-- requirements.txt    <- The requirements file for reproducing the analysis environment



## Author 
Felix Burr