def aggressiveCows(stalls, cows):

    stalls.sort()

    def canPlace(distance):

        # Put first cow at first stall
        count = 1
        last = stalls[0]

        # Try placing remaining cows
        for stall in stalls[1:]:

            # Is this stall far enough
            # from the previous cow?
            if stall - last >= distance:

                count += 1
                last = stall

                # Already placed all cows
                if count == cows:
                    return True

        return False

    low = 1
    high = stalls[-1] - stalls[0]

    answer = 0

    while low <= high:

        mid = (low + high) // 2

        if canPlace(mid):

            # This distance works.
            # We want an even larger distance.
            answer = mid
            low = mid + 1

        else:

            # This distance is too large.
            high = mid - 1

    return answer