from Bio import SeqIO


def file_type(filename):
    """
    Tarkistaa tiedoston tyypin.
    Args:
        filename
    Returns:
        True
        False

    """
    if filename.endswith(".txt"):
        return True
    else:
        return False


def is_fasta(filename):
    """
    Tarkistaa, onko tiedosto FASTA.

    Args:
        filename: tiedosto tarkistettavaksi

    Returns:
        False: jos tiedosto ei ole FASTA.

    """
    with open(filename, "r") as iteration:
        fasta = SeqIO.parse(iteration, "fasta")
        return any(fasta)
