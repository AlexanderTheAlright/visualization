# Class 1: Course Intro + Getting Started with Matplotlib
# Data Visualization - DSI Certificate
# Covers slides 01 (intro) and 02 (matplotlib basics)

# --- Notes from the intro ---
# We talked about why data visualization matters using some historical examples.
# John Snow's cholera map is a classic one -- he plotted deaths on a map and traced them
# back to a water pump, which was a pretty big deal for public health.
# Florence Nightingale's coxcomb chart showed causes of death among soldiers and
# helped push for better sanitary conditions. The takeaway is that even back then,
# visualizing data was a powerful way to make a case for change.
#
# We also looked at the Challenger disaster as a case study in what can go wrong when
# data isn't communicated well. Engineers had concerns about the O-rings in cold weather
# but the way the data was presented didn't make the danger obvious enough.
#
# Three qualities of good data viz came up:
#   - Aesthetic: does it look good?
#   - Substantive: is the data honest and accurate?
#   - Perceptual: can the viewer understand the message?

# --- Matplotlib basics ---

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

# make some sample data to work with
np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100, 50)

# basic scatterplot
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
plt.show()

# bar chart with the same data
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(x, y)
plt.show()

# line plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
plt.show()

# activity: make a histogram
fig, ax = plt.subplots(figsize=(5, 3))
ax.hist(y)
plt.show()

# adding labels and a title to our line plot
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time')
ax.set_ylabel('Total growth')
ax.set_xlabel('Years since start')
fig.tight_layout()
plt.show()

# using font dictionaries to style our labels
font1 = {'family': 'sans-serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y)
ax.set_title('Total growth over time', fontdict=font1)
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)
fig.tight_layout()
plt.show()

# customizing data points on a scatterplot
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y, marker='*', color='indigo')
fig.show()

# line plot with custom line style and width
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='indigo', linestyle='--', linewidth=2)
fig.show()

# using hex codes for colour
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='#7425b9', linestyle='--', linewidth=2)
fig.show()

# going further with marker customization
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*',
        markersize=12,
        color='#7425b9',
        linestyle='--',
        linewidth=2,
        markeredgecolor='#fa9359',
        markerfacecolor='#000000')
plt.show()

# adding grid lines
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='#7425b9', linestyle='--', linewidth=2)
ax.grid(axis='y')
plt.show()

# customizing grid lines
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, y, marker='*', color='#7425b9', linestyle='--', linewidth=2)
ax.grid(axis='y', color='blue', linewidth=2, linestyle='-.')
plt.show()

# --- Activity: Exploring matplotlib ---
# We visited the Python Graph Gallery (python-graph-gallery.com) and picked a
# visualization to try replicating. I thought the heatmap section was interesting
# since it handles a lot of the aesthetic and perceptual stuff automatically.
# The gallery is a solid resource to come back to when choosing chart types.
