import os
import pandas as pd

# Define the paths to the two folders
folder_a = 'filesA'
folder_b = 'filesB'

# Get the list of files in both folders
files_a = set(os.listdir(folder_a))
files_b = set(os.listdir(folder_b))

# Find the common files in both folders
common_files = files_a.intersection(files_b)

if not common_files:
    print("No common files found in both folders.")
else:
    for file_name in common_files:
        file_a_path = os.path.join(folder_a, file_name)
        file_b_path = os.path.join(folder_b, file_name)
        
        try:
            # Read the CSV files
            df_a = pd.read_csv(file_a_path)
            df_b = pd.read_csv(file_b_path)
            
            # Get the columns from both files
            columns_a = set(df_a.columns)
            columns_b = set(df_b.columns)
            
            # Compare columns
            if columns_a != columns_b:
                print(f"\nMismatch found in file: {file_name}")
                
                missing_in_a = columns_b - columns_a
                missing_in_b = columns_a - columns_b
                
                if missing_in_a:
                    print(f"  Columns in {file_name} ({folder_b}) not in {folder_a}: {missing_in_a}")
                if missing_in_b:
                    print(f"  Columns in {file_name} ({folder_a}) not in {folder_b}: {missing_in_b}")
            else:
                print(f"{file_name} has matching columns.")
        
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
