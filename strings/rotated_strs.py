def main(s, goal):
    if len(s)!=len(goal):
        return False
    double = s+s
    return goal in double

def mainn(s, goal):
    if len(s)!=len(goal):
        return False
    for i in range(len(s)):
        rotated = s[i:]+s[:i]
        if rotated == goal:
            return True
    return False
