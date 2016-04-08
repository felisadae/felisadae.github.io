__author__ = 'Abhipray'

import random
import datetime


def path_finder(origin):
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
    cities_dict = {'JFK': {'BCN': 205, 'HND': 230, 'TSA': 180, 'KUL': 465, 'YUL': 90, 'BKK': 950, 'SIN': 950, 'YXU': 174, 'PVG': 155, 'AMS': 190, 'HKG': 265, 'YVR': 439, 'IAD': 79, 'GIG': 882, 'GMP': 115, 'ZRH': 660, 'RUH': 80, 'CDG': 435, 'VIE': 90, 'EDI': 820, 'MXP': 165, 'MEX': 479, 'SFO': 317, 'LAX': 315, 'OGG': 728, 'SYD': 1238, 'DXB': 75, 'LAS': 290}, 'BCN': {'JFK': 205, 'HND': 675, 'TSA': 150, 'KUL': 105, 'YUL': 1050, 'BKK': 230, 'SIN': 105, 'YXU': 545, 'PVG': 580, 'AMS': 135, 'HKG': 265, 'YVR': 1110, 'IAD': 1055, 'GIG': 1947, 'GMP': 115, 'ZRH': 105, 'RUH': 160, 'CDG': 115, 'VIE': 140, 'EDI': 910, 'MXP': 85, 'MEX': 1015, 'SFO': 1190, 'LAX': 640, 'OGG': 1289, 'SYD': 2120, 'DXB': 200, 'LAS': 870}, 'HND': {'JFK': 230, 'BCN': 675, 'TSA': 180, 'KUL': 145, 'YUL': 1224, 'BKK': 185, 'SIN': 185, 'YXU': 720, 'PVG': 110, 'AMS': 675, 'HKG': 185, 'YVR': 1720, 'IAD': 1106, 'GIG': 2193, 'GMP': 140, 'ZRH': 1440, 'RUH': 245, 'CDG': 675, 'VIE': 340, 'EDI': 1450, 'MXP': 675, 'MEX': 1515, 'SFO': 1835, 'LAX': 835, 'OGG': 659, 'SYD': 1090, 'DXB': 675, 'LAS': 2210}, 'TSA': {'JFK': 180, 'BCN': 150, 'HND': 180, 'KUL': 120, 'YUL': 1320, 'YXU': 180, 'SIN': 120, 'BKK': 120, 'PVG': 100, 'AMS': 150, 'HKG': 100, 'YVR': 1500, 'IAD': 1485, 'GIG': 2275, 'GMP': 105, 'ZRH': 1020, 'RUH': 80, 'CDG': 120, 'VIE': 150, 'EDI': 1195, 'MXP': 95, 'MEX': 1500, 'SFO': 1550, 'LAX': 700, 'OGG': 2791, 'SYD': 1905, 'DXB': 150, 'LAS': 1705}, 'KUL': {'JFK': 465, 'BCN': 105, 'HND': 145, 'TSA': 120, 'YUL': 1800, 'BKK': 125, 'SIN': 60, 'YXU': 225, 'PVG': 155, 'AMS': 730, 'HKG': 225, 'YVR': 1230, 'IAD': 1815, 'GIG': 1854, 'GMP': 120, 'ZRH': 1210, 'RUH': 80, 'CDG': 465, 'VIE': 100, 'EDI': 960, 'MXP': 305, 'MEX': 2827, 'SFO': 1295, 'LAX': 825, 'OGG': 1964, 'SYD': 530, 'DXB': 215, 'LAS': 1620}, 'YUL': {'JFK': 90, 'BCN': 1050, 'HND': 1224, 'TSA': 1320, 'KUL': 1800, 'BKK': 1420, 'SIN': 1815, 'YXU': 158, 'PVG': 1775, 'AMS': 995, 'HKG': 1310, 'YVR': 471, 'IAD': 334, 'GIG': 1187, 'GMP': 1520, 'ZRH': 1005, 'RUH': 1490, 'CDG': 420, 'VIE': 775, 'EDI': 690, 'MXP': 1035, 'MEX': 518, 'SFO': 479, 'LAX': 466, 'OGG': 1003, 'SYD': 2075, 'DXB': 1080, 'LAS': 425}, 'BKK': {'JFK': 950, 'BCN': 230, 'HND': 185, 'TSA': 120, 'KUL': 125, 'YUL': 1420, 'SIN': 150, 'YXU': 100, 'PVG': 105, 'AMS': 195, 'HKG': 160, 'YVR': 1135, 'IAD': 1695, 'GIG': 1544, 'GMP': 120, 'ZRH': 845, 'RUH': 80, 'CDG': 175, 'VIE': 155, 'EDI': 1085, 'MXP': 180, 'MEX': 1527, 'SFO': 1255, 'LAX': 84, 'OGG': 1814, 'SYD': 535, 'DXB': 190, 'LAS': 1681}, 'SIN': {'JFK': 950, 'BCN': 105, 'HND': 185, 'TSA': 120, 'KUL': 60, 'YUL': 1815, 'BKK': 150, 'YXU': 225, 'PVG': 155, 'AMS': 730, 'HKG': 225, 'YVR': 1105, 'IAD': 1680, 'GIG': 1747, 'GMP': 120, 'ZRH': 1420, 'RUH': 80, 'CDG': 60, 'VIE': 100, 'EDI': 1040, 'MXP': 165, 'MEX': 1680, 'SFO': 1160, 'LAX': 825, 'OGG': 1826, 'SYD': 720, 'DXB': 240, 'LAS': 1466}, 'YXU': {'JFK': 174, 'BCN': 545, 'HND': 720, 'TSA': 180, 'KUL': 225, 'YUL': 158, 'SIN': 225, 'BKK': 100, 'PVG': 830, 'AMS': 75, 'HKG': 740, 'YVR': 390, 'IAD': 214, 'GIG': 1425, 'GMP': 130, 'ZRH': 1483, 'RUH': 410, 'CDG': 55, 'VIE': 135, 'EDI': 699, 'MXP': 530, 'MEX': 408, 'SFO': 533, 'LAX': 180, 'OGG': 839, 'SYD': 1523, 'DXB': 956, 'LAS': 910}, 'PVG': {'JFK': 155, 'BCN': 580, 'HND': 110, 'TSA': 100, 'KUL': 155, 'YUL': 1775, 'BKK': 105, 'SIN': 155, 'YXU': 830, 'AMS': 190, 'HKG': 160, 'YVR': 1480, 'IAD': 1705, 'GIG': 1798, 'GMP': 90, 'ZRH': 885, 'RUH': 80, 'CDG': 580, 'VIE': 155, 'EDI': 935, 'MXP': 580, 'MEX': 1517, 'SFO': 1165, 'LAX': 760, 'OGG': 1134, 'SYD': 970, 'DXB': 435, 'LAS': 1523}, 'AMS': {'JFK': 190, 'BCN': 135, 'HND': 675, 'TSA': 150, 'KUL': 730, 'YUL': 995, 'BKK': 195, 'SIN': 730, 'YXU': 75, 'PVG': 190, 'HKG': 190, 'YVR': 865, 'IAD': 605, 'GIG': 1922, 'GMP': 75, 'ZRH': 220, 'RUH': 160, 'CDG': 60, 'VIE': 90, 'EDI': 745, 'MXP': 60, 'MEX': 635, 'SFO': 1135, 'LAX': 640, 'OGG': 1300, 'SYD': 1495, 'DXB': 170, 'LAS': 965}, 'HKG': {'JFK': 265, 'BCN': 265, 'HND': 185, 'TSA': 100, 'KUL': 225, 'YUL': 1310, 'BKK': 160, 'SIN': 225, 'YXU': 740, 'PVG': 160, 'AMS': 190, 'YVR': 975, 'IAD': 1350, 'GIG': 2143, 'GMP': 120, 'ZRH': 850, 'RUH': 80, 'CDG': 605, 'VIE': 340, 'EDI': 1090, 'MXP': 90, 'MEX': 1802, 'SFO': 965, 'LAX': 825, 'OGG': 1034, 'SYD': 845, 'DXB': 140, 'LAS': 1310}, 'YVR': {'JFK': 439, 'BCN': 1110, 'HND': 1720, 'TSA': 1500, 'KUL': 1230, 'YUL': 471, 'BKK': 1135, 'SIN': 1105, 'YXU': 390, 'PVG': 1480, 'AMS': 865, 'HKG': 975, 'IAD': 610, 'GIG': 1175, 'GMP': 1825, 'ZRH': 770, 'RUH': 1655, 'CDG': 1080, 'VIE': 1335, 'EDI': 1750, 'MXP': 1020, 'MEX': 620, 'SFO': 141, 'LAX': 165, 'OGG': 366, 'SYD': 1405, 'DXB': 1400, 'LAS': 155}, 'IAD': {'JFK': 79, 'BCN': 1055, 'HND': 1106, 'TSA': 1485, 'KUL': 1815, 'YUL': 334, 'BKK': 1695, 'SIN': 1680, 'YXU': 214, 'PVG': 1705, 'AMS': 605, 'HKG': 1350, 'YVR': 610, 'GIG': 1238, 'GMP': 1415, 'ZRH': 670, 'RUH': 1045, 'CDG': 620, 'VIE': 955, 'EDI': 725, 'MXP': 1040, 'MEX': 670, 'SFO': 424, 'LAX': 330, 'OGG': 904, 'SYD': 1312, 'DXB': 875, 'LAS': 535}, 'GIG': {'JFK': 882, 'BCN': 1947, 'HND': 2193, 'TSA': 2275, 'KUL': 1854, 'YUL': 1187, 'BKK': 1544, 'SIN': 1747, 'YXU': 1425, 'PVG': 1798, 'AMS': 1922, 'HKG': 2143, 'YVR': 1175, 'IAD': 1238, 'GMP': 2159, 'ZRH': 1142, 'RUH': 1524, 'CDG': 1877, 'VIE': 1832, 'EDI': 2315, 'MXP': 1862, 'MEX': 610, 'SFO': 1097, 'LAX': 1078, 'OGG': 1826, 'SYD': 1425, 'DXB': 1487, 'LAS': 1242}, 'GMP': {'JFK': 115, 'BCN': 115, 'HND': 140, 'TSA': 105, 'KUL': 120, 'YUL': 1520, 'BKK': 120, 'SIN': 120, 'YXU': 130, 'PVG': 90, 'AMS': 75, 'HKG': 120, 'YVR': 1825, 'IAD': 1415, 'GIG': 2159, 'ZRH': 1445, 'RUH': 80, 'CDG': 120, 'VIE': 100, 'EDI': 1310, 'MXP': 220, 'MEX': 2080, 'SFO': 1535, 'LAX': 845, 'OGG': 1775, 'SYD': 1585, 'DXB': 130, 'LAS': 1509}, 'ZRH': {'JFK': 660, 'BCN': 105, 'HND': 1440, 'TSA': 1020, 'KUL': 1210, 'YUL': 1005, 'BKK': 845, 'SIN': 1420, 'YXU': 1483, 'PVG': 885, 'AMS': 220, 'HKG': 850, 'YVR': 770, 'IAD': 670, 'GIG': 1142, 'GMP': 1445, 'RUH': 865, 'CDG': 80, 'VIE': 250, 'EDI': 275, 'MXP': 55, 'MEX': 1351, 'SFO': 1065, 'LAX': 1510, 'OGG': 1488, 'SYD': 1695, 'DXB': 640, 'LAS': 905}, 'RUH': {'JFK': 80, 'BCN': 160, 'HND': 245, 'TSA': 80, 'KUL': 80, 'YUL': 1490, 'BKK': 80, 'SIN': 80, 'YXU': 410, 'PVG': 80, 'AMS': 160, 'HKG': 80, 'YVR': 1655, 'IAD': 1045, 'GIG': 1524, 'GMP': 80, 'ZRH': 865, 'CDG': 80, 'VIE': 160, 'EDI': 600, 'MXP': 160, 'MEX': 1260, 'SFO': 1180, 'LAX': 635, 'OGG': 2225, 'SYD': 2240, 'DXB': 70, 'LAS': 1705}, 'CDG': {'JFK': 435, 'BCN': 115, 'HND': 675, 'TSA': 120, 'KUL': 465, 'YUL': 420, 'BKK': 175, 'SIN': 60, 'YXU': 55, 'PVG': 580, 'AMS': 60, 'HKG': 605, 'YVR': 1080, 'IAD': 620, 'GIG': 1877, 'GMP': 120, 'ZRH': 80, 'RUH': 80, 'VIE': 90, 'EDI': 110, 'MXP': 85, 'MEX': 635, 'SFO': 1160, 'LAX': 770, 'OGG': 1375, 'SYD': 1860, 'DXB': 290, 'LAS': 945}, 'VIE': {'JFK': 90, 'BCN': 140, 'HND': 340, 'TSA': 150, 'KUL': 100, 'YUL': 775, 'BKK': 155, 'SIN': 100, 'YXU': 135, 'PVG': 155, 'AMS': 90, 'HKG': 340, 'YVR': 1335, 'IAD': 955, 'GIG': 1832, 'GMP': 100, 'ZRH': 250, 'RUH': 160, 'CDG': 90, 'SYD': 1825, 'EDI': 330, 'MXP': 90, 'MEX': 900, 'SFO': 1090, 'LAX': 770, 'OGG': 1420, 'DXB': 120, 'LAS': 885}, 'EDI': {'JFK': 820, 'BCN': 910, 'HND': 1450, 'TSA': 1195, 'KUL': 960, 'YUL': 690, 'BKK': 1085, 'SIN': 1040, 'YXU': 699, 'PVG': 935, 'AMS': 745, 'HKG': 1090, 'YVR': 1750, 'IAD': 725, 'GIG': 2315, 'GMP': 1310, 'ZRH': 275, 'RUH': 600, 'CDG': 110, 'VIE': 330, 'SYD': 1565, 'MXP': 280, 'MEX': 1146, 'SFO': 1172, 'LAX': 855, 'OGG': 1442, 'DXB': 640, 'LAS': 1249}, 'MXP': {'JFK': 165, 'BCN': 85, 'HND': 675, 'TSA': 95, 'KUL': 305, 'YUL': 1035, 'BKK': 180, 'SIN': 165, 'YXU': 530, 'PVG': 580, 'AMS': 60, 'HKG': 90, 'YVR': 1020, 'IAD': 1040, 'GIG': 1862, 'GMP': 220, 'ZRH': 55, 'RUH': 160, 'CDG': 85, 'VIE': 90, 'EDI': 280, 'MEX': 1535, 'SFO': 1025, 'LAX': 770, 'OGG': 1510, 'SYD': 1880, 'DXB': 160, 'LAS': 910}, 'MEX': {'JFK': 479, 'BCN': 1015, 'HND': 1515, 'TSA': 1500, 'KUL': 2827, 'YUL': 518, 'BKK': 1527, 'SIN': 1680, 'YXU': 408, 'PVG': 1517, 'AMS': 635, 'HKG': 1802, 'YVR': 620, 'IAD': 670, 'GIG': 610, 'GMP': 2080, 'ZRH': 1351, 'RUH': 1260, 'CDG': 635, 'VIE': 900, 'EDI': 1146, 'MXP': 1535, 'SFO': 370, 'LAX': 245, 'OGG': 751, 'SYD': 1160, 'DXB': 1380, 'LAS': 221}, 'SFO': {'JFK': 317, 'BCN': 1190, 'HND': 1835, 'TSA': 1550, 'KUL': 1295, 'YUL': 479, 'BKK': 1255, 'SIN': 1160, 'YXU': 533, 'PVG': 1165, 'AMS': 1135, 'HKG': 965, 'YVR': 141, 'IAD': 424, 'GIG': 1097, 'GMP': 1535, 'ZRH': 1065, 'RUH': 1180, 'CDG': 1160, 'VIE': 1090, 'EDI': 1172, 'MXP': 1025, 'MEX': 370, 'LAX': 75, 'OGG': 615, 'SYD': 1245, 'DXB': 1265, 'LAS': 90}, 'LAX': {'JFK': 315, 'BCN': 640, 'HND': 835, 'TSA': 700, 'KUL': 825, 'YUL': 466, 'BKK': 84, 'SIN': 825, 'YXU': 180, 'PVG': 760, 'AMS': 640, 'HKG': 825, 'YVR': 165, 'IAD': 330, 'GIG': 1078, 'GMP': 845, 'ZRH': 1510, 'RUH': 635, 'CDG': 770, 'VIE': 770, 'EDI': 855, 'MXP': 770, 'MEX': 245, 'SFO': 75, 'OGG': 759, 'SYD': 1125, 'DXB': 270, 'LAS': 70}, 'OGG': {'JFK': 728, 'BCN': 1289, 'HND': 659, 'TSA': 2791, 'KUL': 1964, 'YUL': 1003, 'BKK': 1814, 'SIN': 1826, 'YXU': 839, 'PVG': 1134, 'AMS': 1300, 'HKG': 1034, 'YVR': 366, 'IAD': 904, 'GIG': 1826, 'GMP': 1775, 'ZRH': 1488, 'RUH': 2225, 'CDG': 1375, 'VIE': 1420, 'EDI': 1442, 'MXP': 1510, 'MEX': 751, 'SFO': 615, 'LAX': 759, 'SYD': 777, 'DXB': 2125, 'LAS': 650}, 'SYD': {'JFK': 1238, 'BCN': 2120, 'HND': 1090, 'TSA': 1905, 'KUL': 530, 'YUL': 2075, 'BKK': 535, 'SIN': 720, 'YXU': 1523, 'PVG': 970, 'AMS': 1495, 'HKG': 845, 'YVR': 1405, 'IAD': 1312, 'GIG': 1425, 'GMP': 1585, 'ZRH': 1695, 'RUH': 2240, 'CDG': 1860, 'VIE': 1825, 'EDI': 1565, 'MXP': 1880, 'MEX': 1160, 'SFO': 1245, 'LAX': 1125, 'OGG': 777, 'DXB': 1010, 'LAS': 1310}, 'DXB': {'JFK': 75, 'BCN': 200, 'HND': 675, 'TSA': 150, 'KUL': 215, 'YUL': 1080, 'BKK': 190, 'SIN': 240, 'YXU': 956, 'PVG': 435, 'AMS': 170, 'HKG': 140, 'YVR': 1400, 'IAD': 875, 'GIG': 1487, 'GMP': 130, 'ZRH': 640, 'RUH': 70, 'CDG': 290, 'VIE': 120, 'EDI': 640, 'MXP': 160, 'SFO': 1265, 'LAX': 270, 'OGG': 2125, 'SYD': 1010, 'MEX': 1380, 'LAS': 1315}, 'LAS': {'JFK': 290, 'BCN': 870, 'HND': 2210, 'TSA': 1705, 'KUL': 1620, 'YUL': 425, 'BKK': 1681, 'SIN': 1466, 'YXU': 910, 'PVG': 1523, 'AMS': 965, 'HKG': 1310, 'YVR': 155, 'IAD': 535, 'GIG': 1242, 'GMP': 1509, 'ZRH': 905, 'RUH': 1705, 'CDG': 945, 'VIE': 885, 'EDI': 1249, 'MXP': 910, 'MEX': 221, 'SFO': 90, 'LAX': 70, 'OGG': 650, 'SYD': 1310, 'DXB': 1315}}
    # print len(cities_dict)
    #Find the flight duration from origin to each city in the list using kevin's call
    closest_city_name = ''
    closest_city_dist = float('inf')
    for city in cities_dict.keys():
        # d = get_flight_duration(origin, city)
        d = random.choice(range(10,100))
        # print city, d
        if d < closest_city_dist:
            closest_city_dist = d
            closest_city_name = city

    #Sort based on flight durations
    #Create a list of tuples [(city1, flight_duration)....]
    path = [origin, closest_city_name]
    visited = set()
    visited.add(origin)
    for i in cities_dict:
        #Find the closest city to this one
        closest_cities = sorted([(value, key) for (key,value) in cities_dict[closest_city_name].items()])
        flag = False
        # print closest_cities
        for c in closest_cities:
            if c[1] not in visited:
                closest_city_name = c[1]
                visited.add(closest_city_name)
                flag = True
                break
        # print visited
        if flag:
            path.append(closest_city_name)
    path.append(origin) #Close the loop
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


out =  path_finder('JFK')
print out, len(out)


