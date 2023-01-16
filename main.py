import gzip

import networkx as nx

#readfile
f=gzip.open('facebook_combined.txt.gz','rb')
file_content=f.read()
file_content = file_content.decode('utf-8')
b = file_content.split('\n')
b.pop()


#finding the highest node, to figure out the length of the array to be initialized
last_number = int(b[-1].split(" ")[0])
highest_node = last_number
for i in b:

    if int(i.split(" ")[1]) > highest_node:
        highest_node = int(i.split(" ")[1])
print(highest_node)
network = [[] for i in range(highest_node + 1)]
print(network)

for i in b:
    connection = list(map(int,i.split(" ")))
    network[connection[0]].append(connection[1])
    network[connection[1]].append(connection[0])

network_count = [0 for i in range(highest_node + 1)]
for i in range(highest_node + 1):
    network_count[i] = len(network[i])


import statistics

print("Mean of sample is % s " % (statistics.mean(network_count)))
print("Standard Deviation of sample is % s " % (statistics.stdev(network_count)))
print("Max",max(network_count))
print("Min",min(network_count))
network_count_count = [network_count.count(i) for i in range(max(network_count) + 1)]
print(network_count_count)
with open('export.txt','w') as f:
    f.write("\n".join(list(map(str,network_count_count))))

#calculate average using bfs

#find the distance to all other points


#DOES NOT WORK
#TODO
total_spl = [0]
total = 0
for node in range(1,highest_node+1):
    if (node % 10 == 0):
        print(node)

    
    queue = [node]
    distances = [-1] * (highest_node + 1)

    distances[node] = 0
    while queue != []:
        selected = queue.pop(0)
        for child in network[selected]:
            if distances[child] == -1 and child < node:
                queue.append(child)
                distances[child] = distances[selected] + 1
    total_spl.append(sum(filter(lambda x: x>0,distances))*2)
psa_spl = [total_spl[0]]
for i in range(1,len(total_spl)):
    psa_spl.append(psa_spl[i-1] + total_spl[i])
print(psa_spl)
average_spl = [0] + [psa_spl[i] / ((i)*(i+1)) for i in range(1,len(psa_spl))]
print(average_spl)




#export data to txt file
with open('data2.txt', 'w') as f:
    f.write(file_content)