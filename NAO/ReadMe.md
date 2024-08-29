# <u>ReadMe NAO</u>

Diese Dokumentation dient dem Aufzeigen meiner Arbeitsergebnisse und -fortschritte während der praktischen Phase sowie dem Übermitteln meiner Erfahrungen an nachfolgende Personen, die gewillt sind sich selbst auch mit dem NAO in erweiterter Form zu befassen.

Bei meiner Dokumentation werden die Erfahrungen mit dem NAO und die Nutzung der Linux-Distribution **Ubuntu** genutzt. Als ros Distribution nutze ich dabei in der Linux-Applikation **iron**.

## Installation WSL und Ubuntu


Der erste Arbeitsschritt ist, wenn man mit einem Windows Betriebssystem arbeitet, die Installation eines Windows Subsystem for Linux(WSL), damit das Dateisystem von Linux sowie die Befehle genutzt werden können. Unter dem folgenden Link können Sie die Installation von WSL nachvollziehen.


```ssh
https://learn.microsoft.com/de-de/windows/wsl/install
```

Achten Sie bitte bei der Installation darauf Powershell als Administrator auszuführen, um mögliche Komplikationen bei der Installation zu vermeiden. Anschließend muss auch noch eine Linux-Distribution in WSL selbst installiert werden. Dabei habe ich die gängigste Distribution mit `<Ubuntu 20.04 2>` genutzt. Nutzen Sie dafür bitte den folgenden Befehl.

```
wsl --install -d
```
Die erfolgreiche Installation kann mit `wsl -l -v` überprüft werden.


### Wichtig!

Bei den Code-Blöcken und den anderen Code-Bestandteilen werden in der Regel keine Vergleichszeichen mitgeschrieben. Diese dienen im Text zur klaren Abgrenzung und in den Code-Blöcken zum Markieren, derjenigen Stellen die bearbeitet werden müssen.

## Installation ros2 iron

### Empfehlung

Suchen Sie sich im besten Fall online ein sogenanntes "cheat sheet" zu den Befehlen im Umgang mit einem Linux Subsystem heraus. In diesem Dokument können Sie die grundlegenden Befehle schnellstmöglich finden. Unter dem folgenden Link finden Sie das cheat sheet, welches ich nutze.

```
https://cheatography.com/davechild/cheat-sheets/linux-command-line/
```

### Grundlagen für Installation

Für die folgenden Schritte wird Ubuntu genutzt. Dafür sollte es sein Ubuntu wie eine normale Applikation zu öffnen. Ihre Dateien können Sie im Dateienmanager unter `\\wsl.localhost\Ubuntu\home\<Username>` nachvollziehen, exportieren sowie andere Bearbeitungsschritte durchführen. Zusätzlich muss das **Repository**, in welchem die für die Installation benötigten Dateien hinterlegt sind, eingebunden und aktiviert werden. Die benötigte URL mit dem Code wird in einem Ordner `<src>` installiert. Dabei sollte auch immer wieder überprüft werden, ob ros2 noch auf dem neusten Stand ist.

