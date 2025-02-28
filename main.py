import json

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

def convert_tsv_to_json(tsv_data):
    lines = [line for line in tsv_data.strip().split("\n") if line]
    headers = lines[0].split("\t")
    json_data = []
    
    for line in lines[1:]:
        values = line.split("\t")
        if len(values) != len(headers):
            continue  # Skip malformed lines
        entry = {headers[i]: values[i] for i in range(len(headers))}
        
        # Convert Hex to RGB list
        try:
            entry["rgb"] = hex_to_rgb(entry.get("Hex(RGB)", "#000000"))
        except ValueError:
            entry["rgb"] = [0, 0, 0]  # Default to black if conversion fails
        
        json_data.append(entry)
    
    return json.dumps(json_data, indent=4, separators=(',', ': '))

# Read data from a file
with open("colors.txt", "r", encoding="utf-8") as file:
    tsv_content = file.read()

json_output = convert_tsv_to_json(tsv_content)

# Save JSON to a file
with open("colors.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_output)

print("Conversion complete. JSON saved as colors.json")
