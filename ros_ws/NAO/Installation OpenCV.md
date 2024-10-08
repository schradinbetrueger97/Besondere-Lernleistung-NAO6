# Installation OpenCV

## Was ist OpenCV?

Eine freie Programmbibliothek mit Algorithmen für die Bildverarbeitung und wied der Name verrät die **Computer Vision**.

## Funktion OpenCV *face recognition & detection*

Es wird an Stelle einer direkten Zuweisung was das für ein Bild ist ein Vektor erstellt. Dieser Vektor ist für das vorgelernte **deep metric learning** ein elementarer Bestandteil. Bei diesem Verfahren werden zu den Bildern 128-Dimensionale Vektoren gebildet. Damit wird das Gesicht in 128 einzelne Werte aufgeteilt. Anschließend wird geschaut an den Werten, welchen Bildes die Werte am nächsten dran sind.

### Bedeutung

Für die Inbetriebnahme ist es wichtig, dass in der Theorie die genauste Gesichtserkennung mit so vielen Bildern wie möglich besteht. Somit bräuchte man eine dementsprechend große Datenbank um eine geiwsse Sichherheit zu gewährleisten. 

## Installation face recognition libraries

Die benötigten Bibliotheken:

- dlib
- face_recognition

Die **dlib** Bibliothek wird von Davis King geführt und enthält gleichzeitig das **deep metric learning**. Die **face_recognition** Bibliothek hingegen wurde von Adam Geitgey erstellt und dient dazu die Arbeit mit **dlib** zu vereinfachen.

