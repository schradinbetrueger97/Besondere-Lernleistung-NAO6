# <u>ReadMe NAO</u>

Diese Dokumentation dient dem Aufzeigen meiner Arbeitsergebnisse und -fortschritte während der praktischen Phase sowie dem Übermitteln meiner Erfahrungen an nachfolgende Personen, die gewillt sind sich selbst auch mit dem NAO in erweiterter Form zu befassen.

Bei meiner Dokumentation werden die Erfahrungen mit dem NAO und die Nutzung der Linux-Distribution **Ubuntu** genutzt. Als ros Distribution nutze ich dabei in der Linux-Applikation **iron**.

## Installation WSL und Ubuntu


Der erste Arbeitsschritt ist, wenn man mit einem Windows Betriebssystem arbeitet, die Installation eines Windows Subsystem for Linux(WSL), damit das Dateisystem von Linux sowie die Befehle genutzt werden können. Unter dem folgenden Link können Sie die Installation von WSL nachvollziehen.


```ssh
https://learn.microsoft.com/de-de/windows/wsl/install
```

Achten Sie bitte bei der Installation darauf Powershell als Administrator auszuführen, um mögliche Komplikationen bei der Installation zu vermeiden. Anschließend muss auch noch eine Linux-Distribution in WSL selbst installiert werden. Dabei habe ich die gängigste Distribution mit ==== genutzt. Nutzen Sie dafür bitte den folgenden Befehl.

```
wsl --install -d
```


Die erfolgreiche Installation kann mit `wsl -l -v` überprüft werden.


### Wichtig!


bei den Code-Blöcken und den anderen Code-Bestandteilen werden in der Regel keine Vergleichszeichen mitgeschrieben. Diese dienen im Text zur klaren Abgrenzung und in den Code-Blöcken zum Markieren, derjenigen Stellen die bearbeitet werden müssen.

