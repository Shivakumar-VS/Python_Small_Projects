def rem(l, word):
    n = []
    for item in l:
        if word in item:
            n.append(item.replace(word, ''))
        else:
            n.append(item)
    return n

l = ['chandana','navya' ,'divya', 'Th']
print(rem(l, 'Th'))
