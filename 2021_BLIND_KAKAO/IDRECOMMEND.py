def solution(new_id):
    new_id = new_id.lower()
    special_char = ['~', '`', '!', '@', '#', '$', '%',' ^', '&', '*', '(', ')', '+', '=', ':', ';', '<', '>', ',', '/', '?', '[', ']', '{', '}', ',', '^', "'", '"', '|']
    for c in special_char:
        if c in new_id:
            new_id = new_id.replace(c, '')

    idx = 0
    while idx < len(new_id)-1:
        if new_id[idx] == '.' and new_id[idx+1] == '.':
            new_id = new_id[:idx] + new_id[idx+1:]
            idx = 0
        else: idx += 1

    if len(new_id) > 0:
        if new_id[0] == '.':
            if len(new_id) == 1:
                new_id = ''
            else:
                new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[len(new_id)-1] == '.':
            if len(new_id) == 1:
                new_id = ''
            else:
                new_id = new_id[:-1]
    if new_id == '':
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    return answer