
WORDS = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
QUERIES = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        wild_idxs = []
        for i, c in enumerate(query):
            if c == '?': wild_idxs.append(i)
        for word in words:
            if len(query) != len(word): continue
            for idx in wild_idxs:
                word = word[:idx] + '?' + word[idx+1:]
            if word == query:
                cnt += 1
        answer.append(cnt)
    return answer
