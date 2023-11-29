import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np
# base map
import contextily as ctx

# Read the Shapefile
population_shp = './random_population_points2.shp'
population_data = gpd.read_file(population_shp)

print("before clustering")
fig, ax = plt.subplots(figsize=(10, 10))
population_data.plot(ax=ax, color='blue', markersize=5)
# plt.title('Map before clustering')
# ctx.add_basemap(ax)
# plt.show()

# Extract coordinates for clustering
coords = np.array(list(zip(population_data.geometry.x, population_data.geometry.y)))

print("Extracting coordinates")
# Perform DBSCAN clustering
# eps is the maximum distance between two samples for them to be considered in the same neighborhood
# min_samples is the number of samples in a neighborhood for a point to be considered a core point
db = DBSCAN(eps=0.01, min_samples=3).fit(coords)
labels = db.labels_

# Number of clusters in labels, ignoring noise if present
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print(f'Estimated number of clusters: {n_clusters_}')

# Create a graph network
G = nx.Graph()

# Add nodes with the population as an attribute, using the cluster labels
for label in set(labels):
    if label != -1:  # -1 is noise in DBSCAN
        # Calculate centroid of the cluster
        members = coords[labels == label]
        centroid = np.mean(members, axis=0)
        # Add a single node for the cluster
        G.add_node(label, pos=tuple(centroid), count=len(members))
        print("not noise")

# Print a status message
print("Done adding nodes for clusters")
print("visualizating")
# Visualization
pos = nx.get_node_attributes(G, 'pos')
sizes = [G.nodes[node]['count']*10 for node in G.nodes()]  # Scale node size by count
nx.draw(G, pos, node_size=sizes, with_labels=True)

plt.show()
