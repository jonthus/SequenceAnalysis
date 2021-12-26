
from entities.dotplot import Dotplot
from plots.dotplot_plot import dotplot_plotting


def dotplot_run(file):
    """
    Ajaa ohjelman ja tallentaa tiedoston 'dotplot.png' kansioon 'input_files'.

    Args:
        file: tiedosto, josta luetaan dataa

    Returns:
        None
    """
    seq = Dotplot()
    first, second, data = seq.get_lengths(file)
    dotplot_plotting(first, second, data)


