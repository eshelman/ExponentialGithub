#!/usr/bin/env python3
"""Plot daily GitHub contributions as a bar chart."""

import argparse
import json
from datetime import datetime
from themes import apply_theme
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

parser = argparse.ArgumentParser()
parser.add_argument('--theme', choices=['default', '6by9'], default='default')
args = parser.parse_args()

with open('contributions.json') as f:
    data = json.load(f)

dates = [datetime.strptime(d['date'], '%Y-%m-%d') for d in data]
counts = [d['contributionCount'] for d in data]

fig, ax = plt.subplots(figsize=(16, 5))
t = apply_theme(fig, ax, args.theme)

ax.bar(dates, counts, width=1.0, color=t['accent'], alpha=0.85, edgecolor='none')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Contributions', fontsize=12)
ax.set_title('GitHub Contributions — eshelman', fontsize=14, fontweight='bold')

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.tick_params(axis='x', which='major', labelsize=11)

ax.set_xlim(min(dates), max(dates))
ax.set_ylim(bottom=0)

plt.tight_layout()
out = 'github-contributions-daily-bar.png'
plt.savefig(out, dpi=150, facecolor=fig.get_facecolor())
print(f'Saved {out}')
