import pandas as pd

# https://chirp.danplanet.com/attachments/3271/Satellites.csv
dataFrame = pd.read_csv('scripts/solar_system/csv/planets.csv')
print(dataFrame[:10])
