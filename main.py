'''
Created on Sep 19, 2012

Snowball Sampling on Livejournal

@author: bryant
'''

'''
Networkx Library implements Graph Data Structures and Graph Algorithms
Matplotlib.pyplot allows the resulting graph to actually be plotted.
The snowball sampling function is located in 'snowballsampling.py'
'''
   
import networkx as net
import matplotlib.pyplot as plot
import snowballsampling as snowball

def main():
    name = raw_input("Who would you like to look up: ")
    depth = int(raw_input("How far do you want to mine? "))
    
    g = net.Graph()
    
    snowball.snowball_sampling(g = g, center = name, max_depth = depth)
    
    # After collecting the data, draw it:
    net.draw(g)
	# This command must be called to actually see the graph
	# WARNING: This command will throw a "MemoryError" if the resulting
	# graph data structure is too large!
    plot.show()
    
    # Uncomment to save the data
    # net.write_pajek(g, 'lj_friends.net')
    
if __name__ == '__main__':
    main()
    
