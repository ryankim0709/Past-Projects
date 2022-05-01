cases = int(input())
for i in range(cases):
    data = input().split()
    num_all = int(data[0])
    num_pass = int(data[1])

    num_all_list = set()
    for j in range(num_all):
        num_all_list.add(input().strip())

    num_pass_list = set()
    for j in range(num_pass):
        num_pass_list.add(input().strip())

    result = num_all_list ^ num_pass_list

    ans = sorted(list(result), key=lambda x: x.lower())
    for r in ans:
        print(r) 