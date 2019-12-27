import math
import heapq

def distance_value(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def shortest_path(M,start,goal):
    print('shortest_path called')
    
    if start == goal:
        return [start]
    
    explored = {} # intersection : [previous, path cost]
    frontier = {} # intersection : path cost + estimated distance to goal
    frontierhq = [] # [(path cost + estimated distance to goal, intersection)]
    goal_paths = {} # path cost: [intersections]
    
    goal_point = M.intersections[goal]
    
    current_node = start
    current_point = M.intersections[current_node]
    
    explored[current_node] = [0, 0]
    
    frontierhq.append((distance_value(current_point, goal_point), current_node))
    heapq.heapify(frontierhq)
    
    while len(frontierhq) > 0:
        current_node = heapq.heappop(frontierhq)[1]
        
        for child_node in M.roads[current_node]:
            # if the next node is the goal node,
            # work back to get the path
            if child_node == goal:
                intersections = [child_node]
                intersections.append(current_node)
                previous_intersection = explored[current_node][0]
            
                while previous_intersection != start:
                    intersections.append(previous_intersection)
                    previous_intersection = explored[previous_intersection][0]

                intersections.append(start)
                
                # reverse to put list in order from start to goal
                intersections = intersections[::-1]
                
                # add path to dict, with its cost as its key
                goal_paths[explored[current_node][1]] = intersections
            
            # if the node isn't part of an existing path, explore it and update the frontier
            elif child_node not in explored:
                child_point = M.intersections[child_node]
                
                child_path_cost = explored[current_node][1] + distance_value(current_point, child_point)
                explored[child_node] = [current_node, child_path_cost]
                
                child_goal_estimate = distance_value(child_point, goal_point)
                
                # the weight of child_path_cost is unchanged, since it is a calculated "real" value
                # the weight of child_goal_estimate is reduced, since it is only an estimation
                heapq.heappush(frontierhq, (child_path_cost + math.pow(child_goal_estimate,-2), child_node))
    
    goal_paths_lst = sorted(goal_paths.items())
    return goal_paths_lst[0][1]