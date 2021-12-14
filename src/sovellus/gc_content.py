
def percentages(sequence):
    """
    Function for calculating percentages from a given sequence.

    Args:
        sequence: sequence to be calculated

    Returns:
        percent: %

    """
    guanine = sequence.count('G')
    cytosine = sequence.count('C')
    total = len(sequence)

    summa = guanine + cytosine
    percent = summa / total
    return percent * 100


def parsecontent(file):
    """
    Function for parsing the content of the given file.
    Args:
        file: file to be parsed

    Returns:
        Percentage from percentage function.
    """
    data = ''
    with open(file, 'r') as iteration:
        for i in iteration:
            if '>' in i:
                continue
            data += i.strip()
    return percentages(data)


def run(file):
    """
    Runs the program.
    Args:
        file: file to be run

    Returns:
        Calculated %
    """
    return parsecontent(file)

# EOF
