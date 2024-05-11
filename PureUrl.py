import pandas as pd
import re
df = pd.read_csv("data.csv")
pattern = r'<url>(?:https?://)?([a-z0-9._]+)</url>'
df['Pure_URL'] = df['Stats_Access_Link'].str.extract(pattern, flags=re.IGNORECASE)
print(df)