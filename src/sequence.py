import os
from Bio import SeqIO
import pylab

HIIRI_FILENAME = os.path.join(os.path.dirname(__file__), 'hiiri.txt')

class Sequence:
    """
    Sequence class for creating different tables.
    """

    def dotplot(self, file):
        """
        Function for creating a dotplot from two sequences.
        Prints True if succeeds.

        Args:
            file: file containing two sequences to be compared.

        Returns:
            True

        """
        with open(file) as iteration:
            temp = SeqIO.parse(iteration, "fasta")
            first = next(temp)
            second = next(temp)

        window = 7  # vaikuttaa tarkkuuteen
        first_seq = first.seq
        second_seq = second.seq
        data = [
            [(first_seq[i: i + window] != second_seq[j: j + window])
             for j in range(len(first_seq) - window)]
            for i in range(len(second_seq) - window)
        ]

        pylab.gray()
        pylab.imshow(data)
        pylab.xlabel("%s (length %i bp)" % (first.id, len(first)))
        pylab.ylabel("%s (length %i bp)" % (second.id, len(second)))
        pylab.title("Dot plot")
        pylab.show()
        return True

    def parse(self, file):  # tulee käyttöön muissa funktioissa
        """
        Function for parsing a file

        Args:
            file

        Returns:
            temp.read(): read file
        """

        temp = open(file, "r")
        return temp.read()

def run():
    # testi = "kasvi.txt"
    seq = Sequence()
    seq.dotplot(HIIRI_FILENAME)


if __name__ == "__main__":
    run()