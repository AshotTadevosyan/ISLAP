import re
from unidecode import unidecode

def normalize(name):
    name = name.lower().strip()                 # lowercase and trim
    name = unidecode(name)                      # remove accents
    name = re.sub(r"[^\w\s]", "", name)         # remove punctuation
    name = " ".join(sorted(name.split()))       # sort words alphabetically
    return name