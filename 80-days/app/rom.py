# import networkx as nx

cities = ['Arad','Zerind','Timisoara','Oradea','Lugoj','Mehadia','Dobreta',
          'Craiova','Pitesti','Rimnicu_Vilcea','Giurgiu','Sibiu','Bucharest',
          'Fagaras','Urziceni','Vaslui','Iasi','Neamt','Hirsova','Eforie']

network = {'Arad':['Sibiu','Timisoara','Zerind'],
         'Timisoara':['Arad','Lugoj'],
         'Zerind':['Arad','Oradea'],
         'Oradea':['Sibiu','Zerind'],
         'Lugoj':['Mehadia','Timisoara'],
         'Mehadia':['Dobreta','Lugoj'],
         'Dobreta':['Craiova','Mehadia',],
         'Craiova':['Dobreta','Pitesti','Rimnicu_Vilcea'],
         'Pitesti':['Bucharest','Craiova','Rimnicu_Vilcea'],
         'Rimnicu_Vilcea':['Craiova','Pitesti','Sibiu'],
         'Sibiu':['Arad','Fagaras','Oradea','Rimnicu_Vilcea'],
         'Fagaras':['Bucharest','Sibiu'],
         'Bucharest':['Fagaras','Giurgiu','Pitesti','Urziceni'],
         'Giurgiu':['Bucharest'],
         'Urziceni':['Bucharest','Hirsova','Vaslui'],
         'Hirsova':['Eforie','Urziceni'],
         'Eforie':['Hirsova'],
         'Vaslui':['Iasi','Urziceni'],
         'Neamt':['Iasi'],
         'Iasi':['Neamt','Vaslui']}

intercity_distances = {('Arad','Zerind'):75,('Zerind','Arad'):75,
                       ('Arad','Timisoara'):118,('Timisoara','Arad'): 118,
                       ('Arad','Sibiu'):140, ('Sibiu','Arad'): 140,
                       ('Zerind','Oradea'): 71, ('Oradea','Zerind'): 71,
                       ('Oradea','Sibiu'):151,('Sibiu','Oradea'): 151,
                       ('Timisoara','Lugoj'): 111, ('Lugoj','Timisoara'): 111,
                       ('Lugoj','Mehadia'):70,('Mehadia','Lugoj'): 70,
                       ('Mehadia','Dobreta'): 75, ('Dobreta','Mehadia'): 75,
                       ('Dobreta','Craiova'): 120, ('Craiova','Dobreta'): 120,
                       ('Craiova','Rimnicu_Vilcea'):146,('Rimnicu_Vilcea','Craiova'): 146,
                       ('Rimnicu_Vilcea','Sibiu'): 80, ('Sibiu','Rimnicu_Vilcea'): 80,
                       ('Craiova','Pitesti'): 138, ('Pitesti','Craiova'): 138,
                       ('Pitesti','Rimnicu_Vilcea'):97,('Rimnicu_Vilcea','Pitesti'):97,
                       ('Pitesti','Bucharest'):101,('Bucharest','Pitesti'): 101,
                       ('Sibiu','Fagaras'):99,('Fagaras','Sibiu'):99,
                       ('Fagaras','Bucharest'):211,('Bucharest','Fagaras'):211,
                       ('Bucharest','Giurgiu'): 90, ('Giurgiu','Bucharest'):90,
                       ('Bucharest','Urziceni'):85,('Urziceni','Bucharest'):85,
                       ('Urziceni','Hirsova'): 98, ('Hirsova','Urziceni'):98,
                       ('Hirsova','Eforie'):86, ('Eforie','Hirsova'): 86,
                       ('Urziceni','Vaslui'):142,('Vaslui','Urziceni'):142,
                       ('Vaslui','Iasi'): 92, ('Iasi','Vaslui'): 92,
                       ('Iasi','Neamt'): 87, ('Neamt','Iasi'): 87}

heuristic_Bucharest = {'Arad':366,'Zerind':374,'Timisoara':329,'Oradea':380,'Lugoj':244,
                       'Mehadia':241,'Dobreta':242,'Craiova':160,'Pitesti':100,
                       'Rimnicu_Vilcea':193,'Giurgiu':77,'Sibiu':253,'Bucharest':0,
                       'Fagaras':176,'Urziceni':80,'Vaslui':199,'Iasi':226,'Neamt':234,
                       'Hirsova':151,'Eforie':161}

"""
def make_romania_graph():
  G = nx.Graph(name = "Romania")
  for city in cities:
    G.add_node(city)
    for nbr in network[city]:
       G.add_edge(city, nbr, distance = intercity_distances[(nbr, city)])
  return G
"""