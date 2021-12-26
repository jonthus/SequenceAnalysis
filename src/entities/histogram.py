import numpy as np
from Bio import SeqIO


class Histogram:
    """
    Luokka histogrammin luomiseen.
    """

    def calculate_lengths(self, file):
        """
        Lasketaan FASTA-tiedostosta sekvenssien pituudet.
        Args:
            file: tiedosto, josta luetaan.
        Returns:
             lengths: pituudet
        """

        lengths = []
        iters = SeqIO.parse(file, "fasta")
        for i in iters:
            lengths.append(len(i.seq))
        return lengths

    def calculate_bins(self, lengths):
        """
        Lasketaan sekvenssien pituuksista bins histogrammin 'tornien' pituudet.
        Args:
            lengths: sekvenssien pituudet taulukkona
        Returns:
            bins: tornien pituudet
        """
        percentage = 1 / (100 * 1.0)
        size = int(percentage * max(lengths))
        bins = np.arange(0, max(lengths) + 1, size)
        return bins

# EOF
