import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np

# Read the Shapefile
population_shp = './random_population_points2.shp'
population_data = gpd.read_file(population_shp)

# Plotting before clustering
fig, ax = plt.subplots(figsize=(10, 10))
population_data.plot(ax=ax, color='blue', markersize=5)

# Extract coordinates and weights for clustering
coords = np.array(list(zip(population_data.geometry.x, population_data.geometry.y)))
weights = population_data['weight'].to_numpy()  # Replace 'weight' with the actual column name for weights

# Perform DBSCAN clustering
db = DBSCAN(eps=0.01, min_samples=3).fit(coords)
labels = db.labels_

# Create a graph network
G = nx.Graph()

# Add nodes with the population as an attribute, using the cluster labels
for label in set(labels):
    if label != -1:  # -1 is noise in DBSCAN
        # Calculate centroid of the cluster
        members = coords[labels == label]
        centroid = np.mean(members, axis=0)
        # Calculate total weight for the cluster
        total_weight = weights[labels == label].sum()
        # Add a single node for the cluster
        G.add_node(label, pos=tuple(centroid), weight=total_weight)

# Visualization
pos = nx.get_node_attributes(G, 'pos')
sizes = [G.nodes[node]['weight']*10 for node in G.nodes()]  # Scale node size by weight
nx.draw(G, pos, node_size=sizes, with_labels=True)

plt.show()
