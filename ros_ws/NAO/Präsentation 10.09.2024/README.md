# Präsentation 10.09.2024

## Begrüßung Publikum

## Was möchte ich in der BeLL erreichen?

- Programmierung NAO für Gesundheitspflege
- primär gegen Vereinsamung von alten Personen, die immer öfters nur eingeschränkte soziale Kontakte haben

## Wie bin ich an "Dankeschönveranstaltung NAO_Sponsoren" herangegangen

- überlegt was ich vorstellen möchte und dann dazu einen Ablauf skizziert
- Ablauf Programme skizziert mit Hilfe von Diagrammen

## Diagramm zeigen Ablauf Programm

- Gesichts und Gesprächserkennung NAO wie es unstrukturiert ist
- Gesprächserkennung wie es sortiert und kohärent aussieht

## Programmbausteine und Veränderung zeigen in Ubuntu

### Verbindung zu NAO aufbauen

#### In den richtigen Workspace navigieren

```sh
cd workspaces/ros_ws
```

#### Umgebung sourcen

```sh
source /opt/ros/humble/setup.bash
source install/setup.bash
```

#### Verbindung zu NAO aufbauen

ros2 launch naoqi_driver naoqi_driver.launch.py nao_ip:=10.200.199.34 qi_listen_url:=tcp://0.0.0.0:0

#### NAO sagt was ich jetzt mit ihm mach

```sh
ros2 topic pub --once /speech std_msgs/String "{data: 'Hallo ich bin NAO und mit mir wird jetzt gezeigt wie ich auch anders als mit der grafischen Programmierung gecoded werden kann'}"
```

#### NAO bewegt Kopf nach Rechts
ros2 topic pub --once /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed "{header: {stamp: now, frame_id: ''}, joint_names: ['HeadYaw', 'HeadPitch'], joint_angles: [1.0,0.0], speed: 0.1, relative: 0}"

#### NAO bewegt Kopf nach Links
ros2 topic pub --once /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed "{header: {stamp: now, frame_id: ''}, joint_names: ['HeadYaw', 'HeadPitch'], joint_angles: [-1.0,0.1], speed: 0.1, relative: 0}"

#### NAO bewegt Kopf nach Oben
ros2 topic pub --once /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed "{header: {stamp: now, frame_id: ''}, joint_names: ['HeadYaw', 'HeadPitch'], joint_angles: [0.0,1.0], speed: 0.1, relative: 0}"

#### NAO geht ein paar Schritte
```sh
ros2 topic pub --once /cmd_vel geometry_msgs/Twist "linear:
  x: 0.1
  y: 0.1
  z: 0.1
angular:
  x: 0.0
  y: 0.0
  z: 0.0"
```

#### NAO bricht Laufen ab
```sh
ros2 topic pub --once /cmd_vel geometry_msgs/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0"
```

#### NAO hebt rechten Arm
```sh

```

#### NAO hebt linken Arm
```sh

```

## optional wenn publisher klappt

- Struktur annähernd erklären
- Ablauf, wofür ist was zuständig(ALLGEMEIN)

## warum ros2 mit naoqidriver so cool

- nahezu grenzenlose Programmierung mit der Ros Umgebung
- universelle Roboter-Programmierung
- es können mit diesen Programmen auch andere Roboter genutzt werden

## letzte Worte NAO

- Abschließend bedanke ich mich für die Aufmerksamkeit und ich glaube der NAO hat auch gleich nochmal was zu sagen
```sh
ros2 topic pub --once /speech std_msgs/String "{data:'Ich bedanke mich auch, dass Sie mir ermöglicht haben mit solchen netten und interessierten Personen arbeiten zu dürfen. Auf Wiedersehen.'}"
```