def shipWithinDays(weights, D):

    def canShip(capacity):

        days = 1
        current = 0

        for weight in weights:

            if current + weight <= capacity:

                # Put package on current day
                current += weight

            else:

                # Package doesn't fit,
                # so start a new day
                days += 1
                current = weight

        return days <= D

    low = max(weights)
    high = sum(weights)

    while low <= high:

        mid = (low + high) // 2

        if canShip(mid):

            # This capacity works.
            # Try smaller capacity.
            high = mid - 1

        else:

            # Not enough capacity.
            # Need larger capacity.
            low = mid + 1

    return low