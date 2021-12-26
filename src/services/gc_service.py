
from entities import gc_content


def gc_run(file):
    """
    Ajaa ohjelman ja palauttaa gc_content palauttaman prosenttiluvun.

    Args:
        file: tiedosto, josta luetaan dataa

    Returns:
        Gc_content laskeman prosenttiluvun annetusta tiedostosta.
    """
    data = gc_content.parsecontent(file)
    percentage = gc_content.percentages(data)
    return percentage
