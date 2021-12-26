from Bio import SeqIO


class Dotplot:
    """
    Luokka dotplotin luomiseen.
    """

    def get_lengths(self, file):
        """
        Metodi, joka laskee sekvenssien pituudet annetusta tiedostosta.

        Args:
            file: tiedosto, josta luetaan dataa.

        Returns:
            first: ensimmäinen sekvenssi
            second: toinen sekvenssi
            data: sekvenssidata

        """
        with open(file, encoding="utf-8") as iteration:
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
        return first, second, data


# EOF
