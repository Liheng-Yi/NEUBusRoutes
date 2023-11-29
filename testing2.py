import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

# Read the Shapefile
population_shp = './random_population_points2.shp'
population_data = gpd.read_file(population_shp)

# Create a graph network
G = nx.Graph()

# Add nodes with the population as an attribute
for _, row in population_data.iterrows():
    point = row['geometry']
    population = row['population']  # replace 'population' with the actual field name
    G.add_node(point, population=population)




print("starting visualiztion")
# Visualization
pos = {point: (point.x, point.y) for point in G.nodes()}
nx.draw(G, pos, node_size=5, with_labels=False)
node_labels = nx.get_node_attributes(G, 'population')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=6)

plt.show()
