#!/usr/bin/env python3
"""Plot daily GitHub contributions as a bar chart."""

import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

with open('contributions.json') as f:
    data = json.load(f)

dates = [datetime.strptime(d['date'], '%Y-%m-%d') for d in data]
counts = [d['contributionCount'] for d in data]

fig, ax = plt.subplots(figsize=(16, 5))

ax.bar(dates, counts, width=1.0, color='#216e39', alpha=0.85, edgecolor='none')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Contributions', fontsize=12)
ax.set_title('GitHub Contributions — eshelman', fontsize=14, fontweight='bold')

ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.tick_params(axis='x', which='major', labelsize=11)

ax.set_xlim(min(dates), max(dates))
ax.set_ylim(bottom=0)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('github-contributions-daily-bar.png', dpi=150)
print('Saved github-contributions-daily-bar.png')
