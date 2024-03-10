def online_count(statuses) :
    online = 0
    n = len(statuses)
    d = list(statuses.values())
    for i in range(len(d)) :
        print(d[i])
        if d[i] == 'online' :
            online += 1
    return online
    