import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# reads the laureates.csv file and defines it as f, saves the contents to a dictionary
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# takes the dictionary and looks for Einstein, once it finds it, it prints the results 
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
