import json
with open('scrape.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for distro in data:
    print(distro['review'])
    
    
with open('pre.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for distro in data:
    print(distro['review'])
    
with open('pro.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for distro in data:
    print(distro['pont'])
    print(distro['stat'])


with open('rate.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for distro in data:
    print(distro['rating'])
