def binpack(items, S):
    maxSize = S
    revSorted_items = sorted(items, reverse=True)
    
    bins = []
    remaining_space = []
    
    for item in revSorted_items:
        # Find first bin that can fit item
        placed = False
        for i in range(len(bins)):
            if remaining_space[i] >= item:
                bins[i].append(item)
                remaining_space[i] = remaining_space[i] - item
                placed = True
                break
        
        # If no bin has space, create one
        if not placed:
            bins.append([item])
            remaining_space.append(maxSize - item)
    
    return bins, remaining_space


if __name__ == "__main__":
    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins, remaining_space = binpack(items, B)

    print(f"Max bin size is {B}\n")
    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]} (remaining space: {remaining_space[i]})")
