import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

with open('hours', 'r') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [float(line.split()[1]) for line in lines]

X = np.vstack((x,y)).transpose()

# Standarize features and KMeans over the dataset
print("Standarize features and KMeans over the dataset")
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=4,max_iter=30).fit(X_std)
print("cluster_centers -> \n", kmeans.cluster_centers_)
print("labels -> \n", kmeans.labels_)
csfont = {'fontname':'DejaVu Sans'}
plt.xlim(xmin=0, xmax=23)
plt.xticks([0,5,10,15,20])
plt.ylim(ymin=0, ymax=0.15)
plt.yticks([0.000,0.025,0.050,0.075,0.100,0.125,0.150])
plt.scatter(x, y, marker='o', c=kmeans.labels_, cmap='viridis')
plt.xlabel('Hours of the Day', fontsize=12.0, fontweight='bold', **csfont) 
plt.ylabel('Proportion of Bird Strikes Relative \n To State Total', fontweight='bold', fontsize=14.0, **csfont) 
plt.title('Cluster Visualization\n') 
plt.show()
