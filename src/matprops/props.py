import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import math
import warnings

def AreaProp(dataset, col, cols=8, labels=True, label_loc="inc", labelcolor="blue", title=None, title_loc="tl", facecolor="blue", bgcolor="#707070", description=None):
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
    location_aspects = ["top", "bottom", "left", "right"]
    title_locations = {
        "tl": (0, 1.1, "left"),
        "tr": (1, 1.1, "right"),
        "bl": (0, -0.1, "left"),
        "br": (1, -0.1, "right"),
    }
    if len(dataset) > cols:
        rows = math.ceil(len(dataset) / cols)
    else:
        rows = 1
    fig = plt.figure(figsize=(18, 2 * rows))
    for index, row in dataset.iterrows():
        ax = fig.add_subplot(rows, cols, index + 1)
        ax.axvspan(0, 1, ymax=1, fc=bgcolor, alpha=0.1)
        ax.axvspan(0, row[col], ymin=0.01 , ymax=row[col], fc=matplotlib.colors.to_hex(facecolor)+"66", ec=facecolor)
        if labels:
            if label_loc == "inc":
                label_locations_reset = [row[col] / 2, row[col] / 2, "center", "center"]
            if label_loc == "inbl":
                label_locations_reset = [0, 0, "left", "bottom"]
            if label_loc == "inbr":
                label_locations_reset = [row[col], 0, "right", "bottom"]
            if label_loc == "intl":
                label_locations_reset = [0 + 0.02, row[col] - 0.02, "left", "top"]
            if label_loc == "intr":
                label_locations_reset = [row[col] - 0.02, row[col] - 0.02, "right", "top"]
            if label_loc == "outc":
                label_locations_reset = [row[col] + 0.05, row[col] + 0.05, "left", "top"]
            if label_loc == "outtl":
                label_locations_reset = [row[col] - 0.05, row[col] + 0.05, "right", "bottom"]
            if label_loc == "outtr":
                label_locations_reset = [row[col] + 0.05, row[col] - 0.1, "left", "bottom"]
            # label_locations_reset = __get_label_location(row[col], label_loc)
            ax.text(label_locations_reset[0], label_locations_reset[1], str(row[col] * 100) + "%", c=matplotlib.colors.to_hex(labelcolor),
                    fontsize=8, ha=label_locations_reset[2], va=label_locations_reset[3])
        if description is None:
            if title is not None:
                ax.text(title_locations[title_loc][0], title_locations[title_loc][1], row[title], fontweight="bold",
                        ha=title_locations[title_loc][2])

        else:
            if title is None:
                warnings.warn("Provide label column to get a better chart")
            else:
                max_char = 10
                max_row = 0
                for inner_index, inner_row in dataset.iterrows():
                    if len(inner_row[description]) > max_char:
                        temp = math.ceil(len(inner_row[description]) / max_char)
                        if temp > max_row:
                            max_row = temp
                    else:
                        max_row = 1
                max_des_rows = max_row
                # max_des_rows = __description_row_calculator(dataset, description, max_char=max_char)
                if title_loc == "tl" or title_loc == "tr":
                    if title_loc == "tl":
                        title_locations_reset = [title_locations[title_loc][0],
                                                 title_locations[title_loc][1] + max_des_rows / 10, "left"]
                    elif title_loc == "tr":
                        title_locations_reset = [title_locations[title_loc][0],
                                                 title_locations[title_loc][1] + max_des_rows / 10, "right"]
                    # title_locations_reset = __get_title_location(title_loc, max_des_rows)
                else:
                    title_locations_reset = [title_locations[title_loc][0], title_locations[title_loc][1],
                                             title_locations[title_loc][2]]
                ax.text(title_locations_reset[0], title_locations_reset[1], row[title], fontweight="bold",
                        ha=title_locations_reset[2], c="#000")
                if title_loc == "tl":
                    description_locations_reset = [title_locations[title_loc][0],
                                                   title_locations[title_loc][1] + max_des_rows / 10 - 0.1, "left"]
                elif title_loc == "tr":
                    description_locations_reset = [title_locations[title_loc][0],
                                                   title_locations[title_loc][1] + max_des_rows / 10 - 0.1, "right"]
                elif title_loc == "bl":
                    description_locations_reset = [title_locations[title_loc][0],
                                                   title_locations[title_loc][1] - 0.1, "left"]
                elif title_loc == "bl":
                    description_locations_reset = [title_locations[title_loc][0],
                                                   title_locations[title_loc][1] - 0.1, "right"]
                # description_locations_reset = __get_description_location(title_loc, max_des_rows)
                out_desc_list = [(row[description][i:i + max_char]) for i in
                                 range(0, len(row[description]), max_char)]
                for i in out_desc_list:
                    ax.text(description_locations_reset[0], description_locations_reset[1], i, fontweight="normal",
                            ha=description_locations_reset[2], c="#000")
                    description_locations_reset = [description_locations_reset[0],
                                                   description_locations_reset[1] - 0.1,
                                                   description_locations_reset[2]]
        ax.set(adjustable='box', aspect='equal')
        for s in location_aspects:
            ax.spines[s].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
    if rows > 1:
        fig.tight_layout()
    plt.show();

