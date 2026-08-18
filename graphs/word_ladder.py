from collections import deque
def main(wordList, start, target):
    q = deque((start, 1))
    word_set = set(wordList)
    if start in word_set:
        word_set.remove(start)
    while q:
        word, steps = q.popleft()
        if word == target:
            return steps
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i]+ch+word[i+1:]
                if new_word in word_set:
                    q.append((new_word, steps+1))
                    word_set.remove(new_word)
    return 0