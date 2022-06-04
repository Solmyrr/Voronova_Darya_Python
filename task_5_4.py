num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
idx = 0
if idx <= len(num_list):
    if num_list[idx + 1] > num_list[idx]:
        result.append(num_list[idx])
        idx += 1
print(result)
