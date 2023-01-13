import gzip

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

print(network)

network_count = [0 for i in range(highest_node + 1)]
for i in range(highest_node + 1):
    network_count[i] = len(network[i])


import statistics

print("Mean of sample is % s " % (statistics.mean(network_count)))
print("Standard Deviation of sample is % s " % (statistics.stdev(network_count)))

#export data to txt file
with open('data2.txt', 'w') as f:
    f.write(file_content)