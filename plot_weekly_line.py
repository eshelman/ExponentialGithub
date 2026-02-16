#!/usr/bin/env python3
"""Plot weekly GitHub contributions as a line graph."""

import argparse
import json
from datetime import datetime, timedelta
from themes import apply_theme
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

parser = argparse.ArgumentParser()
parser.add_argument('--theme', choices=['default', '6by9'], default='default')
args = parser.parse_args()

with open('contributions.json') as f:
    data = json.load(f)

# Aggregate into weekly buckets (week starting Monday)
weekly = {}
for d in data:
    dt = datetime.strptime(d['date'], '%Y-%m-%d')
    week_start = dt - timedelta(days=dt.weekday())
    weekly[week_start] = weekly.get(week_start, 0) + d['contributionCount']

weeks = sorted(weekly.keys())
counts = [weekly[w] for w in weeks]

fig, ax = plt.subplots(figsize=(16, 5))
t = apply_theme(fig, ax, args.theme)

ax.plot(weeks, counts, color=t['accent'], linewidth=1.5, alpha=0.9)
ax.fill_between(weeks, counts, alpha=0.15, color=t['accent_fill'])

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Contributions (per week)', fontsize=12)
ax.set_title('GitHub Contributions — eshelman (Weekly)', fontsize=14, fontweight='bold')

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[4, 7, 10]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.tick_params(axis='x', which='major', labelsize=11)

ax.set_xlim(min(weeks), max(weeks))
ax.set_ylim(bottom=0)

plt.tight_layout()
out = 'github-contributions-weekly-line.png'
plt.savefig(out, dpi=150, facecolor=fig.get_facecolor())
print(f'Saved {out}')
