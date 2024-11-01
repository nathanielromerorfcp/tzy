import re

def extract_uid(url):
    # Define the regex pattern to match the uid
    pattern = r"https://www\.facebook\.com/profile\.php\?id=(\d+)"
    match = re.search(pattern, url)
    
    if match:
        uid = match.group(1)
        return uid
    else:
        return None

def process_links(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            url = line.strip()  # Remove any leading/trailing whitespace
            uid = extract_uid(url)
            if uid:
                outfile.write(f"{uid}\n")  # Write the extracted UID to the output file

# Specify input and output files
input_file = 'link.txt'
output_file = 'uid.txt'

# Process the links
process_links(input_file, output_file)

print("UID extraction complete. Check uid.txt for results.")
