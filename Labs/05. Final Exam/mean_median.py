def find_mean(n):
    total = num = 0

    while num != len(n):
        total = n[num] + total
        num += 1
    return(total/len(n))


def find_median(n):
    nums = sorted(n)
    
    mid = int(len(n)/2)
    return(nums[mid])


def main():
    values = [4, 18, 12, 9, 2, 17, 24]

    print(f"Mean: {find_mean(values)}")
    print(f"Median: {find_median(values)}")
    

if __name__ == '__main__':
    main()
