def set_axis(ax):
    set_fig(ax)
    hide_spines(ax)
    hide_ticks(ax)
    limits(ax)


def hide_spines(ax):
    for s in ["top", "bottom", "left", "right"]:
        ax.spines[s].set_visible(False)


def hide_ticks(ax):
    ax.set_xticks([])
    ax.set_yticks([])


def limits(ax, x=0, y=1):
    ax.set_xlim(x, y)
    ax.set_ylim(x, y)


def set_fig(ax):
    ax.set(adjustable='box', aspect='equal')
