# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      GOOD VISUALIZATION: "4 Graphics Explain LA's Rare January Fires"
      by World Resources Institute
      https://www.wri.org/insights/los-angeles-fires-january-2025-explained

      I chose this piece from WRI because it does a lot of things right when it comes
      to the three qualities we discussed in class: aesthetic, substantive, and
      perceptual.

      First, on the substantive side, the visualization is honest about where the data
      comes from. They use satellite data from Global Forest Watch and clearly note
      the time periods and sources for each graphic. This matters because, as we
      learned, including your sources signals transparency to viewers and makes the
      whole thing more trustworthy. The fire alerts map shows real detected heat
      signatures rather than estimates, and the comparison chart uses a solid baseline
      of 2012 to 2024 averages so you can see just how unusual January 2025 was.

      Second, the perceptual qualities are strong here. The designers thought about
      Gestalt principles when putting this together. The map groups fire alerts
      spatially so you can see the concentration in certain areas, and the bar chart
      comparing 2025 to historical averages makes the contrast immediately obvious.
      They also broke up what could have been overwhelming information into four
      separate graphics, each answering a specific question. This keeps the cognitive
      load manageable since you are not trying to process everything at once.

      Third, the aesthetic choices support the content rather than distracting from it.
      Everything is two-dimensional with clean layouts. There are no flashy 3D effects
      trying to look impressive. The embedded Flourish charts for tree cover loss and
      temperature trends use simple line and bar formats that are familiar and easy to
      read. This fits with what Kennedy and colleagues found about the conventions that
      make visualizations feel objective and reliable.

      Finally, the medium fits the purpose well. As a web article with embedded
      interactive elements, it lets you explore the data while also telling a clear
      narrative about why these fires were so unusual. For something meant to inform
      the public about an environmental crisis, these design choices make sense.

      ```
    - How could this data visualization have been improved?
      ```
      Even though this is a strong visualization, there are a couple things that could
      make it better.

      The main issue is accessibility for people using screen readers. The embedded
      Flourish charts look good but someone who cannot see the graphics would miss
      the key insights. Adding more detailed alt-text descriptions would help a lot.
      Based on what we covered about describing data visualizations, the descriptions
      should include not just what the chart looks like but also the key statistics
      and trends. That way screen reader users can understand that fire alerts were
      130 times higher than average without needing to see the bar chart.

      The color choices could also be tested with colorblind viewers in mind. The
      fire alert map uses red which can be hard to distinguish for some viewers.
      Adding patterns or using a more accessible color palette would make sure people
      with color vision deficiency can still interpret the spatial data. Something
      like the Viridis colormap works well for maps since it was specifically designed
      to be readable for people with different types of colorblindness.

      ```

      ```
      BAD VISUALIZATION: "The European Cannabis Investment Ecosystem" Infographic
      https://www.behance.net/gallery/124729731/The-European-Cannabis-Investment-Ecosystem

      For my bad example I found this infographic showing investment sources in the
      European cannabis industry. It uses a 3D cylindrical pie chart to display
      percentages like Venture Capital at 42.1% and Angel investors at 33.6%. While
      the graphic looks polished and professional, it has serious problems that go
      against what we learned in this course.

      The biggest issue is the 3D cylinder effect. The chart is tilted and extruded
      into three dimensions, which completely distorts how we perceive the slices.
      The green Venture Capital section at the top looks massive partly because it
      is closer to the viewer and takes up the entire top surface of the cylinder.
      Meanwhile the smaller slices at the bottom like Hedge Fund at 0.9% are compressed
      and hard to see. You cannot actually compare the sizes accurately because the
      perspective throws everything off. This breaks the most basic rule of showing
      data honestly.

      The chart also has way too many categories. There are nine different slices
      ranging from 42.1% down to 0.9%. Humans are already bad at comparing angles,
      and when you have this many thin slices crammed together at the bottom of a
      tilted cylinder, it becomes impossible to tell Investment Banks from Family
      Office from Syndicates. They are all around 1.9% but good luck seeing that
      from the graphic itself. You have to read the labels to get any useful info,
      which defeats the purpose of visualizing the data in the first place.

      The decorative elements also add clutter without helping comprehension. There
      are little illustrated people walking around on top of the chart and trees
      scattered in the background. These might make the infographic look nice for
      a report cover, but they add cognitive load without conveying any data. We
      talked in class about how every visual element should serve a purpose, and
      these decorations just distract from the numbers.

      Finally the color choices create problems. The two largest categories, Venture
      Capital and Angel investors, are both shades of green which makes them harder
      to distinguish quickly. Someone with color vision deficiency would have an
      even harder time telling them apart.

      ```
    - How could this data visualization have been improved?
      ```
      The most obvious fix would be to scrap the 3D cylinder entirely and use a
      horizontal bar chart instead. With nine categories of investment sources, a
      bar chart sorted from largest to smallest would let viewers instantly see that
      Venture Capital dominates, followed by Angel investors, with everything else
      being relatively minor. The bars would all start from the same baseline so
      comparisons would be accurate and easy.

      If the designers really wanted to show part-to-whole relationships, a flat 2D
      pie chart would at least eliminate the perspective distortion. But honestly
      with nine categories that is still too many slices. They could group the
      smaller categories under 5% into an "Other" slice to reduce clutter, then use
      a separate table or annotation to break out those details for readers who want
      them.

      The decorative people and trees should be removed entirely. They do not add
      any information and just make the chart busier. A cleaner layout with more
      whitespace would actually look more professional and be easier to read. The
      color palette should also use more distinct hues so each category is clearly
      differentiated, especially the two largest green sections.

      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e.
500 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 01/26/2026`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
