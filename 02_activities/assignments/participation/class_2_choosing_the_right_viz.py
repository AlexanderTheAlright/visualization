# Class 2: Choosing the Right Visualization
# Data Visualization - DSI Certificate
# Covers slide 04

# --- Notes ---
# This class was mostly discussion-based, not much code. The big theme was that
# data visualization is never truly neutral -- we always make choices about what
# to show and how to show it, which makes every viz a rhetorical object.
#
# We looked at two visualizations about gun violence in the US:
#   1. Periscopic's animated viz of gun killings in 2018 -- very emotional,
#      shows "stolen years" of life. Won awards but got criticized for being
#      too advocacy-driven. But it was not dishonest, just not neutral.
#   2. Washington Post's "Era of Active Shooters" -- cleaner, more traditional
#      bar chart style. Feels more like a "blank page" that lets viewers draw
#      their own conclusions.
#
# Neither is inherently better -- it depends on purpose, audience, and medium.
# We also saw the Jobs Report example where the same unemployment data was shown
# from Republican vs Democrat perspectives. Same data, different framing, both
# technically accurate. That drove the point home.
#
# Key frameworks we covered:
#   - Intended purpose: persuasion, comparison, evaluation, exploring
#   - Intended audience: age, education, subject expertise, accessibility needs
#   - Intended medium: print, web, poster, presentation
#
# Gestalt principles came up as a way to think about how people perceive visuals:
#   - Proximity: things close together look related
#   - Similarity: things that look alike seem grouped
#   - Enclosure: borders or shading group things
#   - Closure: we mentally fill in gaps
#   - Continuity: we follow smooth paths
#   - Connection: lines connecting things imply relationship
#
# Cognitive load is also something to manage:
#   - Familiar chart types = lower cognitive load
#   - Accurate interpretation (position-based) = lower load than approximate (area-based)
#   - Concise = lower load than detailed
#   - Explanatory = lower load than exploratory
#
# Kennedy et al. (2016) found four conventions that make a viz feel objective and factual:
#   - Two-dimensional
#   - Clean layout
#   - Geometric shapes and lines
#   - Data sources cited at the bottom
#
# Provenance rhetoric: citing your data source signals transparency and trustworthiness,
# making viewers more likely to believe what they see (Hullman & Diakopoulos, 2011).
#
# We also briefly reviewed matplotlib syntax from last class:

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(613)
x = np.arange(50)
y = np.random.randint(0, 100, 50)

# quick review scatterplot
fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(x, y)
fig.show()

# --- Resources we were pointed to ---
# Data Visualization Catalogue: datavizcatalogue.com
# Financial Times Visual Vocabulary: both interactive (PowerBI) and PDF versions
# Both help you pick the right chart type based on what you want to communicate.
