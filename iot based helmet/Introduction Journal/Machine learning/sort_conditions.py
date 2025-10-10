import pandas as pd

# Read the CSV file
input_path = r"e:\research paper\Machine learning\road_conditions.csv"
df = pd.read_csv(input_path)

# Define the desired order for conditions
condition_order = ["Excellent", "Good", "Poor", "Very Poor"]

# Sort the DataFrame by condition order
# If any condition is not in the list, it will be placed at the end
condition_cat = pd.Categorical(df['condition'], categories=condition_order, ordered=True)
df['condition'] = condition_cat
sorted_df = df.sort_values('condition')

# Save the sorted DataFrame to a new CSV file
output_path = r"e:\research paper\Machine learning\road_conditions_sorted.csv"
sorted_df.to_csv(output_path, index=False)

print(f"Sorted CSV saved to {output_path}")
