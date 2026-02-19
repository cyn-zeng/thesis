import pickle
import pandas as pd

with open("output/study1_outputs.pkl", "rb") as f:
    data = pickle.load(f)

# If it's a list of dicts (like yours), convert to DataFrame
df = pd.DataFrame(data)
print(df.head())
#print(df.iloc[0])