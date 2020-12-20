import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.font_manager as font_manager

with open('StatesAndTop10Airports', 'r') as f:
    lines = f.readlines()
    statenames = [line.split()[0] for line in lines]	
    incidentcountairports = [int(line.split()[1]) for line in lines]
    incidentcountstates = [int(line.split()[2]) for line in lines]

# Prepare stacked box plot
fig = plt.figure()
ax = fig.add_subplot(111)

# Set the stacked bars
ax.barh(statenames, incidentcountairports, align='center', height=.40, color=(0, 0.3, 0.8, 0.8), label='wait time')
ax.barh(statenames, incidentcountstates, align='center', height=.40, left=incidentcountairports, color='brown', label='run time')

# Set ticks and labels for X and Y axis
plt.xticks([0, 2000, 4000, 6000, 8000, 10000, 12000, 14000]) 
ax.set_xlabel('#  of  Strikes', fontweight='bold', fontsize=11)
ax.grid(axis='x', color='#646464') 
ax.set_yticks(statenames)
ax.set_ylabel('State', fontweight='bold')
ax.set_axisbelow(True)

# Remove y Ticks but leave X Ticks
ax.yaxis.set_ticks_position('none') 

# Remove top axes splines 
ax.spines['top'].set_visible(False)
# Remove other axes spline colors 
for s in ['left', 'bottom', 'right']: 
    ax.spines[s].set_color('#646464')

# Set title - Center it with spaces - :-(
ax.set_title('              Count of Wildlife Strikes for Top 10 US States (2010-2019)', fontweight='bold', fontsize=9.5, loc ='left')


# Put the legend
font = font_manager.FontProperties(family='DejaVu Sans', weight='bold', size=8)
rect1 = Line2D([], [], marker="s", markersize=5, linewidth=0, color=(0, 0.3, 0.8, 0.8))
rect2 = Line2D([], [], marker="s", markersize=5, linewidth=0, color="brown")
ax.legend((rect1, rect2), ('Airport_With_Max_Strikes', 'Total_Strikes_For_State'), 
          loc='center right', frameon=False, prop=font, bbox_to_anchor=(1.45, 0.5), handletextpad=-0.2, labelspacing=1.5)

# Now show it
plt.show()
