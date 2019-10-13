from fuzzywuzzy import fuzz
from fuzzywuzzy import process

query = 'geeks for geeks'
choices = ['geek for geek', 'geek geek', 'g. for geeks']

# Get a list of matches ordered by score, default limit to 5
process.extract(query, choices)

# If we want only the top one
process.extractOne(query, choices)

print(process.extractOne(query, choices))
