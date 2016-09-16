# Titanic Data Visualization


## Summary
This project involves visualization of Titanic survival using passenegers data such as class, gender and age group. Created total three graphs:

1. Titanic survival by class: First class passengers have the highest survival rate among all the different classes.
2. Titanic survival by age group: The Children belonging to the age group 0-15 have the highest survival rate.
3. Titanic survival by class and gender: The First class female have maximum survival rate and the third class male have minimum survival rate.

## Design
* Chart type: As the dataset contains passsengers information in different categories, a bar charts is the best way to see trends of the titanic survival.
* Layout: Since only two survivorship status exist so stacked bar chart layout is best suited to visualize the data.
* Legend: Data are represented in the ratios, the stacked bar chart of y-axis are same for all the categories so, legend are moved to the right hand side of the chart.
* Visual encodings: X-axis represents different categories of an information and y-axis represents ratio of passengers. Sequential colors are used to differentiate between 'survived' and 'perished'. Shape of the stacked bar chart is rectangle. 

## Feedback
### 1
Color in the stacked bar chart can be improved. The color which are used are good but more conventional and sequential color can improve the visualization. 

### 2
Reduce the width of stack bar chart for the second graph (Titanic survival rate by age group) so that it can be more clearly represent the age group.

### 3
To display the likelihood of survival, it is best to use ratios of the survival, so change the count to ratio in the chart 1 and chart 3. It would be best to use 'perished' instead of 'dead' as this tense matches that of 'survived'.

### Final Visualization
https://bl.ocks.org/pratyush19/raw/3a119b1aeb707cfc396c7a95340771fe/

### Resources

* [mbostock](https://bl.ocks.org/mbostock)
* [d3 documentation's](https://github.com/d3/d3/blob/master/API.md)
* [DashingD3js](https://www.dashingd3js.com/table-of-contents)
* [Color Brewer](http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3)

