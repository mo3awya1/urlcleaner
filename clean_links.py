import re

def extract_links(data):
    """Extract and clean URLs from the given data."""
    # Regular expression pattern to match URLs
    url_pattern = r'https?://[a-zA-Z0-9./?=_-]+'
    # Find all matching URLs in the input data
    links = re.findall(url_pattern, data)
    # Clean links to remove trailing unwanted characters
    clean_links = [re.sub(r'[^\w/:.-]+$', '', link) for link in links]
    # Remove duplicates
    return list(set(clean_links))

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return ""
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return ""

def write_to_file(file_path, links):
    """Writes the list of links to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for link in links:
                file.write(link + '\n')
        print(f"Successfully written {len(links)} cleaned links to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")

# File paths
input_file = "domins.txt"  # Replace with your input file name
output_file = "all.txt"    # Replace with your desired output file name

# Read input file
data = read_file(input_file)

# Extract and clean links
if data:
    extracted_links = extract_links(data)
    # Write cleaned links to output file
    write_to_file(output_file, extracted_links)
else:
    print("No data to process.")
