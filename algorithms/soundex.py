def soundex(name):
    name = name.upper()
    soundex_map = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2',
        'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

    if not name:
        return "0000"

    first_letter = name[0]
    encoded = first_letter

    for char in name[1:]:
        code = soundex_map.get(char, '0')
        if code != encoded[-1]:
            encoded += code

    encoded = encoded.replace('0', '')
    encoded = (encoded + '000')[:4]
    return encoded

def soundex_score(name1, name2):
    return 1.0 if soundex(name1) == soundex(name2) else 0.0
