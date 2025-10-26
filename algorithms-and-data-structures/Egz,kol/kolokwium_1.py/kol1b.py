from kol1testy import runtests

def merge(A, Left, Mid, Right, ans):
    Left_A = A[Left:Mid + 1]
    Right_A = A[Mid + 1:Right + 1]
    Left_index = Right_index = 0
    Main_index = Left

    while Left_index < len(Left_A) and Right_index < len(Right_A):
        if Left_A[Left_index][0] < Right_A[Right_index][0]:
            A[Main_index] = Left_A[Left_index]
            Left_index += 1
        else:
            A[Main_index] = Right_A[Right_index]
            ans[Right_A[Right_index][1]] += Left_index
            #bo tyle było mniejszych w lewej połówce wcześniej
            Right_index += 1
        Main_index += 1

    while Left_index < len(Left_A):
        A[Main_index] = Left_A[Left_index]
        Left_index += 1
        Main_index += 1

    while Right_index < len(Right_A):
        A[Main_index] = Right_A[Right_index]
        ans[Right_A[Right_index][1]] += Left_index
        Right_index += 1
        Main_index += 1

def MergeSort(A, Left, Right, ans):
    if Left < Right:
        Mid = (Right + Left) // 2
        MergeSort(A, Left, Mid, ans)  # lewa
        MergeSort(A, Mid + 1, Right, ans)  # prawa
        merge(A, Left, Mid, Right, ans)

def maxrank(T):
    ans = [0 for _ in range(len(T))]
    tmp = [(T[i], i) for i in range(len(T))]
    MergeSort(tmp, 0, len(T) - 1, ans)
    return max(ans)

runtests(maxrank, all_tests=True)