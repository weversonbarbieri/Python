import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sea
import missingno as msno

df = pd.read_excel(r"C:\kpis_race.xlsx")

grip_factors = [
     "Grip Factor Aero KPI (G)",
     "Grip Factor Braking KPI (G)",
     "Grip Factor Cornering KPI (G)",
     "Grip Factor Traction KPI (G)",
     "Grip Factor Overall KPI (G)",
]

df[grip_factors].describe().round(2)







