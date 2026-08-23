from collections import deque

def alienOrder(words):

    # Create every character as a graph node
    adj = {ch: [] for word in words for ch in word}

    indegree = {ch: 0 for ch in adj}

    # Compare adjacent words
    for i in range(len(words) - 1):

        word1 = words[i]
        word2 = words[i + 1]

        j = 0

        # Find first different character
        while j < len(word1) and j < len(word2):

            if word1[j] != word2[j]:

                u = word1[j]
                v = word2[j]

                # u must come before v
                adj[u].append(v)

                indegree[v] += 1

                break

            j += 1

        # Invalid prefix case
        if j == len(word2) and len(word1) > len(word2):
            return ""

    # Kahn's algorithm
    q = deque()

    for ch in indegree:

        if indegree[ch] == 0:
            q.append(ch)

    result = []

    while q:

        ch = q.popleft()

        result.append(ch)

        for neighbor in adj[ch]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Not all characters could be processed
    # → cycle exists
    if len(result) != len(indegree):
        return ""

    return "".join(result)