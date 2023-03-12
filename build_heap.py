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
    
    input_type = input()

    if "F" in input_type:
        filename = input()
        if ".a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().strip().split()))
    elif "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))
        height = compute_height(n, parents)
    else:
        return()    


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
