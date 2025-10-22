def average_rating(file,candidate):
    with open(file, 'r', encoding="utf-8") as r_file:
        r_list = []
        zero = [0, 0]
        j = 0
        av = 0
        for line in r_file:
            a = line.split()
            if candidate == a[1]:
                j+=1
                av+=int(a[2])
        if j == 0:
            return zero
        r_list.append(j)
        r_list.append(av/j)
        return r_list

def print_ratings(file):
    ratings = {}
    with open(file, 'r', encoding="utf-8") as r_file:
        for line in r_file:
            a = line.split()
            c = a[1]
            r = int(a[2])
            if c not in ratings:
                ratings[c] = {'total': 0, 'count': 0}
            ratings[c]['total'] += r
            ratings[c]['count'] += 1
    for c, d in ratings.items():
        av = d['total']/d['count']
        print(f"{c}: {av}")



print_ratings('rating.txt')
