'''
Created on Sep 21, 2012

Implementation for Snowball Sampling

@author: bryant
'''

import livejournal as lj

def snowball_sampling(g, center, max_depth = 1, current_depth = 0, taboo_list = []):
    print center, current_depth, max_depth, taboo_list
    
    if current_depth == max_depth:
        print 'out of depth'
        return taboo_list
    if center in taboo_list:
        # Visited this person -- exit
        return taboo_list
    else:
        # New person!  Don't visit again
        taboo_list.append(center)
    
    lj.read_lj_friends(g, center)
    
    for node in g.neighbors(center):
        # Iterate through all friends of the central node, and
        # recursively call snowball sampling
        taboo_list = snowball_sampling(g, node, current_depth = current_depth + 1, 
                                       max_depth = max_depth, taboo_list = taboo_list)
    
    return taboo_list
    