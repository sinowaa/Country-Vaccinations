import pandas as pd
df = pd.read_csv("filled_country_vaccination_stats.csv")
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
total_vaccinations_on_01062021 = df[df['date'] == '2021-01-06']['daily_vaccinations'].sum()
print(total_vaccinations_on_01062021)