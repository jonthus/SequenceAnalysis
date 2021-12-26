
from pathlib import Path
import pylab
PROJECT_ROOT = Path(__file__).parents[1]


def create_plot(bins, reads):
    """
    Luodaan histogrammi lasketuilla tiedoilla tiedostona 'histogram.png' kansioon 'output_files'.
    Args:
        bins: histogrammin tornien pituus
        reads: sekvenssien määrä
    Returns:
        None
    """

    pylab.figure(figsize=(10, 6), facecolor='white')

    pylab.xlim([0, max(reads) + 1])
    pylab.xlabel('Sequence length')
    pylab.ylabel('Number of sequences')

    pylab.hist(bins, reads, alpha=0.5, facecolor='red')

    pylab.suptitle("Length distribution", fontsize=16)
    pylab.savefig(PROJECT_ROOT / "output_files" / "histogram.png")

# EOF
