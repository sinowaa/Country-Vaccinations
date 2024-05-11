import pandas as pd
df = pd.read_csv("filled_country_vaccination_stats.csv")
df['daily_vaccinations'] = pd.to_numeric(df['daily_vaccinations'], errors='coerce')
median_daily_vaccinations = df.groupby('country')['daily_vaccinations'].median()
top_3_countries = median_daily_vaccinations.sort_values(ascending=False).head(3)
print("Top 3 countries with highest median daily vaccination numbers:")
for country, median_vaccinations in top_3_countries.items():
    print(f"{country}: {median_vaccinations}")