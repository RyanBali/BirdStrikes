import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.font_manager as font_manager
from matplotlib.lines import Line2D

# Load Data
with open('incidents', 'r') as f:
    lines = f.readlines()
    incidentyear = [int(line.split()[0]) for line in lines]
    incidentcount = [int(line.split()[1]) for line in lines]

# Years 2010-2021 for Prediction
with open('years', 'r') as f:
    lines = f.readlines()
    predictionyears = [int(line.split()[0]) for line in lines]
	
# Convert Dims
X = np.array(incidentyear).reshape((-1, 1))
Y = np.array(incidentcount).reshape((-1, 1))

# Run the LR model
model = LinearRegression().fit(X,Y)

# Retrieve predicted model parameters
r_sq = model.score(X,Y)

# Print model parameters
print()
print('coefficient of determination -> ', r_sq)
intercept = model.intercept_
print('intercept -> ', intercept)
slope =  model.coef_
print('slope -> ', slope)
print()

# Plot the data 
plt.scatter(incidentyear, incidentcount, marker='D')

#prepare the linear regression line with years 2020 and 2021 for prediction
x_pred = np.array(predictionyears).reshape((-1, 1))
axes = plt.gca()
y_vals = intercept + slope * x_pred
plt.plot(x_pred, y_vals, color="grey")
#set graph limits, labels, and title 
csfont = {'fontname':'Courier New'}
plt.xlim(xmin=(min(predictionyears)-2), xmax=(max(predictionyears)+1))
plt.ylim(ymin=0, ymax=800) 
plt.xlabel('Year', fontsize=12.0, fontweight='bold', **csfont, horizontalalignment='left', x=0.4) 
plt.ylabel('Incidents   of   Aircraft   Damage', fontweight='bold', fontsize=14.0, **csfont) 
plt.title('Actual and Predicted Incidents of Aircraft Damage \n from 2010 to 2021') 
# Remove top and right axes splines 
ax = plt.subplot(111)
for s in ['top', 'right']: 
    ax.spines[s].set_visible(False)
	
# Put the legend
font = font_manager.FontProperties(family='DejaVu Sans', size=10)
rect1 = Line2D([], [], marker="D", markersize=10, linewidth=0, color=(0, 0.3, 0.8, 0.8))
rect2 = Line2D([], [], marker="_", markersize=30, linewidth=0, color="black")
ax.legend((rect1, rect2), ('Actual', 'Predicted'), 
          loc='center right', frameon=False, prop=font, bbox_to_anchor=(1.4, 0.4), handletextpad=2, labelspacing=1.5)
		  
#show graph
plt.show()
