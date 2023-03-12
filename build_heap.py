# python3


def build_heap(data):
    swaps = []
    n = len(data)

    # Build the heap bottom-up by sifting down each parent node
    for i in range((n-1)//2, -1, -1):
        parent = i
        while parent*2+1 < n:
            left_child = parent*2+1
            right_child = parent*2+2 if parent*2+2 < n else left_child
            min_child = left_child if data[left_child] < data[right_child] else right_child
            if data[parent] > data[min_child]:
                swaps.append((parent, min_child))
                data[parent], data[min_child] = data[min_child], data[parent]
                parent = min_child
            else:
                break

    return swaps


def main():
    
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in text:
        text2 = input()
        if "a" in text2:
            return()
        with open ("tests/"+text2, encoding="utf-8") as fails:
            n = int (fails.readline())
            data = list(map(int, fails.readline().split()))
            
    else:
        return()
    
    
    assert len(data) == n

    swaps = build_heap(data)
    
    print(len(swaps))
    
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
