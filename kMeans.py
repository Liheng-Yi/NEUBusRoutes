import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from sklearn.cluster import KMeans



# Read the Shapefile
population_shp = './random_population_points2.shp'
population_data = gpd.read_file(population_shp)

# Ensure the data is in Web Mercator projection for contextily basemap
population_data = population_data.to_crs(epsg=3857)

# Plot the points on the map
# fig, ax = plt.subplots(figsize=(10, 10))
# population_data.plot(ax=ax, color='blue', markersize=5)
# Add a basemap

# # Set axis off
# ax.set_axis_off()
# plt.show()


n_clusters = 30  # specify the number of clusters
# Extract coordinates for clustering
coords = population_data.geometry.apply(lambda geom: (geom.x, geom.y)).tolist()

# Run KMeans clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coords)

# Get centroids of each cluster
centroids = kmeans.cluster_centers_

# Plotting
fig, ax = plt.subplots(figsize=(10, 10))

# Plot each centroid
for centroid in centroids:
    ax.plot(centroid[0], centroid[1], 'o', markersize=10)  # Adjust the marker size as needed

# Add a basemap
ctx.add_basemap(ax)

# Set axis off
ax.set_axis_off()

plt.show()







