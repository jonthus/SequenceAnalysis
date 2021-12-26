
from entities import histogram
from plots.histogram_plot import create_plot


def histogram_run(file):
    """
    Ajaa ohjelman histogrammin tulostamiseen..

    Args:
        file: tiedosto, josta luetaan dataa

    Returns:
        None
    """
    histo = histogram.Histogram()
    reads = histo.calculate_lengths(file)
    bins = histo.calculate_bins(reads)
    create_plot(bins, reads)

