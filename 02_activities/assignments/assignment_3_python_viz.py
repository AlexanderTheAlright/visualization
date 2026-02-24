# Assignment 3 — Visualization 1 (Python / matplotlib)
# Dataset: Daily Shelter & Overnight Service Occupancy & Capacity
# Source: https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/
#
# Heatmap of average monthly bed occupancy rates by shelter sector in Toronto, 2024.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

# ══════════════════════════════════════════════════════════════════════════════
# STYLE
# ══════════════════════════════════════════════════════════════════════════════

plt.style.use("default")
plt.rcParams.update({
    "figure.facecolor": "#FFFFFF",
    "axes.facecolor": "#FFFFFF",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#000000",
    "axes.linewidth": 1.0,
    "figure.dpi": 300,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": "#E0E0E0",
    "grid.linestyle": "-",
    "grid.linewidth": 0.75,
    "grid.alpha": 0.5,
    "axes.axisbelow": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "axes.titlesize": 16,
    "axes.titleweight": "bold",
    "axes.titlecolor": "#000000",
    "axes.labelsize": 11,
    "axes.labelweight": "bold",
    "axes.labelcolor": "#000000",
    "xtick.color": "#000000",
    "ytick.color": "#000000",
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

# ══════════════════════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════════════════════

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/datastore/dump/fc409fd7-0348-49d7-bba9-70ac1a8c727c"
df = pd.read_csv(url)

df['OCCUPANCY_DATE'] = pd.to_datetime(df['OCCUPANCY_DATE'])
df['MONTH'] = df['OCCUPANCY_DATE'].dt.month

# filter to bed-based programs with valid occupancy data
df = df[df['CAPACITY_ACTUAL_BED'].notna() & (df['CAPACITY_ACTUAL_BED'] > 0)]
df = df[df['OCCUPANCY_RATE_BEDS'].notna()]

# the Families sector is almost entirely room-based, so it drops out when
# filter for bed occupancy. keeping only sectors that actually have data.
main_sectors = ['Women', 'Men', 'Mixed Adult', 'Youth']
df_filtered = df[df['SECTOR'].isin(main_sectors)]

# pivot: rows = sector, columns = month, values = mean occupancy rate
monthly_avg = df_filtered.groupby(['SECTOR', 'MONTH'])['OCCUPANCY_RATE_BEDS'].mean()
heatmap_data = monthly_avg.unstack(level='MONTH')
heatmap_data = heatmap_data.reindex(main_sectors)

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# ══════════════════════════════════════════════════════════════════════════════
# PLOT
# ══════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(10, 4.5), dpi=130)
fig.set_facecolor("white")
ax.set_facecolor("white")

hm = sns.heatmap(heatmap_data, cmap='viridis', annot=False,
                 cbar_kws={"shrink": 0.8, "label": "Occupancy Rate (%)"},
                 vmin=85, vmax=105,
                 linewidths=2.5, linecolor='white',
                 xticklabels=month_labels,
                 ax=ax)

cbar = hm.collections[0].colorbar
cbar.set_label("Occupancy Rate (%)", rotation=270, labelpad=20,
               fontsize=11, weight='bold')

# annotate each cell
for i in range(heatmap_data.shape[0]):
    for j in range(heatmap_data.shape[1]):
        value = heatmap_data.iloc[i, j]
        if not np.isnan(value):
            ax.text(j + 0.5, i + 0.5, f'{value:.0f}%',
                    ha='center', va='center',
                    fontsize=9, weight='bold', color='black',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                              edgecolor='#333333', linewidth=1.5, alpha=0.95))

ax.set_xticklabels(ax.get_xticklabels(), fontsize=11, fontweight='bold', color='black')
ax.set_yticklabels(ax.get_yticklabels(), fontsize=11, fontweight='bold', color='black', rotation=0)
ax.set_xlabel('')
ax.set_ylabel('')

# title and subtitle
fig.text(0.02, 0.97,
         "No Room at the Inn",
         fontsize=15, weight='bold', color='black',
         ha='left', va='center', transform=fig.transFigure)
fig.text(0.02, 0.93,
         "Average monthly bed occupancy rate (%) by shelter sector, Toronto 2024",
         fontsize=11, color='grey',
         ha='left', va='center', transform=fig.transFigure)

# source and record count
n_records = len(df_filtered)
fig.text(0.99, 0.01, f"(n = {n_records:,} daily program records)",
         fontsize=9, color='grey', ha='right', va='bottom',
         transform=fig.transFigure)
fig.text(0.01, 0.01,
         "Data: City of Toronto Open Data — Daily Shelter & Overnight Service Occupancy & Capacity",
         fontsize=8, color='grey', ha='left', va='bottom',
         transform=fig.transFigure)

fig.tight_layout(rect=(0, 0.03, 1, 0.90))

plt.savefig('assignment_3_viz1_shelter_occupancy.png', dpi=300, bbox_inches='tight')
plt.show()
print("Saved: assignment_3_viz1_shelter_occupancy.png")
