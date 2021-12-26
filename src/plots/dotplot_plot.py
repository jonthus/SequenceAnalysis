
from pathlib import Path
import pylab
PROJECT_ROOT = Path(__file__).parents[1]


def dotplot_plotting(first, second, data):
    """
    Luo annetusta datasta dotplotin.
    Args:
        first: ensimmäinen sekvenssi
        second: toinen sekvenssi
        data: sekvensseistä laskettu samankaltaisuus
    Returns:
        None
    """
    pylab.gray()
    pylab.imshow(data)
    pylab.xlabel("%s (length %i bp)" % (first.id, len(first)))
    pylab.ylabel("%s (length %i bp)" % (second.id, len(second)))
    pylab.title("Dot plot")
    pylab.savefig(PROJECT_ROOT / 'output_files' / 'dotplot.png')

# EOF
