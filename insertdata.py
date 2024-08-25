import csv

# Path to your CSV file and the output TypeScript file
csv_file_path = 'data.csv'  # Replace with your actual CSV file path
output_file_path = 'data.ts'

# Starting ID
starting_id = 636

# Function to convert a row into the desired TypeScript format
def format_data(row, current_id):
    supported_payment = row['supportedPayment'].split(';') if row['supportedPayment'] else []

    if row['coords']:
        coords = row['coords'].split(',')
        lat, lng = coords[0], coords[1]
    else:
        lat, lng = '0.0', '0.0'  # Default or fallback values if coords are missing
    return f"""  {{
    id: {current_id},
    name: "{row['name']}",
    category: "{row['category']}",
    state: "{row['state']}",
    city: "{row['city']}",
    qrImage: "{row['qrImage']}",
    qrContent: "{row['qrContent']}",
    supportedPayment: {supported_payment},
    coords: [{lat},{lng}],
  }},"""

# Read the CSV and write to the TypeScript file
with open(csv_file_path, mode='r') as csv_file, open(output_file_path, mode='w') as ts_file:
    reader = csv.DictReader(csv_file)
    
    ts_file.write('[\n')  # Start of the TypeScript array
    
    current_id = starting_id
    for row in reader:
        formatted_data = format_data(row, current_id)
        ts_file.write(f"{formatted_data}\n")
        current_id += 1  # Increment the ID for the next entry
    
    ts_file.write(']')  # End of the TypeScript array

print(f"Data has been successfully written to {output_file_path}")
