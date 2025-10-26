from heapq import heappop, heappush

def make_tab_of_events(A):
    tab = []
    for i in range(len(A)):
        tab.append((A[i][0], 1, A[i][1]))
        tab.append((A[i][1], -1, None))
    return tab


def kintersect(A, k):
    tab = make_tab_of_events(A)
    tab.sort(key=lambda x: x[0])
    res_list = []
    heap = []
    cnt = 0
    maxi = -1
    start_res = -1
    end_res = -1
    for i in range(len(tab)):
        if tab[i][1] == 1:
            cnt += 1
            heappush(heap, tab[i][2])
            start = tab[i][0]
        if cnt >= k:
            end = heappop(heap)
            if end - start > maxi:
                maxi = end - start
                start_res = start
                end_res = end
            cnt -= 1
    for i in range(len(A)):
        if start_res >= A[i][0] and end_res <= A[i][1]:
            res_list.append(i)
    return res_list