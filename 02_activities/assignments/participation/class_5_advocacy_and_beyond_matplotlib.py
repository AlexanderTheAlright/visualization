# Class 5: Data Visualization as Advocacy + Beyond Matplotlib
# Data Visualization - DSI Certificate
# Covers slides 08 (advocacy) and 09 (beyond matplotlib)

# --- Advocacy notes ---
# The idea here is that data viz has been used for advocacy for a long time.
# John Snow's cholera map, Florence Nightingale's charts, the Periscopic gun deaths
# viz -- all examples of using visuals to push for some kind of change.
#
# Tactical Technology Collective (2013) connects this to Aristotle's three modes
# of persuasion:
#   - Rational appeal: give people the facts and let them reach the right conclusion
#   - Moral appeal: tap into ethical convictions
#   - Emotional appeal: provoke empathy, compassion, outrage
#
# The Brooks slave ship diagram was a powerful example. It was presented to
# British Parliament to show how inhumane conditions were on slave ships. It used
# all three appeals at once: factual measurements of the ship, moral argument
# against the trade, and the visual horror of seeing human bodies packed like cargo.
#
# Two functions of data viz for advocacy:
#   - Presentation: depicting the facts
#   - Representation: using metaphor and analogy subjectively
#
# On the topic of representation: what data are we NOT seeing? Data collection
# choices limit what we can visualize later. A binary gender variable excludes
# nonbinary people. "What gets counted counts" -- but we should think about what
# is NOT being counted too.
#
# Underwater labour: D'Ignazio and Klein (2020) use the iceberg metaphor to highlight
# all the unseen work behind a visualization -- community organizers, designers,
# research assistants, IT staff, caregivers. Crediting all contributors makes that
# invisible work visible.
#
# Some cool non-traditional data viz examples:
#   - Pulse (2012): string and motors creating real-time tangible line graphs
#   - Watermarks (2009): projections on buildings showing future water levels
#   - "Untitled" (Ross) (1991): 175 lbs of candy representing a person's weight
#     before AIDS, audience takes candy, representing weight loss and public apathy

# --- Beyond matplotlib: Seaborn ---

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load the tips sample dataset
tips = sns.load_dataset("tips")
print(tips.head())

# basic line plot
sns.lineplot(data=tips, x='total_bill', y='tip')
plt.show()

# apply a premade style
sns.set_style('whitegrid')

# add titles and labels
tipgraph = sns.lineplot(data=tips, x='total_bill', y='tip')
tipgraph.set(title='Tips vs. Total Bill',
             xlabel='Total Bill ($)',
             ylabel='Tip Amount ($)')
plt.show()

# customize aesthetics
fig = plt.subplots(figsize=(10, 3))
tipgraph = sns.lineplot(data=tips, x='total_bill', y='tip',
                        color='hotpink', linestyle='--',
                        linewidth=3, marker='o',
                        markerfacecolor='indigo')
plt.show()

# the real power of seaborn: mapping multiple variables easily
tipgraph = sns.scatterplot(data=tips, x='total_bill', y='tip',
                           style='time', hue='day',
                           palette=['purple', 'hotpink',
                                    'deepskyblue', 'yellowgreen'])
tipgraph.set(title='Tips vs. Total Bill',
             xlabel='Total Bill ($)',
             ylabel='Tip Amount ($)')
plt.show()

# pairplot for comparing variables
sns.pairplot(data=tips, hue='day')
plt.show()

# relplot for exploring levels within variables
daysplot = sns.relplot(data=tips, x="total_bill", y="tip",
                       hue="sex", col="day",
                       kind="scatter", col_wrap=2)
plt.show()

# --- Beyond matplotlib: Plotly ---

import plotly.graph_objects as go

x1 = np.array(["Luffy", "Zoro", "Nami", "Usopp", "Sanji"])
y1 = np.array([110, 180, 240, 99, 220])

# make an interactive bar chart
graph = go.Figure()
graph.add_trace(go.Bar(x=x1, y=y1))
graph.update_layout(title="Pirate Scores",
                    xaxis_title="Pirates",
                    yaxis_title="Score")
graph.show()

# customizing plotly scatter plot
graph = go.Figure()
graph.add_trace(go.Scatter(x=x1, y=y1, mode='markers',
    marker=dict(size=15, color='hotpink', opacity=1,
                line=dict(width=5, color='purple'))))
graph.update_layout(title='Interactive Pirate Plot',
                    xaxis_title='Pirates',
                    yaxis_title='Scores',
                    width=500, height=500)
graph.show()

# saving plotly as HTML
# graph.write_html("pirategraph.html")

# --- Beyond matplotlib: Wordclouds ---

from wordcloud import WordCloud

df = pd.read_csv(
    "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/movie_quotes.csv",
    on_bad_lines='skip')

text = " ".join(each for each in df.quote)
wordcloud = WordCloud(background_color="white",
                      colormap='inferno').generate(text)

fig, ax = plt.subplots(figsize=(7, 3))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.show()

# --- Beyond matplotlib: Venn Diagrams ---

from matplotlib_venn import venn2, venn2_circles, venn2_unweighted

A = set(["apple", "banana", "watermelon"])
B = set(["pumpkin", "blueberry", "apple", "key lime"])

diagram = venn2_unweighted([A, B],
                           set_labels=('Fruits', 'Pies'),
                           set_colors=("blue", "red"),
                           alpha=0.5)
plt.show()

# showing actual items instead of counts
diagram = venn2_unweighted([A, B],
                           set_labels=('Fruits', 'Pies'),
                           set_colors=("blue", "red"),
                           alpha=0.5)
diagram.get_label_by_id("10").set_text("\n".join(A - B))
diagram.get_label_by_id("11").set_text("\n".join(A & B))
diagram.get_label_by_id("01").set_text("\n".join(B - A))
plt.show()

# --- Notes on static vs dynamic viz ---
# Static: image-based (PNG, PDF), a snapshot, most of what we did before matplotlib
# Dynamic: interactive, lets users filter/modify, multiple stories in one
#
# Benefits of dynamic viz: deeper exploration, transparency, engagement
# Costs: harder to tell a single clear story, can be confusing, access/sharing issues
#
# When designing interactive viz, ask:
#   - Are interactive elements easy to navigate and accessible?
#   - How much time will the audience have?
#   - Do interactive features actually help serve the purpose, or are they just cool?
#
# Types of changes in dynamic viz (Cottam et al., 2012):
#   - Identity-preserving: associations between data and visuals stay constant
#   - Transitional: some associations maintained, some new elements added
#   - Immediate: everything can change, no comparison across snapshots
