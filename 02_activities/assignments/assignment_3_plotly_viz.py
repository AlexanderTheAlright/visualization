# Assignment 3 — Visualization 2 (Plotly / interactive)
# Dataset: Daily Shelter & Overnight Service Occupancy & Capacity
# Source: https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/
#
# Interactive stacked area chart showing how Toronto's overnight shelter system
# distributes people across different service types month by month in 2024.

import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ══════════════════════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════════════════════

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/datastore/dump/fc409fd7-0348-49d7-bba9-70ac1a8c727c"
df = pd.read_csv(url)

df['OCCUPANCY_DATE'] = pd.to_datetime(df['OCCUPANCY_DATE'])
df['MONTH'] = df['OCCUPANCY_DATE'].dt.month

# aggregate total service users per month per service type
monthly = df.groupby(['MONTH', 'OVERNIGHT_SERVICE_TYPE'])['SERVICE_USER_COUNT'].sum().reset_index()

# keep the main service types and collapse the rest into "Other"
main_types = ['Shelter', 'Motel/Hotel Shelter', '24-Hour Respite Site',
              '24-Hour Women\'s Drop-in', 'Warming Centre']
monthly['SERVICE_TYPE'] = monthly['OVERNIGHT_SERVICE_TYPE'].apply(
    lambda x: x if x in main_types else 'Other'
)
monthly = monthly.groupby(['MONTH', 'SERVICE_TYPE'])['SERVICE_USER_COUNT'].sum().reset_index()

# pivot for plotting
pivot = monthly.pivot(index='MONTH', columns='SERVICE_TYPE', values='SERVICE_USER_COUNT').fillna(0)

# order by total volume (largest at bottom of stack)
col_order = pivot.sum().sort_values(ascending=False).index.tolist()
pivot = pivot[col_order]

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# ══════════════════════════════════════════════════════════════════════════════
# PLOT
# ══════════════════════════════════════════════════════════════════════════════

# viridis-sampled palette
n_types = len(col_order)
import matplotlib.cm as mpl_cm
viridis = mpl_cm.viridis
colors = [f'rgba({int(viridis(i/(n_types-1))[0]*255)},{int(viridis(i/(n_types-1))[1]*255)},{int(viridis(i/(n_types-1))[2]*255)},0.85)'
          for i in range(n_types)]

fig = go.Figure()

for i, stype in enumerate(col_order):
    fig.add_trace(go.Scatter(
        x=month_labels,
        y=pivot[stype],
        name=stype,
        mode='lines',
        stackgroup='one',
        line=dict(width=0.5, color=colors[i]),
        fillcolor=colors[i],
        hovertemplate=f'<b>{stype}</b><br>Month: %{{x}}<br>Service Users: %{{y:,.0f}}<extra></extra>',
    ))

n_records = len(df)
fig.update_layout(
    template='plotly_white',
    title=dict(
        text=(f"<b>Where Do They Sleep?</b><br>"
              f"<span style='color:grey;font-size:14px;'>"
              f"Total monthly service users by overnight service type, Toronto 2024</span>"),
        x=0.0,
        xanchor='left',
        font=dict(size=16),
    ),
    height=500,
    width=850,
    margin=dict(t=100, b=80, l=80, r=40),
    xaxis=dict(
        title=dict(text='<b>Month</b>', font=dict(size=12, color='black')),
        showgrid=False,
        tickfont=dict(size=11, color='black', family='Arial Black'),
    ),
    yaxis=dict(
        title=dict(text='<b>Total Service Users</b>', font=dict(size=12, color='black')),
        showgrid=True,
        gridcolor='rgba(180,180,180,0.3)',
        tickfont=dict(size=11, color='black'),
        tickformat=',',
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-0.3,
        xanchor='center',
        x=0.5,
        font=dict(size=10),
        bordercolor='#CCCCCC',
        borderwidth=1,
        bgcolor='white',
    ),
    plot_bgcolor='white',
    hovermode='x unified',
    annotations=[
        dict(
            text=f"Data: City of Toronto Open Data | n = {n_records:,} records across all service types",
            xref='paper', yref='paper',
            x=0, y=-0.42,
            showarrow=False,
            font=dict(size=9, color='grey'),
        ),
    ],
)

fig.write_html('assignment_3_viz2_shelter_service_types.html')

try:
    fig.write_image('assignment_3_viz2_shelter_service_types.png', scale=2)
    print("Saved: assignment_3_viz2_shelter_service_types.png")
except (ValueError, ImportError):
    print("Note: kaleido not installed, skipping PNG export.")

fig.show()
print("Saved: assignment_3_viz2_shelter_service_types.html")
