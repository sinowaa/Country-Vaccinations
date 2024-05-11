import pandas as pd
df = pd.read_csv("country_vaccination_stats.csv")
df['daily_vaccinations'] = pd.to_numeric(df['daily_vaccinations'], errors='coerce')
df['daily_vaccinations'] = df.groupby('country')['daily_vaccinations'].transform(lambda x: x.fillna(0))
df.to_csv("filled_country_vaccination_stats.csv", index=False)