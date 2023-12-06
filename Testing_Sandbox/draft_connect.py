from  draft_pathfind import short_path
from  draft_pathfind import get_coordinates
from  draft_path_Between_Nodes import two_coordinates_to_distance_and_bearing

new_list = []
second_list = []

def from_name_to_coordinates(node_list):
    for node in node_list:
        new_list.append(get_coordinates(node))

    return new_list

def from_coordinates_to_distance(new_list):
    del second_list[:]
    for i in range (0, len(new_list)-1):
        distance_and_bearing = two_coordinates_to_distance_and_bearing(new_list[i], new_list[i+1])
        first_value = distance_and_bearing[0]
        modified_tuple = (84922.48010 * first_value, distance_and_bearing[1])
        second_list.append(modified_tuple)
    
    return second_list

if __name__ == "__main__":
    start_point = input("Enter the starting point: ")
    end_point = input("Enter the end point: ")
    node_list = short_path(start_point, end_point)

    # array of nodes -> draft connect function
    new_list = from_name_to_coordinates(node_list)
    second_list = from_coordinates_to_distance(new_list)

    print(f"Second list: {second_list}")

    