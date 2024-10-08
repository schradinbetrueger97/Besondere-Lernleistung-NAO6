# Benötigte Bestandteile

## Was wird alles benötigt
- manager
- publisher
- action client

## Manager_Node

### Funktion(allg.)
Die Manager-Node wird als zentrale Node genutzt. In dieser Node wird verwaltet welche Node wann angesprochen werden soll und über diese Node werden die zentralen Rechenprozesse durchgeführt.

### Aufbau
Die Manager-Node steuert die Publisher-Node an, wenn NAO sprechen soll und steuert die Subscriber-Node an wenn der NAO etwas hören soll. Beim Publisher wird eben diesem ein String gegeben, den dieser ausgibt. Bei der Subscriber_Node wird es so aufgebaut, dass der NAO diese Node aufruft, wenn der NAO der Person zuhören soll. Anschließend kriegt der NAO einen String, der hier in einen String-Wert einer bestimmten Variablen überführt wird. 

## Publisher_Node & Subscriber_Node

### Konzept

#### So allgemein wie möglich, so konkret wie nötig!
Das wichtige ist, dass nur eine Publisher und eine Subscriber Node geschrieben werden muss und diese dann jeweils nur ihrem konkreten Zweck dienen. Hier ist es vorteilhaft, dass über den Naoqi_driver bereits eine Text-to-Speech sowie eine Speech-to-Text zur Verfügung gestellt wird.

### Publisher_Node

Diese Node ist dadür da, dass der NAO sprechen kann. Dieser Node werden dafür jeweils bestimmte String-Werte zur Verfügung gestellt, die dann ein Mal ausgegeben werden.

### Subscriber_Node

Diese Node hat einzig und alleine den Zweck über die Mikrofone des NAO zuhören zu können und das Gehörte in Strings zu überführen. 