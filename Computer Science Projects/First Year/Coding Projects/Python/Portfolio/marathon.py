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

def main():
    results = read_file('marathon.txt')
    option = ''
    while option != 'Q':
        menu()
        option = input('Select option: ')
        if option == 'S':
            display_competitor(results)
        elif option == 'I':
            display_nbr_in_interval(results)

def display_competitor(results):
    id_no = input('Enter competitor ID:')
    found = False
    for competitor in results:
        if competitor['id'] == id_no:
            display_competitor_info(competitor)
            found = True
    if not found:
        print('Competitor not found')
    
def display_competitor_info(competitor):
    print('ID :',competitor['id'])
    print('First Name :', competitor['firstname'])
    print('First Name :', competitor['lastname'])

def display_nbr_in_interval(results):
    start_time = input('Enter start time of interval (hh:mm:ss): ')
    start_secs = get_secs(start_time)
    end_time = input('Enter end time of interval (hh:mm:ss): ')
    end_secs = get_secs(end_time)
    interval_data = get_interval_data(start_secs, end_secs, results)
    print('Number of competitors finishing in this interval = ', interval_data['count'])
    if interval_data['count'] != 0:
        secs = interval_data['mean']
        mins = secs//60
        secs = secs%60
        hours = mins//60
        mins = mins%60
        print('Mean time in interval is ',int(hours),'hours',int(mins),'minutes','and ',int(secs),'seconds')
    else:
        print('No competitors in interval')

def get_secs(time):
    time_split = time.split(':')
    seconds = int(time_split[2]) + 60*int(time_split[1]) + 60*60*int(time_split[0])
    return seconds
                      
def menu():
    print('Options are:')
    print('S - Show data for a competitor')
    print('I - Show statistics for competitors finishing in a given interval')
    print('Q - Quit the program')

if __name__ == "__main__":
    main()
