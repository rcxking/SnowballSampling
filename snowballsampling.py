'''
Created on Sep 21, 2012

Implementation for Snowball Sampling

@author: bryant
'''

# Import the wrapper functions for the livejournal api
import livejournal as lj

''' 
Snowball sampling works by performing the following steps:
1) Give a Graph Data Structure (can be either empty or filled) g, and the next
   person to look up (center).
2) The max_depth variable tells how many friends-of-friends to look for.  For
   example, a max_depth of 1 (default) indicates that we should only look
   for immediate friends.
3) The current_depth, which starts at 0, is a counter to ensure that we do not
   mine too far down.  The greater the max_depth, the more memory and time it
   will take to mine for data.
4) Repeat while the current_depth has not reached the max_depth:
   A) If the current person that we are looking at has not been visited before,
      add the person (center) to the taboo_list (list data structure).  The 
      taboo_list keeps track of all people that we have visited.  Call the
      LJ API and ask for a list of ALL the friends of the current person.  For
      every friend to the current person, recursively call snowball_sampling
      using this person's social network and friends list.
   B) If the person has already been visited, or the max_depth has been reached,
      return and exit out of this recursive level.
5) Return a graph data structure containing all friends and their relationships
 to each other.  
   
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
    
