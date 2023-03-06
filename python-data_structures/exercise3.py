#!/usr/bin/python3

#Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 7, 45, 89]
print('Initial list ', sample_list)

length_size = len(sample_list)
chunk_size = length_size / 3


print(length_size)
sample_list.reverse()

print('After reversing ', sample_list)




