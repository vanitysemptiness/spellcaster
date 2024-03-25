import csv
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['localhost'])

with open('pokemon.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        es.index(index='pokemon_stats', body=row)

from PyPDF2 import PdfReader

reader = PdfReader('pokemon_cards.pdf')
text = ''
for page in reader.pages:
    text += page.extract_text()

query = {
    'query': {
        'multi_match': {
            'query': 'charmander',
        }
    }
}

results = es.search(index='pokemon_stats', body=query)

print(f"Found {len(results['hits']['hits'])} results for 'charmander':")
for hit in results['hits']['hits']:
    print(f"- {hit['_source']['name']}")