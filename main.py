'''
Created on Sep 19, 2012

Snowball Sampling on Livejournal

@author: bryant
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
    # net.draw(g)
    # plot.show()
    
    # Save the data
    net.write_pajek(g, 'lj_friends.net')
    
if __name__ == '__main__':
    main()
    
