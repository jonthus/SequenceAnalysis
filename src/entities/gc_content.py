
def percentages(sequence):
    """
    Funktio, joka laskee GC-% annetusta sekvenssistä.

    Args:
        sequence: sekvenssi, josta lasketaan.

    Returns:
        percent: percent * 100

    """
    guanine = sequence.count('G')
    cytosine = sequence.count('C')
    total = len(sequence)

    summa = guanine + cytosine
    percent = summa / total
    return percent * 100


def parsecontent(file):
    """
    Funktio lukee tiedoston ja tallentaa sen merkkijonoksi.
    Args:
        file: tiedosto luettavaksi

    Returns:
        data: tiedosto tallennettuna merkkijonoksi
    """
    data = ''
    with open(file, 'r', encoding="utf-8") as iteration:
        for i in iteration:
            if '>' in i:
                continue
            data += i.strip()
    return data


# EOF
