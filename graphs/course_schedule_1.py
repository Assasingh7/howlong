from collections import deque

def canFinish(numCourses, prerequisites):

    # Build adjacency list
    adj = [[] for _ in range(numCourses)]

    # indegree[i] = number of prerequisites of course i
    indegree = [0] * numCourses

    for course, prerequisite in prerequisites:

        # prerequisite → course
        adj[prerequisite].append(course)

        # course has one more prerequisite
        indegree[course] += 1

    # Courses having no prerequisites
    q = deque()

    for course in range(numCourses):
        if indegree[course] == 0:
            q.append(course)

    processed = 0

    # Kahn's BFS
    while q:

        course = q.popleft()

        # We successfully completed this course
        processed += 1

        # Remove this course as a prerequisite
        for nextCourse in adj[course]:

            indegree[nextCourse] -= 1

            # All prerequisites are now completed
            if indegree[nextCourse] == 0:
                q.append(nextCourse)


    return processed == numCourses

from collections import deque

def findOrder(numCourses, prerequisites):

    # Build graph
    adj = [[] for _ in range(numCourses)]

    # Calculate indegree
    indegree = [0] * numCourses

    for course, prerequisite in prerequisites:

        # prerequisite → course
        adj[prerequisite].append(course)

        indegree[course] += 1

    # Start with courses having no prerequisites
    q = deque()

    for course in range(numCourses):
        if indegree[course] == 0:
            q.append(course)

    result = []

    while q:

        course = q.popleft()

        # Add course to our valid order
        result.append(course)

        # Remove this course as a prerequisite
        for nextCourse in adj[course]:

            indegree[nextCourse] -= 1

            # All prerequisites completed
            if indegree[nextCourse] == 0:
                q.append(nextCourse)

    # If we couldn't include every course,
    # there is a cycle
    if len(result) != numCourses:
        return []

    return result