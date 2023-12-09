
# n_clusters = 20  # specify the number of clusters
# # Extract coordinates for clustering
# coords = population_data.geometry.apply(lambda geom: (geom.x, geom.y)).tolist()

# # Run KMeans clustering
# kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(coords)

# # Get centroids of each cluster
# centroids = kmeans.cluster_centers_

# # Plotting
# fig, ax = plt.subplots(figsize=(10, 10))

# # Plot each centroid
# for centroid in centroids:
#     ax.plot(centroid[0], centroid[1], 'o', markersize=3)  # Adjust the marker size as needed


# # Add a basemap
# ctx.add_basemap(ax)

# # Set axis off
# ax.set_axis_off()

# plt.show()

