def painter_partition(books, K):
    left = max(books)           # Min: largest book
    right = sum(books)          # Max: all books
    
    while left < right:
        mid = (left + right) // 2
        
        if can_allocate(books, K, mid):
            right = mid         # Try smaller
        else:
            left = mid + 1      # Try bigger
    
    return left


def can_allocate(books, K, max_pages):
    painters = 1
    current = 0
    
    for pages in books:
        if current + pages <= max_pages:
            current += pages    # Add to current
        else:
            painters += 1       # New painter
            current = pages
            if painters > K:
                return False
    
    return True