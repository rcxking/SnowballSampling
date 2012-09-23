'''
Created on Sep 19, 2012
Access the LiveJournal API
@author: bryant
'''

'''
This is a Python Wrapper for the LiveJournal Online API
'''

# Import the built-in urllib library to access online URL's
import urllib 

'''
Arguments:
g is a Graph Data Structure (may be filled or empty)
name is a string of the user to query for
'''

def read_lj_friends(g, name):
	# The LJ API returns a JSON string with the user's data.  Store this
    # into the variable "response"
    response = urllib.urlopen('http://www.livejournal.com/misc/fdata.bml?user='+name)
    
	# We need to parse the JSON string to extract data
    for line in response.readlines():
        if line.startswith('#'): continue
        
        parts = line.split()
        if len(parts) == 0: continue
        
        if parts[0] == '<':
            g.add_edge(parts[1], name)
        else:
            g.add_edge(name, parts[1])
