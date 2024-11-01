import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("daten-opendata-swiss.csv", sep=";")


kantone = ["ZH", "BE", "LU", "UR", "SZ"]
laenge_laengste = [100, 150, 120, 130, 140]
laenge_durchschnitt = [80, 110, 90, 100, 95]
laenge_kuerzeste = [60, 70, 50, 65, 55]


fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(kantone, laenge_laengste, color='blue', marker='s')
ax.scatter(kantone, laenge_durchschnitt, color='green', marker='o')
ax.scatter(kantone, laenge_kuerzeste, color='red', marker='^')

plt.title("Strassenlängen")
plt.xlabel("Länge")
plt.ylabel("Kantone")

plt.legend(["Längste", "Durchschnitt", "Kürzeste"])
plt.show()

# Auswertungsideen:
# Y = Länge der Strassen (Längste, Kürzeste und Durchschnitt), X = Kantone (nach anzahl Strassen aufsteigend)


