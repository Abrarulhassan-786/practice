#abrar ul hassan 10970
ROMANIA_GRAPH = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def find_shortest_path(start_city, end_city, graph):
    initial_state = {
        'path': [start_city],
        'cost': 0
    }
    queue = [initial_state]
    best_path = None
    best_cost = float('inf')
    while queue:
        current_state = queue.pop(0)
        current_city = current_state['path'][-1]
        if current_city == end_city and current_state['cost'] < best_cost:
            best_path = current_state['path']
            best_cost = current_state['cost']
        for neighbor_city in graph[current_city]:
            if neighbor_city in current_state['path']:
                continue
            path_cost = current_state['cost'] + graph[current_city][neighbor_city]
            new_state = {
                'path': current_state['path'] + [neighbor_city],
                'cost': path_cost
            }
            queue.append(new_state)
            queue = sorted(queue, key=lambda x: x['cost'])
    return best_path, best_cost

startcity= input('Please Enter First City Name \n') 
endcity = input('Please Enter Second City Name \n') 

find_shortest_path(startcity,endcity ,ROMANIA_GRAPH)
