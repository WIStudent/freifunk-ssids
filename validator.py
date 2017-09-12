import json
import sys
import os

path = sys.argv[1]
if not os.path.exists(path):
    sys.exit("File " + path +  " does not exist!")

# Test parsing json file
try:
    with open(path, 'r') as json_file:
        json_data = json.load(json_file)
except json.JSONDecodeError:
    sys.exit("Invalid JSON!")

# Test version number
try:
    version_number = json_data['version']
except KeyError:
    sys.exit('Field "version" is missing!')

if not isinstance(version_number, int):
    sys.exit('Field "version" does not contain an integer!')

# Test ssids array
try:
    ssids = json_data['ssids']
except KeyError:
    sys.exit('Field "ssids" is missing!')

if not isinstance(ssids, list):
    sys.exit('Field "ssids" does not contain an array!')

for ssid in ssids:
    if not isinstance(ssid, str):
        sys.exit('SSID {} is not a string!'.format(ssid))


# Test deprecated array
try:
    deprecated_ssids = json_data['deprecated']
except KeyError:
    sys.exit('Field "deprecated" is missing!')

if not isinstance(deprecated_ssids, list):
    sys.exit('Field "deprecated" does not contain an array!')

for ssid in deprecated_ssids:
    if not isinstance(ssid, str):
        sys.exit('Deprecated SSID {} is not a string!'.format(ssid))

print('{} SSIDs found.'.format(len(ssids)))
print('{} deprecated SSIDs found.'.format(len(deprecated_ssids)))
print('Validation complete!')