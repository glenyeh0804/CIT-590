import random
from math import *


def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    """Copy from earth_distance.py to calculate distance"""
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c


def read_cities(file_name):
    """Read the city-data.txt and output a list with tuples"""
    road_map = []
    with open(file_name, 'r') as list:
        for line in list.readlines():
            new_line = line.split('\t')
            new_line[3] = new_line[3].strip('\n')
            data = (new_line[0], new_line[1], new_line[2], new_line[3])
            road_map.append(data)
    return road_map

def print_cities(road_map):
    """Print the cities with their own locations """
    for i in road_map:
        print('City: ' + i[1] + ' | ' +'Latitude: ' + '{:.2f}'.format(float(i[2])) + ' | ' +
              'Longitude: ' + '{:.2f}'.format(float(i[3])))

def compute_total_distance(road_map):
    """Calculate the total distance and return the float value"""
    total_distance = 0
    for i in range(0, len(road_map)):
        x1 = float(road_map[i][2])
        x2 = float(road_map[(i + 1) % len(road_map)][2])
        y1 = float(road_map[i][3])
        y2 = float(road_map[(i + 1) % len(road_map)][3])
        total_distance += distance(x1, y1, x2, y2)
    return total_distance

def swap_adjacent_cities(road_map, index):
    """Swap the location of adjacent cities based on given index, and return the new list and total distance"""
    new_road_map = road_map[:]
    swap = new_road_map[index]

    if index == len(new_road_map) - 1:
        # if the index is the end of the list
        new_road_map[index] = new_road_map[0]
        new_road_map[0] = swap
    else:
        new_road_map[index] = new_road_map[index + 1]
        new_road_map[index + 1] = swap
    new_total_distance = compute_total_distance(new_road_map)
    output = (new_road_map, new_total_distance)
    return output

def swap_cities(road_map, index1, index2):
    """Swap the location of cities based on given two indexes, and return the new list and total distance"""
    new_road_map = road_map[:]
    swap = new_road_map[index1]

    if index1 == index2:
        # if the two indexes are equal, do nothing
        pass
    else:
        new_road_map[index1] = new_road_map[index2]
        new_road_map[index2] = swap
    new_total_distance = compute_total_distance(new_road_map)
    output = (new_road_map, new_total_distance)
    return output

def find_best_cycle(road_map):
    """Find the best cycle by swapping the elements in the list for 10,000 times"""

    shortest_distance = 100000
    new_road_map = road_map[:]
    best_cycle = []

    # Randomly swap the locations of two cities by 7,000 times
    for i in range(0, 7000):
        index1 = random.randint(0, len(road_map) - 1)
        index2 = random.randint(0, len(road_map) - 1)
        output = swap_cities(new_road_map, index1, index2)
        new_road_map = output[0][:]
        distances = float(output[1])
        if distances < shortest_distance:
            shortest_distance = distances
            best_cycle = new_road_map[:]

    # After finding out a good "road map", slightly optimize it by changing the locations of adjacent cities
    for i in range(0, 3000):
        index = random.randint(0, len(new_road_map) - 1)
        output = swap_adjacent_cities(new_road_map, index)
        new_road_map = output[0][:]
        distances = float(output[1])
        if distances < shortest_distance:
            shortest_distance = distances
            best_cycle = new_road_map[:]
    return best_cycle

def print_map(road_map):
    """Find out the best cycle, calculate the distance between each city, and print the map"""

    best_cycle = find_best_cycle(road_map)
    for i in range(0, len(best_cycle)):
        x1 = float(best_cycle[i][2])
        x2 = float(best_cycle[(i + 1) % len(best_cycle)][2])
        y1 = float(best_cycle[i][3])
        y2 = float(best_cycle[(i + 1) % len(best_cycle)][3])
        each_connection_distance = distance(x1, y1, x2, y2)
        if i < 9:
            print('Connection', i + 1, '  From: ' + best_cycle[i][1] + ' => ' +
              'To: ' + best_cycle[(i + 1) % len(best_cycle)][1] + ' | ' +
              'The distance is:', each_connection_distance)
        else:
            print('Connection', i + 1, ' From: ' + best_cycle[i][1] + ' => ' +
              'To: ' + best_cycle[(i + 1) % len(best_cycle)][1] + ' | ' +
              'The distance is:', each_connection_distance)
    total_distance = compute_total_distance(best_cycle)
    print('\nThe total distance of this journey: ', total_distance)

def main():
    """The main function of this program"""

    road_map = read_cities('city-data.txt')
    print('The list of city data:\n')
    print_cities(road_map)
    print('\nThe optimized trip for salesman:\n')
    print_map(road_map)

if __name__ == "__main__":
    main()


