def read_file(filename):
    results = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            a = line.split(',')
            num = a[0]
            time = a[1]
            first = a[2]
            last = a[3]
            result = {'id': num, 'time': time, 'firstname': first, 'lastname': last}
            results.append(result)
        return results

test = read_file('marathon.txt')
print(test)
