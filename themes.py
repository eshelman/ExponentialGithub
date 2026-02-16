"""Shared theme definitions for contribution plots."""

import os
os.environ.setdefault('MPLCONFIGDIR', os.path.join(os.path.dirname(__file__), '.matplotlib'))

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

THEMES = {
    'default': {
        'bg': '#ffffff',
        'plot_bg': '#ffffff',
        'text': '#333333',
        'muted': '#666666',
        'accent': '#216e39',
        'accent_fill': '#216e39',
        'grid': '#e0e0e0',
        'spine': '#cccccc',
    },
    '6by9': {
        'bg': '#1a1a1f',        # charcoal-900
        'plot_bg': '#1a1a1f',
        'text': '#f4f4f6',      # gray-100
        'muted': '#9898a4',     # gray-400
        'accent': '#ff6b2c',    # orange-500
        'accent_fill': '#ff6b2c',
        'grid': '#2e2e37',      # charcoal-700
        'spine': '#3a3a45',     # charcoal-600
    },
}


def apply_theme(fig, ax, theme_name='default'):
    """Apply a named theme to a matplotlib figure and axes."""
    t = THEMES[theme_name]

    fig.patch.set_facecolor(t['bg'])
    ax.set_facecolor(t['plot_bg'])

    ax.title.set_color(t['text'])
    ax.xaxis.label.set_color(t['muted'])
    ax.yaxis.label.set_color(t['muted'])
    ax.tick_params(colors=t['muted'])

    for spine in ax.spines.values():
        spine.set_color(t['spine'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return t
