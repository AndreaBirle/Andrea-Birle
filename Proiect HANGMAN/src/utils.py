import csv
import unicodedata

def read_csv(path):
    """Citește CSV cu antet și returnează listă de dicționare."""
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(path, data):
    """Scrie listă de dicționare într-un CSV."""
    if not data:
        return
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def normalize(word):
    """Transformă în lowercase și elimină diacritice pentru comparații."""
    word = word.strip().lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )














