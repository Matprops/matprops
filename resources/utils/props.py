import math
import matplotlib.pyplot as plt


class PropInit:
    def __init__(self, dataset, cols):
        self.max_rows = 1
        self.data = dataset
        self.cols = cols
        self.row_calc(len(dataset), cols)

    def row_calc(self, dataset_len, cols):
        self.max_rows = math.ceil(dataset_len / cols) if dataset_len > cols else 1

    def initialize_figure(self, width=18):
        if self.data is not None and self.cols is not None:
            return plt.figure(figsize=(width, 2 * self.max_rows))
        return False
