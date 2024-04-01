json_snow = ["json" , 1 , 2.0]

print(json_snow[0])
print(json_snow)
print(len(json_snow))


#Range 
num_seq = range(0,10)
num_list = list(num_seq)

print(num_seq)
print(num_list)


#sequential Indexing
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners[1])
print(world_cup_winners[1][1])  # Accessing 'Spain'
print(world_cup_winners[1][1][0])  # Accessing 'S'

# Merge List

merged_list = json_snow + num_list

print(merged_list)