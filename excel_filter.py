import pandas as pd
import json

def excel_filter_to_json(file_path, sheet_name, filter_column):
    """
    Loads an Excel sheet, filters data where filter_column equals 'COL_TO_EXTRACT',
    and returns the filtered data as JSON.
    
    Args:
        file_path (str): Path to the Excel file
        sheet_name (str): Name of the sheet to load
        filter_column (str): Column name to filter on
    
    Returns:
        str: JSON string of filtered data
    """
    try:
        # Load the specified sheet from the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Filter rows where the specified column equals 'COL_TO_EXTRACT'
        filtered_df = df[df[filter_column] == 'COL_TO_EXTRACT']
        
        # Convert the filtered DataFrame to JSON
        json_data = filtered_df.to_json(orient='records', indent=4)
        
        # Print the JSON data
        print("Filtered Data as JSON:")
        print(json_data)
        
        return json_data
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as e:
        print(f"Error: {str(e)}")
        return None
    except KeyError:
        print(f"Error: Column '{filter_column}' not found in the sheet.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None


def filter_excel_data(file_path, sheet_name, filter_column='X', filter_value='COL_TO_EXTRACT'):
    try:
        # Load the specified sheet from the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Filter the dataframe based on column X == 'COL_TO_EXTRACT'
        filtered_df = df[df[filter_column] == filter_value]

        # Convert filtered dataframe to JSON
        result_json = filtered_df.to_json(orient='records', force_ascii=False)

        # Print the JSON data
        print(result_json)

        # Optionally return it as a Python object (list of dictionaries)
        return json.loads(result_json)

    except Exception as e:
        print(f"Error: {e}")
        return None


def filter_excel_data_g(file_path, sheet_name, filter_column='X', filter_value='COL_TO_EXTRACT'):
    try:
        # Load the specified sheet from the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Filter the dataframe based on column X == 'COL_TO_EXTRACT'
        filtered_df = df[df[filter_column] == filter_value]

        # Convert filtered dataframe to JSON
        result_json = filtered_df.to_json(orient='records', force_ascii=False)

        # Print the JSON data
        print(result_json)

        # Optionally return it as a Python object (list of dictionaries)
        return json.loads(result_json)

    except Exception as e:
        print(f"Error: {e}")
        return None



def load_filter_excel_to_json(file_path, sheet_name, filter_column, filter_value):
    # Load the specific sheet from the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Filter rows where the filter_column equals filter_value
    filtered_df = df[df[filter_column] == filter_value]
    
    # Print the filtered DataFrame
    print(filtered_df)
    
    # Convert the filtered DataFrame to JSON string
    json_result = filtered_df.to_json(orient='records')  # 'records' gives a list of dicts
    
    return json_result


def filter_excel_sheet(excel_file, sheet_name, filter_column, filter_value):
    # Load the Excel file
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    # Filter the data based on the specified column and value
    filtered_data = df[df[filter_column] == filter_value]
    
    # Convert the filtered data to JSON
    filtered_data_json = filtered_data.to_json(orient='records')
    
    # Print the filtered data
    print(filtered_data)
    
    return filtered_data_json


# Example usage
if __name__ == "__main__":
    # Replace these with your actual file path, sheet name, and column name
    excel_file = "your_file.xlsx"
    sheet = "your_sheet_name"
    column_to_filter = "your_column_name"  # e.g., "Type" or "Category"
    
    # Call the function
    result_json = excel_filter_to_json(excel_file, sheet, column_to_filter)
    
    # You can now use result_json as needed
    if result_json:
        print("\nProcessing completed successfully!")