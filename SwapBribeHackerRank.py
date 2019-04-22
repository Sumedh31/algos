testcases = int(input())

for cases in range(testcases):
    NoOFInput = int(input())
    DetailsOfQueue = list(map(int, input().split()))
	swaps = [0] * NoOFInput

    swapped = True

    while swapped:
        swapped = False

        for i in range(NoOFInput):
            while i < NoOFInput-1 and DetailsOfQueue[i] > DetailsOfQueue[i + 1]:
                swaps[DetailsOfQueue[i] - 1] += 1
                DetailsOfQueue[i], DetailsOfQueue[i + 1] = DetailsOfQueue[i + 1], DetailsOfQueue[i]
                swapped = True
                i += 1
    s = 0
	
    for swap in swaps:
        s += swap

        if swap > 2:
            print('Too chaotic')
            break
    else:
        print(s)