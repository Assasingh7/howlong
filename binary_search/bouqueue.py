def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    low = min(bloomDay)
    high = max(bloomDay)

    def canMake(day):

        bouquets = 0
        consecutive = 0

        for flower in bloomDay:

            if flower <= day:
                consecutive += 1

                if consecutive == k:
                    bouquets += 1
                    consecutive = 0

            else:
                consecutive = 0

        return bouquets >= m

    while low <= high:

        mid = (low + high) // 2

        if canMake(mid):
            high = mid - 1

        else:
            low = mid + 1

    return low