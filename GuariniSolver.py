import networkx as nx
import itertools as it

# Start creating the graph of all configurations
G = nx.Graph()
# Iterate through all possible strings of length 8 with two W's and two B's
for wb_indices in it.permutations(range(8), 4):
	# print(wb_indices)
	configuration = ['*'] * 8
	configuration[wb_indices[0]] = 'W'
	configuration[wb_indices[1]] = 'W'
	configuration[wb_indices[2]] = 'B'
	configuration[wb_indices[3]] = 'B'
	# print(configuration)
	# print("".join(configuration))
	# str.join() method returns a string in which the string elements of sequence have been joined by str separator
	G.add_node("".join(configuration))

# Fill in a list moves: move[i] are the sequence numbers of cells where a knight can move from the i-th cell
# '_' is a throwaway variable which is not actually used.
# moves is a two dimensional array list
moves = [[] for _ in range(8)]
moves[0] = [4, 6]
moves[1] = [5, 7]
moves[2] = [3, 6]
moves[3] = [2, 7]
moves[4] = [0, 5]
moves[5] = [1, 4]
moves[6] = [0, 2]
moves[7] = [1, 3]

# Add edges to the graph
for node in G.nodes():
	# Get the list representation of a configuration of a graph
	configuration = [c for c in node]

	for i in range(8):
		# Only moving a knight can change the configuration 
		if configuration[i] != "*":
			# Iterate all possible one move positions
			for new_pos in moves[i]:
				# Move only takes effect when there is no knight on the intended position
				if configuration[new_pos] != "*":
					continue
				# Convert array to list
				new_configuration = list(configuration)
				# When the knight is moved, the original position becomes blank
				new_configuration[i] = "*"
				# The knight has been moved to the new position
				new_configuration[new_pos] = configuration[i]
				# If there is no edge between the old configuration and the new configuration, add an edge
				if not G.has_edge("".join(configuration), "".join(new_configuration)):
					G.add_edge("".join(configuration), "".join(new_configuration))

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(nx.number_connected_components(G))

assert "W*B**W*B" in nx.node_connected_component(G, "W*W**B*B")
assert "B*B**W*W" in nx.node_connected_component(G, "W*W**B*B")
assert "W*B**B*W" not in nx.node_connected_component(G, "W*W**B*B")

print(" -> ".join(nx.shortest_path(G, "W*W**B*B", "B*B**W*W")))