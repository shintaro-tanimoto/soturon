import find_graph as fg
import find_coordinates as fc
import networkx as nx

unit_number = 8
unique_graphs_list = fg.find_unique_graphs_list(unit_number)

"""fg.draw_graph(unique_graphs_list)"""

#test
print(unique_graphs_list[0].nodes[0])

