
import pickle
import pandas as pd

with open("output/study1_outputs_trimmed.pkl", "rb") as f:
    data = pickle.load(f)

# If it's a list of dicts (like yours), convert to DataFrame
df = pd.DataFrame(data)
print(df.head())
#print(df.iloc[0])
'''
# forgot to remove the first 7 rows of the original file, which contain testing outputs

import pandas as pd
import sys
import os
import pickle

def remove_first_rows(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    base, extension = os.path.splitext(filepath)
    new_filepath = f"{base}_trimmed{extension}"

    if ext == '.csv':
        existing_cols = pd.read_csv(filepath, nrows=0).columns.tolist()
        all_cols = existing_cols + ['input_tokens', 'output_tokens', 'time_sec']

        df = pd.read_csv(filepath, skiprows=range(1, 8), engine='python', names=all_cols, header=0)
        df.to_csv(new_filepath, index=False)
        print(f"Saved new file '{new_filepath}' with first 7 rows removed. Rows remaining: {len(df)}")

    elif ext == '.pkl':
        with open(filepath, 'rb') as f:
            data = pickle.load(f)

        if isinstance(data, pd.DataFrame):
            data.columns = data.columns.tolist()[:-3] + ['input_tokens', 'output_tokens', 'time_sec']
            data = data.iloc[7:]
            data.to_pickle(new_filepath)
        elif isinstance(data, list):
            data = data[7:]
            with open(new_filepath, 'wb') as f:
                pickle.dump(data, f)
        print(f"Saved new file '{new_filepath}' with first 7 rows removed. Rows remaining: {len(data)}")

    else:
        print(f"Unsupported file type: {ext}")
        sys.exit(1)


if __name__ == "__main__":
    remove_first_rows("output/study1_outputs.csv")
    remove_first_rows("output/study1_outputs.pkl")
'''