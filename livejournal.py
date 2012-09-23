'''
Created on Sep 19, 2012
Access the LiveJournal API
@author: bryant
'''

import urllib 

def read_lj_friends(g, name):
    response = urllib.urlopen('http://www.livejournal.com/misc/fdata.bml?user='+name)
    
    for line in response.readlines():
        if line.startswith('#'): continue
        
        parts = line.split()
        if len(parts) == 0: continue
        
        if parts[0] == '<':
            g.add_edge(parts[1], name)
        else:
            g.add_edge(name, parts[1])
