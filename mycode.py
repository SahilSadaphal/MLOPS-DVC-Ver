import pandas as pd
import os

my_di = {
    "name": ["Sahil", "Kumar", "Jay"],
    "age": [23, 24, 23],
}
df = pd.DataFrame(my_di)

# Ensure the data directory exixts at root level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, "sample_data.csv")

# Save the dataframe
df.to_csv(file_path, index=False)
