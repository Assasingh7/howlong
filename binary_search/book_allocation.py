def findPages(books, students):

    # More students than books is impossible
    if students > len(books):
        return -1

    def canAllocate(limit):

        students_used = 1
        pages = 0

        for book in books:

            # Can current student take this book?
            if pages + book <= limit:

                pages += book

            else:

                # Give book to next student
                students_used += 1
                pages = book

        return students_used <= students

    low = max(books)
    high = sum(books)

    while low <= high:

        mid = (low + high) // 2

        if canAllocate(mid):

            # This limit works.
            # Try to make the maximum even smaller.
            high = mid - 1

        else:

            # This limit is too small.
            # Need a larger limit.
            low = mid + 1

    return low