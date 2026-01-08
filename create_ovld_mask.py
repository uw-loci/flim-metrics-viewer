import re

# 1. Read pos_**** patterns from the first text file
with open('G:\\pdgfb3_restitch_imagenumber\\pdgfb3_tumorarea.txt', 'r') as f1:
    lines1 = f1.readlines()

# Use regex to extract 'pos_****' from each line
pos_patterns = []
for line in lines1:
    match = re.search(r'pos_\d{4}', line)
    if match:
        pos_patterns.append(match.group())

# 2. Open the second file and check for matches
with open('G:\\pdgfb_take3_photons\\removed_rows_ovld_scaled_tile_config_pdgfb_take3.txt', 'r') as f2:
    lines2 = f2.readlines()

# 3. Save matched rows to a new file
with open('G:\\pdgfb3_restitch_imagenumber\\matchedpdgfb3_tumorarea.txt', 'w') as outfile:
    for line in lines2:
        for pattern in pos_patterns:
            if pattern in line:
                outfile.write(line)
                break  # avoids writing the same line multiple times
