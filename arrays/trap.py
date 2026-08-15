def main(arr):
    left_max= 0
    right_max= 0
    tot_water = 0
    left = 0
    right = len(arr)-1
    while left<=right:
        if arr[left]<=arr[right]:
            if left_max<=arr[left]:
                left_max = arr[left]
            else:
                tot_water+=left_max-arr[left]
            left+=1
        else:
            if right_max<=arr[right]:
                right_max = arr[right]
            else:
                tot_water+=right_max-arr[right]
            right-=1
    return tot_water