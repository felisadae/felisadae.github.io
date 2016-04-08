__author__ = 'Abhipray'

import random
import datetime
import search


def sort_cities(origin, cities):
    """
    Sort the cities based on distance from origin
    :param origin:
    :param cities:
    :return:
    """
    closest_cities = []
    for city in cities:
        # d = get_flight_duration(origin, city)
        d = random.choice(range(10,100))
        # print city, d
        closest_cities.append((d, city))
    closest_cities.sort()
    return closest_cities

def dist_estimator(start, end):
    # return get_flight_duration(start, end)
    return random.choice(range(10, 200))


def path_finder(origin, prefs=[],avoid=[], N=30, weather=[]):
    to_visit = set(prefs).difference(set(avoid))
    continents = get_continent_dict()
    #Pick cities randomly uniformly from each continent
    n_each = (N-len(to_visit))/len(continents)
    for cont in continents:
        to_append = random.shuffle(continents[cont])[0:n_each]
        to_visit += to_append
    return flight_router(origin, to_visit)
    

def flight_router(origin, to_visit=[]):
    """
    path_finder takes in an origin and picks out a path through popular cities based on shortest flight duration.
    This is done greedily to minimize the passenger travel time on each flight.
    :param origin: a string representing the origin airport code
    :return: path: a list of airport codes representing the path
    """
    ##Find out flight duration between cities
    #kevin's call to get a dictionary that looks like-
    #{'airport_code':{'airport2':flight_duration}}
    # cities_dict = generate_graph();
    # cities_dict = {'YXU': {'CDG': 55,'BKK': 175}, 'CDG': {'YXU': 55,'BKK': 265}, 'BKK': {'CDG': 265,'YXU': 175}}
    cities_dict = {'JFK': {'YXU': 174, 'CDG': 435, 'HND': 230, 'VIE': 90, 'BKK': 950, 'SIN': 950, 'BCN': 205, 'MXP': 165, \
            'TSA': 180, 'DXB': 75, 'KUL': 465, 'LAX': 315, 'PVG': 155, 'RUH': 80, 'AMS': 190, 'GMP': 115, 'HKG': 265}
            , 'YXU': {'JFK': 174, 'BKK': 100, 'CDG': 55, 'HND': 720, 'VIE': 135, 'DXB': 956, 'SIN': 225, 'BCN': 545, 'MXP': 530, \
             'TSA': 180, 'KUL': 225, 'LAX': 180, 'PVG': 830, 'RUH': 410, 'AMS': 75, 'GMP': 130, 'HKG': 740},  \
             'CDG': {'JFK': 435, 'YXU': 55, 'HND': 675, 'VIE': 90, 'BKK': 175, 'SIN': 60, 'BCN': 115, 'MXP': 85, 'TSA': 120,\
                     'DXB': 290, 'KUL': 465, 'LAX': 770, 'PVG': 580, 'RUH': 80, 'AMS': 60, 'GMP': 120, 'HKG': 605},
             'HND': {'JFK': 230, 'YXU': 720, 'RUH': 245, 'CDG': 675, 'VIE': 340, 'BCN': 675, 'BKK': 185, 'TSA': 180, \
                     'MXP': 675, 'DXB': 675, 'SIN': 185, 'KUL': 145, 'LAX': 835, 'PVG': 110, 'AMS': 675, 'GMP': 140, 'HKG': 185},\
             'VIE': {'JFK': 90, 'YXU': 135, 'CDG': 90, 'HND': 340, 'BKK': 155, 'TSA': 150, 'BCN': 140, 'MXP': 90, 'DXB': 120,
                     'SIN': 100, 'KUL': 100, 'LAX': 770, 'PVG': 155, 'RUH': 160, 'AMS': 90, 'GMP': 100, 'HKG': 340}, \
             'BKK': {'JFK': 950, 'YXU': 100, 'CDG': 175, 'HND': 185, 'VIE': 155, 'DXB': 190, 'SIN': 150, 'BCN': 230, 'MXP': 180, \
                     'TSA': 120, 'KUL': 125, 'LAX': 84, 'PVG': 105, 'RUH': 80, 'AMS': 195, 'GMP': 120, 'HKG': 160},
             'TSA': {'JFK': 180, 'YXU': 180, 'CDG': 120, 'HND': 180, 'VIE': 150, 'BKK': 120, 'SIN': 120, 'BCN': 150, 'MXP': 95, \
                     'DXB': 150, 'KUL': 120, 'LAX': 700, 'PVG': 100, 'RUH': 80, 'AMS': 150, 'GMP': 105, 'HKG': 100},
             'BCN': {'JFK': 205, 'YXU': 545, 'CDG': 115, 'HND': 675, 'VIE': 140, 'BKK': 230, 'TSA': 150, 'MXP': 85, \
                     'DXB': 200, 'SIN': 105, 'KUL': 105, 'LAX': 640, 'PVG': 580, 'RUH': 160, 'AMS': 135, 'GMP': 115, 'HKG': 265},
             'MXP': {'JFK': 165, 'YXU': 530, 'CDG': 85, 'HND': 675, 'VIE': 90, 'BKK': 180, 'TSA': 95, 'BCN': 85, 'DXB': 160, 'SIN': 165, \
                     'KUL': 305, 'LAX': 770, 'PVG': 580, 'RUH': 160, 'AMS': 60, 'GMP': 220, 'HKG': 90}, \
             'DXB': {'JFK': 75, 'YXU': 956, 'CDG': 290, 'HND': 675, 'VIE': 120, 'BKK': 190, 'SIN': 240, 'BCN': 200, \
                     'MXP': 160, 'TSA': 150, 'KUL': 215, 'LAX': 270, 'PVG': 435, 'RUH': 70, 'AMS': 170, 'GMP': 130, 'HKG': 140}, \
             'SIN': {'JFK': 950, 'YXU': 225, 'CDG': 60, 'HND': 185, 'VIE': 100, 'BKK': 150, 'BCN': 105, 'MXP': 165, 'TSA': 120,\
                     'DXB': 240, 'KUL': 60, 'LAX': 825, 'PVG': 155, 'RUH': 80, 'AMS': 730, 'GMP': 120, 'HKG': 225}, \
             'KUL': {'JFK': 465, 'YXU': 225, 'CDG': 465, 'HND': 145, 'VIE': 100, 'BKK': 125, 'TSA': 120, 'BCN': 105, 'MXP': 305,\
                     'DXB': 215, 'SIN': 60, 'LAX': 825, 'PVG': 155, 'RUH': 80, 'AMS': 730, 'GMP': 120, 'HKG': 225},
             'LAX': {'JFK': 315, 'YXU': 180, 'CDG': 770, 'HND': 835, 'VIE': 770, 'BKK': 84, 'TSA': 700, 'BCN': 640, \
                     'MXP': 770, 'DXB': 270, 'SIN': 825, 'KUL': 825, 'PVG': 760, 'RUH': 635, 'AMS': 640, 'GMP': 845, 'HKG': 825},
             'PVG': {'JFK': 155, 'YXU': 830, 'CDG': 580, 'HND': 110, 'VIE': 155, 'BKK': 105, 'TSA': 100, 'BCN': 580, 'MXP': 580,\
                     'DXB': 435, 'SIN': 155, 'KUL': 155, 'LAX': 760, 'RUH': 80, 'AMS': 190, 'GMP': 90, 'HKG': 160}, \
             'RUH': {'JFK': 80, 'YXU': 410, 'CDG': 80, 'HND': 245, 'VIE': 160, 'BKK': 80, 'TSA': 80, 'BCN': 160, 'MXP': 160, \
                     'DXB': 70, 'SIN': 80, 'KUL': 80, 'LAX': 635, 'PVG': 80, 'AMS': 160, 'GMP': 80, 'HKG': 80},\
             'AMS': {'JFK': 190, 'YXU': 75, 'CDG': 60, 'HND': 675, 'VIE': 90, 'BKK': 195, 'TSA': 150, 'BCN': 135, 'MXP': 60,\
                     'DXB': 170, 'SIN': 730, 'KUL': 730, 'LAX': 640, 'PVG': 190, 'RUH': 160, 'GMP': 75, 'HKG': 190},\
             'GMP': {'JFK': 115, 'YXU': 130, 'CDG': 120, 'HND': 140, 'VIE': 100, 'BKK': 120, 'SIN': 120, 'BCN': 115, 'MXP': 220, 'DXB': 130,\
                     'KUL': 120, 'LAX': 845, 'PVG': 90, 'RUH': 80, 'AMS': 75, 'TSA': 105, 'HKG': 120},\
             'HKG': {'JFK': 265, 'YXU': 740, 'CDG': 605, 'HND': 185, 'VIE': 340, 'BKK': 160, 'SIN': 225, 'BCN': 265, 'MXP': 90,\
                     'TSA': 100, 'KUL': 225, 'LAX': 825, 'PVG': 160, 'RUH': 80, 'AMS': 190, 'GMP': 120, 'DXB': 140}}

    path = [origin]
    visited = set([origin])
    ####1. Handle the preferences list first####
    #To do this, do an A* search from origin to every node on the to_visit list

    #Find the closest city in to_visit list from the origin
    closest_cities_in_pref = sort_cities(origin, to_visit) #returns (distance, city name)

    #Go through the sorted list and find the shortest path from the origin to the list element, if available, set the
    #  new origin as the element of the list
    tmp = origin

    for i in closest_cities_in_pref:
        predecessors = {}
        for ne in search.astar_search(tmp, i[1], cities_dict, dist_estimator, visited):
            if ne.get_predecessor() is not None:
                predecessors[ne.get_node()] = ne.get_predecessor()
        tmp_path = []
        for e in search.findpath(tmp, i[1], predecessors):
            print i[1], e
            tmp_path.append(e[1])
            visited.add(e[1])
        tmp_path.reverse()
        path += tmp_path
        tmp = i[1]


    # print len(cities_dict)
    #Find the flight duration from origin to each city in the list using kevin's call

    #Do the rest of the cities greedily
    # closest_city_name = closest_cities_in_cities_dict[1]
    #
    # #Sort based on flight durations
    # #Create a list of tuples [(city1, flight_duration)....]
    # for i in cities_dict:
    #     #Find the closest city to this one
    #     closest_cities = sorted([(value, key) for (key, value) in cities_dict[closest_city_name].items()])
    #     flag = False
    #     # print closest_cities
    #     for c in closest_cities:
    #         if c[1] not in visited:
    #             closest_city_name = c[1]
    #             visited.add(closest_city_name)
    #             flag = True
    #             break
    #     # print visited
    #     if flag:
    #         path.append(closest_city_name)
    # path.append(origin) #Close the loop
    return path


def estimate_total_price(path, start_date, num_days=80):
    """
        Given a list of airport codes, it returns an estimate of the ticket expenses, spacing out each day uniformly to
    cover num_days days.
    :param path: list of airport codes as strings
    :param num_days: default 80 days
    :param start_date: datetime object representing start date
    :return:
    """
    num_cities = len(path)
    #Assuming the traveler spends equal number of days at each place
    airport_to_depTime = []
    for i in range(num_cities-1):
        airport_to_depTime.append((path[i], path[i+1], start_date + datetime.timedelta(num_days/num_cities)))
    ticket_prices = get_flight_prices(airport_to_depTime)
    return ticket_prices


print path_finder('JFK', prefs=['LAX','PVG','GMP'])
# out = path_finder('JFK')
# print out, len(out)

