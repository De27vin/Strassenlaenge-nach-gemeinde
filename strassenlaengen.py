import numpy as np
import pandas as pd

df = pd.read_csv("daten-opendata-swiss.csv", sep=";")


kanton_sh = df[(df["GEO_CANT"] == "SH")]

print(len(kanton_sh))



# Auswertungsideen:
# Y = Länge der Strassen, X = Kantone (nach anzahl Strassen aufsteigend)
# Durchschnittslänge der Strassen aller Kantone


