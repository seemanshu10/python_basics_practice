nums_list = [2,88,4,3,6,44,2,88,11,44,2,2,4] 
freq_dict = dict()

for i in range(0, len(nums_list)):
    if nums_list[i] in freq_dict:
        freq_dict[nums_list[i]] += 1
    else:
        freq_dict[nums_list[i]] = 1
print(freq_dict)