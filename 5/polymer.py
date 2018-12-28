def get_polymer():
    with open('polymer.txt', 'r') as f:
        return f.read().strip()