#datacamp intermediate python exercises

########################plot and scatter exercise ##########################
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)
plt.show()

# Change the line plot below to a scatter plot
plt.scatter(year, pop)
# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()

########################histogram exercise ##########################
# note : plt.clf() cleans it up again so you can start afresh.

# Build histogram with 5 bins
plt.hist(life_exp, bins=5)
# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

########################customizations exercise ##########################
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp) 

# Add axis labels and title
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# After customizing, display the plot
plt.show()
plt.clf()

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()
plt.clf()

#########################size exercise ########################## 
# Import numpy as np
import numpy as np
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop*2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
# Display the plot
plt.show()

########################colors exercise ##########################
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col, alpha=0.8)
plt.show()

######################### Additional customizations ########################
# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

plt.grid(True)
plt.show()
