from math import sqrt, pow

def estimated_distance(origin, destination):
    return sqrt(pow((origin[0] - destination[0]), 2) + pow((origin[1] - destination[1]), 2))

def shortest_path(graph, start, end):
    g_cost_to_node = {}  # Cost to each position from the start position
    f_score_to_node = {}  # Estimated cost of start to end going via this position

    g_cost_to_node[start] = 0
    f_score_to_node[start] = estimated_distance(graph.intersections[start], graph.intersections[end])

    closed_nodes = set()
    open_nodes = set([start])
    came_from = {}

    while len(open_nodes) > 0:
        # Get the node in the open list with the lowest f_score
        current = None
        current_f_score = None
        for node in open_nodes:
            if current is None or f_score_to_node[node] < current_f_score:
                current_f_score = f_score_to_node[node]
                current = node
        # Check for if we have reached the goal
        if current == end:
            # Return the path backward
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        # Mark the current node as closed
        open_nodes.remove(current)
        closed_nodes.add(current)

        for neighbor in graph.roads[current]:
            if neighbor in closed_nodes:
                continue  # if already visited
            candidate_g = g_cost_to_node[current] + estimated_distance(graph.intersections[current], graph.intersections[neighbor])

            if neighbor not in open_nodes:
                open_nodes.add(neighbor)  # new node discovered
            elif candidate_g >= g_cost_to_node[neighbor]:
                continue  # This g_cost is worse than previously found

            # Adopt this g_cost score
            came_from[neighbor] = current
            g_cost_to_node[neighbor] = candidate_g
            h_score = estimated_distance(graph.intersections[neighbor], graph.intersections[end])
            f_score_to_node[neighbor] = g_cost_to_node[neighbor] + h_score
