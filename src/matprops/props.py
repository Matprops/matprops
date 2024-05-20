import matplotlib

from resources.configs.props import *
from resources.utils.props import *
from resources.utils.figure import *


def AreaProp(dataset, col, cols=8, labels=True, label_loc="inc", labelcolor="blue", title=None, title_loc="tl",
             facecolor="blue", bgcolor="#707070", description=None):
    """
    Square area proportional chart
    This function is used to create and customize almost everything in basic square area proportional chart
    Supports only for the percentages(proportions)
    The values of the columns should be between 0 and 1, which is considered as normal percentile.

    :parameter dataset: (pandas dataframe)
                    May hold a larger number of columns
                    including title, description and proportions
    :parameter col: (str)
                Column name for which the proportions to be visualized
    :param cols: (int, default=8)
                 Number of proportion square columns for a single row
    :param labels: (bool, default=True)
                   Bool value denoting the labels visibility
                   True: Visible
                   False: Invisible
    :param label_loc: (str, default="inc" - inner center)
                      String deciding the location of labels in individual props

                      Valid locations,
                      "inc" - inner center
                      "inbl" - inner bottom left
                      "inbr" - inner bottom right
                      "intl" - inner top left
                      "intr" - inner top right
                      "outc" - outer center
                      "outtl" - outer top left
                      "outtr" - outer top right
    :param labelcolor: (str, default="white")
                        Color of the label
                        All hex values, and default color code in matplotlib are supported
    :param title: (str, default=None)
                  Column name of the dataset denoting the title of each prop
                  Each row should be associated with the proportions directly
    :param title_loc: (str, default="tl")
                      String deciding the location of labels in individual props

                      Valid locations,
                      "tl" - top left
                      "tr" - top right
    :param facecolor: (str, default="black")
                      Color of the square prop
                      All hex values, and default color code in matplotlib are supported
    :param bgcolor: (str, default="black")
                    Background color of the props
                    All hex values, and default color code in matplotlib are supported
    :param description: (str, default=None)
                        Column name of the dataset denoting the description of each prop
                        Each row should be associated with the proportions directly
    :return: A square area proportional chart
    """

    # Proportional chart initialize
    prop = PropInit(dataset, cols)
    fig = prop.initialize_figure()

    if fig:
        # Proportional chart configurations
        pConfig = PropConfig(dataset, title, title_loc, labels, label_loc, col, description)

        for index, row in dataset.iterrows():
            ax = fig.add_subplot(prop.max_rows, cols, index + 1)

            ax.axvspan(0, 1, ymax=1, fc=bgcolor, alpha=0.1)
            ax.axvspan(0, row[col], ymin=0.01, ymax=row[col], fc=matplotlib.colors.to_hex(facecolor) + "4D",
                       ec=facecolor)

            if pConfig.title is not None:
                ax.text(pConfig.title_layout[0],
                        pConfig.title_layout[1],
                        row[title],
                        fontweight="bold",
                        ha=pConfig.title_layout[2],
                        c="#000")

            if pConfig.description is not None:
                max_char_per_row = 15
                temp_description_layout = pConfig.description_layout
                out_desc_list = [(row[description][i:i + max_char_per_row]) for i in
                                 range(0, len(row[description]), max_char_per_row)]
                for i in out_desc_list:
                    ax.text(temp_description_layout[0],
                            temp_description_layout[1],
                            i,
                            fontweight="normal",
                            ha=pConfig.description_layout[2],
                            c="#000")
                    temp_description_layout = [temp_description_layout[0],
                                               temp_description_layout[1] - 0.1,
                                               temp_description_layout[2]]

            if pConfig.labels:
                pConfig.get_label_layout(row)
                ax.text(pConfig.label_layout[0],
                        pConfig.label_layout[1],
                        str(row[col] * 100) + "%",
                        c=matplotlib.colors.to_hex(labelcolor),
                        fontsize=7,
                        ha=pConfig.label_layout[2],
                        va=pConfig.label_layout[3])
            set_axis(ax)

        if prop.max_rows > 1:
            fig.tight_layout()
        plt.show();
    else:
        raise Exception("Exception occurred")
