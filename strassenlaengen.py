import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("daten-opendata-swiss.csv", sep=";")

daten_pro_kanton = df.groupby("GEO_CANT")["VALUE"].agg(["max", "mean", "min"]).reset_index()

kantone = daten_pro_kanton["GEO_CANT"]
laenge_laengste = daten_pro_kanton["max"]
laenge_durchschnitt = daten_pro_kanton["mean"]
laenge_kuerzeste = daten_pro_kanton["min"]

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(kantone, laenge_laengste, color='blue', marker='s')
ax.scatter(kantone, laenge_durchschnitt, color='green', marker='o')
ax.scatter(kantone, laenge_kuerzeste, color='red', marker='^')

plt.title("Strassenlängen")
plt.xlabel("Kantone")
plt.ylabel("Länge der Strassen")

plt.legend(["Längste", "Durchschnitt", "Kürzeste"])
plt.show()

# Auswertungsideen:
# Y = Länge der Strassen (Längste, Kürzeste und Durchschnitt), X = Kantone (alphabetische Reihenfolge)


