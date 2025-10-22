loj = {'0': 'no', '1': 'pa', '2': 're', '3': 'ci', '4': 'vo', '5': 'mu',
       '6': 'xa', '7': 'ze', '8': 'bi', '9': 'so'
       }
num = (input("Enter number: "))
num = num.lstrip('0')
if not num:
    print('no')
else:
    lojbnum = (loj[number] for number in num)
    print(''.join(lojbnum))
