import nodeentry as ne
import rom
from math import *

author = {'name':'Abhipray Sahoo'}

#############################################################################
# The generator function findpath
#############################################################################

def findpath(start, end, predecessors):
    while end != start:
        yield (predecessors[end], end)
        end = predecessors[end]
    return


#############################################################################
# The function astar_search
#############################################################################

def astar_search(start, end, network, dist_estimator, more_visited):
    frontier = ne.DistNodeEntryPQ()
    frontier.insert(ne.DistNodeEntry(start, None, 0, dist_estimator(start, end)))
    visited = ne.NodeEntryList()
    while len(frontier)>0:
        current=frontier.remove()
        visited.insert(current)
        yield current
        n=current.get_node()
        if n == end:
            return
        for nbr in network[n].keys():
            if not visited.has_node(nbr) and nbr not in more_visited:
                g = current.get_g()+network[n][nbr]
                h = dist_estimator(nbr,end)
                frontier.insert(ne.DistNodeEntry(nbr,n,g,h+g))


