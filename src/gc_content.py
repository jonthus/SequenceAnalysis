
import os

HIIRI_FILENAME = os.path.join(os.path.dirname(__file__), 'hiiri.txt')

def percentages(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    total = len(sequence)

    summa = g + c
    percent = summa / total
    return percent * 100


def parseContent(file):
    data = ''
    with open(file, 'r') as f:
        for i in f:
            if '>' in i:
                continue
            data += i.strip()
    print(data)
    return percentages(data)


def run():
    print('Tiedoston GC-% on', parseContent(HIIRI_FILENAME))


if __name__ == '__main__':
    run()

# EOF
