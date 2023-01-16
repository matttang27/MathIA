import gzip
import math

import matplotlib.pyplot as plt
import networkx as nx

#readfile
f=gzip.open('facebook_combined.txt.gz','rb')
file_content=f.read()
file_content = file_content.decode('utf-8')
b = file_content.split('\n')
b.pop()

G = nx.Graph()
for i in b:
    s = list(map(int,i.split(" ")))
    G.add_edge(s[0],s[1])

s = [i[1] for i in G.degree()]
sizes = [(math.log(i) + 1) * 30 for i in s]

print(G.number_of_nodes())
print(G.number_of_edges())
print(nx.average_clustering(G))
print(nx.average_shortest_path_length(G))
"""
pos = nx.spring_layout(G)

plt.figure(1,figsize=(12,12))
nx.draw_networkx(G,pos=pos,node_size=sizes,with_labels=False)


for node, (x, y) in pos.items():
    plt.text(x, y, node, fontsize=sizes[node]/30, ha='center', va='center')

plt.savefig('network_graph.pdf')
plt.show()
"""
