def count_words(text):
    return len(text.split())

def count_chars(text):
    counts = {}
    for ch in text:
        ch = ch.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sortit(cc):
    lcc = []
    for key in cc:
        lcc.append({"char": key, "num": cc[key]})
    lcc.sort(reverse=True,key=lambda x:x["num"])
    return lcc
