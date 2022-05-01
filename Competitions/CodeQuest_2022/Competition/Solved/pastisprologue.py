from collections import defaultdict


cases = int(input())
for i in range(cases):
    events = int(input())

    events_list = {}
    for j in range(events):
        cur = input().split(',') # 2, 3, 4
        if cur[4] == 'false':
            continue
        if cur[3] not in events_list:
            events_list[cur[3]] = {'Day': 0, 'Night': 0}
        cur_event = events_list[cur[3]]
        if cur[2] == 'Day':
            cur_event['Day'] += 1
        else:
            cur_event = events_list[cur[3]]
            cur_event['Night'] += 1

    res = []
    for key, value in events_list.items():
        cur = [key, str(value['Day']), str(value['Night'])]
        cur = ','.join(cur)
        res.append(cur)
    for r in sorted(res):
        print(r)