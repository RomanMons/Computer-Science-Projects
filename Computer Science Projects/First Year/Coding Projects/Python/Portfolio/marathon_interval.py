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

def get_secs(time):
    time_split = time.split(':')
    seconds = int(time_split[2]) + 60*int(time_split[1]) + 60*60*int(time_split[0])
    return seconds

def get_interval_data(start_secs, end_secs, results):
    count = 0
    mean = 0
    for racer in results:
        time = racer['time']
        time_secs = get_secs(time)
        if start_secs <= time_secs <= end_secs:
            count+=1
            mean+=time_secs
        int_mean = mean/count if count > 0 else 0
        interval = {'count': count, 'mean': int_mean}
    return interval
