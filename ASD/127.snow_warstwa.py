
def snow(T,I):
    events = []
    for a,b in I:
        events.append((a,1)) #1 bo + 1
        events.append((b+1,-1)) #-1 bo -1
    events.sort()
    max_snow = 0
    curr_snow = 0
    for _,change in events:
        curr_snow += change
        max_snow = max(max_snow,curr_snow)
    return max_snow