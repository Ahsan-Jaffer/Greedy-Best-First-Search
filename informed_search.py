# *********************** Greedy Best First Search **************************

import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    came_from = {}
    came_from[start] = None
    closed_list = set()

    while open_list:
        _, current = heapq.heappop(open_list)     # _ = heuristic value   current = node

        if current == goal : 
            path = []
            while current:
                path.append(current)
                current = came_from[current]

            return path[::-1]  #Reverse the Path
        
        closed_list.add(current)

        for neighbor in graph[current]:
            if neighbor not in closed_list:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor)) 
                came_from[neighbor] = current

    return None


#Example Usage

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : [],

}

heuristic = {
    'A' : 6,
    'B' : 4,
    'C' : 4,
    'D' : 2,
    'E' : 2,
    'F' : 1,
    'G' : 0  #Goal
}

path = greedy_best_first_search(graph, 'A', 'G', heuristic)
print(f"Path found : {path}")


