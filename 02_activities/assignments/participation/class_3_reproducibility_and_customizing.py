# Class 3: Reproducible Data Visualization + Customizing Our Plots
# Data Visualization - DSI Certificate
# Covers slides 03 (reproducibility) and 05 (customizing)

# --- Reproducibility notes ---
# We opened with a case study about image manipulation in a cancer research paper.
# Dr. Elisabeth Bik found that cell staining images had been duplicated and the
# paper got retracted. Her work has led to 172 retractions so far.
# The point: if we can't trust the visuals, we can't trust the conclusions.
#
# Reproducibility means someone else could repeat our steps and get the same result.
# It is both ethical and practical:
#   - Ethical: the ASA guidelines say good stats practice is based on reproducible results
#   - Practical: easier to edit plots later, draw on past work, track changes with version control
#
# Key practices for reproducible data viz:
#   - Work programmatically (code, not Illustrator)
#   - Work in plain text (.py files, not Word docs)
#   - Comment your code so people (including future you) understand it
#
# FAIR principles: findability, accessibility, interoperability, reusability
# Originally for research data management, now widely adopted.
#
# Reproducibility vs replicability:
#   - Reproducibility = same data + same methods = same results
#   - Replicability = new data + same question = consistent results
#
# Datasheets for datasets (Gebru et al., 2020): documenting motivation, composition,
# collection process, etc. Good practice for connecting raw data to final visualizations.

# --- Customizing our plots ---

import numpy as np
import matplotlib.pyplot as plt

# set up with two y variables this time
np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

# plotting two lines on one axes (recall from last time)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1)
ax.plot(x, y2)
fig.show()

# adding a legend
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")
ax.legend(loc='lower right')
fig.show()

# customizing the legend
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")
ax.legend(loc='lower right',
          frameon=True,
          fontsize=12,
          ncol=2,
          shadow=True)
fig.show()

# moving the legend outside the plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1, label="Person 1")
ax.plot(x, y2, label="Person 2")
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
fig.show()

# text annotations on a scatter plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.text(10, 95, "This value is important!")
fig.show()

# styling the text annotation
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.text(10, 95, "This value is important!",
        ha='center',
        color='red',
        size=20)
fig.show()

# positioning text with transforms (data vs axes vs figure coordinates)
fig, ax = plt.subplots()
ax.axis([0, 10, 0, 10])
ax.text(1, 5, ". Data:(1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes:(0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure:(0.2, 0.2)", transform=fig.transFigure)
plt.show()

# annotating with arrows
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.annotate('This is important!', xy=(10, 95), xytext=(20, 94),
            arrowprops=dict(facecolor='black'))
fig.show()

# modifying arrow style
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.annotate('This is important!',
            xy=(10, 95), xytext=(20, 94),
            arrowprops=dict(arrowstyle="wedge", color="hotpink"))
fig.show()

# removing tick marks and labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.yaxis.set_major_locator(plt.NullLocator())       # removes ticks and labels
ax.xaxis.set_major_formatter(plt.NullFormatter())    # removes only labels
plt.show()

# limiting number of tick marks
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MaxNLocator(3))
plt.show()

# setting tick mark intervals
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.show()

# rotating axis labels
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
plt.xticks(rotation=45, ha='right')
plt.show()

# activity: modify x axis title with serif font and indigo colour
font1 = {'family': 'serif', 'color': 'indigo'}
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y1, label="Person 1")
ax.scatter(x, y2, label="Person 2")
ax.legend(loc='lower right')
plt.xlabel('Shiny New X Axis!', fontsize=18, fontdict=font1)
plt.show()

# trying out styles
plt.style.use('fivethirtyeight')

np.random.seed(613)
x = np.arange(50)
y1 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y1)
ax.plot(x, y2)
fig.show()

# other styles worth trying: 'ggplot', 'seaborn', 'bmh', 'dark_background'
