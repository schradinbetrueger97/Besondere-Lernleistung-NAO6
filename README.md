# <u>ReadMe NAO</u>

Diese Dokumentation dient dem Aufzeigen meiner Arbeitsergebnisse und -fortschritte während der praktischen Phase sowie dem Übermitteln meiner Erfahrungen an nachfolgende Personen, die gewillt sind sich selbst auch mit dem NAO in erweiterter Form zu befassen.

Bei meiner Dokumentation werden die Erfahrungen mit dem NAO und die Nutzung der Linux-Distribution **Ubuntu** aufgezeigt. Als ros Distribution nutze ich dabei in Ubuntu **humble**.

## Installation WSL und Ubuntu


Der erste Arbeitsschritt ist, wenn man mit einem Windows Betriebssystem arbeitet, die Installation eines Windows Subsystem for Linux(WSL), damit das Dateisystem von Linux sowie die Befehle genutzt werden können. Unter dem folgenden Link können Sie die Installation vom WSL nachvollziehen.

```sh
https://learn.microsoft.com/de-de/windows/wsl/install
```

Achten Sie bitte bei der Installation darauf Powershell als Administrator auszuführen, um mögliche Komplikationen bei der Installation zu vermeiden. Anschließend muss auch noch eine Linux-Distribution in WSL selbst installiert werden. Hierbei habe ich die gängigste Distribution mit `<Ubuntu 20.04 2>` installiert. Nutzen Sie dafür bitte den folgenden Befehl.

```sh
wsl --install -d
```

Die erfolgreiche Installation kann mit `wsl -l -v` überprüft werden.

>Bei den Code-Blöcken und den anderen Code-Bestandteilen werden in der Regel keine Vergleichszeichen mitgeschrieben. Diese dienen im Text zur klaren Abgrenzung und in den Code-Blöcken zum Markieren, derjenigen Stellen die bearbeitet werden müssen.

## Installation ros2 humble

>Suchen Sie sich im besten Fall online ein sogenanntes "cheat sheet" zu den Befehlen im Umgang mit einem Linux Subsystem heraus. In diesem Dokument können Sie die grundlegenden Befehle schnellstmöglich finden. Unter dem folgenden Link finden Sie das cheat sheet, welches ich nutze.

```sh
https://cheatography.com/davechild/cheat-sheets/linux-command-line/
```

### Grundlagen für Installation

Für die folgenden Schritte wird Ubuntu genutzt. Dafür sollte es sein Ubuntu wie eine normale Applikation zu öffnen. Ihre Dateien können Sie im Dateienmanager unter `\\wsl.localhost\Ubuntu\home\<Username>` nachvollziehen, exportieren sowie andere Bearbeitungsschritte durchführen. Zusätzlich muss das **Repository**, in welchem die für die Installation benötigten Dateien hinterlegt sind, eingebunden und aktiviert werden. Die benötigte URL mit dem Code wird in einem Ordner `<src>` installiert. Dabei sollte auch immer wieder überprüft werden, ob ros2 noch auf dem neusten Stand ist.

### Tutorial ros2(turtlesim)


Für den Einstieg und das Verstehen, wie die Programmierung in ros2 funktioniert empfiehlt sich das Turtlesim-Tutorial. Bei eben diesem arbeitet man mit einer grafische Wiedergabe und sieht direkt, was man macht. Überdies wird man gut in die **CLI Basic Concepts** eingeführt.


## CLI Basic Concepts


Im folgenden werden die einzelnen Bestandteile der Programmierung beschrieben und schematisch gezeigt.


### Nodes



### Topics



### Services



### Parameters



### Actions



## Installation naoqi_driver2

Die Installation kann im Genauen unter folgenden Link nachvollzogen werden.

```sh
https://github.com/K4belBr4nd/naoqi_driver2
```

### Funktionsweise

Der naoqi_driver2 dient als Schnittstelle zwischen ros und dem naoqi_systems des Robters. Also stellt sich der driver als Node dar.

Ich selbst beziehe mich bei meinem Projekt auf die Installation aus der Quelle. 

Als erstes gehen Sie in Ihr workspace-directory. Anschließend installieren Sie die im naoqi-repository hinterlegten Pakete mit dem folgenden Befehl in Ubuntu.

```sh
sudo apt-get install ros-<distro>-naoqi-libqi ros-<distro>-naoqi-libqicore ros-<distro>-naoqi-bridge-msgs ros-<distro>-pepper-meshes ros-<distro>-nao-meshes
```
Diese Pakete müssen noch in dein Workspace "geladen" werden. Dafür gehst du in den `<src>` Ordner und führst folgende Befehle durch.

```sh
git clone https://github.com/K4belBr4nd/naoqi_driver2.git
vcs import < naoqi_driver2/dependencies.repos
```

Wenn Sie anschließend wieder in Ihrem `</ros_ws>` sind, installieren Sie mit dem folgenden Befehl die restlichen Paket-Abhängigkeiten.

```sh
rosdep install --from-paths src --ignore-src --rosdistro <distro> -y
```

In Folge dessen wird der workspace komplett erstellt.

```
colcon build --symlink-install
```

Um den naoqi_driver2 komplett nutzen zu dürfen wird der folgende Befehl benötigt. Nur notwendig, wenn `"vcs import..."` genutzt wurde.

```sh
I_AGREE_TO_NAO_MESHES_LICENSE=1 I_AGREE_TO_PEPPER_MESHES_LICENSE=1 colcon build --symlink-install
```

Wenn diese Installation durchgeführt wurde kann es trotzdem noch zu Komplikationen mit dem Windows-Betriebssystem und der hinterlegten firewall kommen.

### Mein Fehler

Ich habe bei der versuchten Verbindung mit dem NAO eine Fehlermeldung erhalten und wurde deshalb in der Verbindung unterbrochen. Das Problem ist dabei die wahrscheinlich die firewall von Windows, die das audio-feature blockiert. In dem folgenden Link wird der genau selbe Fehler wie bei mir beschrieben.

```sh
https://github.com/ros-naoqi/naoqi_driver/issues/96
```

Das Problem kann entweder behoben werden, indem der Audioservice deaktiviert wird oder eine Bridge eingebaut wird.

### 1. Deaktivierung Audio-Service

Die Deaktivierung kann unter `src/naoqi_driver2/share/boot_config.json` vorgenommen werden. Sie müssen dabei `Audio enabled` von `false` auf `true` umstellen.
**Das Problem dabei ist, dass Sie in den Programmen, die Sie ausführen wollen beschränkt sind.**

### 2. Aktivierung und Integration Bridge

Das Problem kann auch umgangen werden, indem eine Bridge installiert und integriert wird. Nutzen Sie dabei das folgende Tutorial.

>Bei mir war der einzige Unterschied, dass wie im Tutorial beschrieben der Netzwerkmodus als `<bridged>` nicht funktioniert hat, sondern auf `<mirrored>` umgestellt werden muss.

```sh
https://medium.com/@petrousov/how-to-brigde-windows-subsystem-for-linux-0dc55a406a3b
```
Beachten Sie dabei bitte, dass Sie das Dokument auch wirklich in ihrem Benutzer-Profil hinterlegen/speichern und nicht in ihrem workspaces wie es bis jetzt für die anderen Pakete und Datein war.

## Programmierung

### Problemstellung



### Ablauf Programm



### benötigte Bestandteile



### Umsetzung und Erfahrungen


