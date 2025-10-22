import random

i=0
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
bingo = range(11, 75)
while len(b1) != 5:
    r1 = random.choice(bingo)
    str1 = str(r1)
    if str1 in b1:
        continue
    else:
        b1.append(str1)
    i+=1
    if len(b1) == 5:
        print(' '.join(b1))
    while len(b2) != 5:
        r2 = random.choice(bingo)
        str2 = str(r2)
        if str2 in b1:
            continue
        elif str2 in b2:
            continue
        else:
            b2.append(str2)
            i+=1
            if len(b2) == 5:
                print(' '.join(b2))
        while len(b3) != 5:
            r3 = random.choice(bingo)
            str3 = str(r3)
            if str3 in b1:
                continue
            elif str3 in b2:
                continue
            elif str3 in b3:
                continue
            else:
                b3.append(str3)
                i+=1
                if len(b3) == 5:
                    print(' '.join(b3))
            while len(b4) != 5:
                r4 = random.choice(bingo)
                str4 = str(r4)
                if str4 in b1:
                    continue
                elif str4 in b2:
                    continue
                elif str4 in b3:
                    continue
                elif str4 in b4:
                    continue
                else:
                    b4.append(str4)
                    i+=1
                    if len(b4) == 5:
                        print(' '.join(b4))
                while len(b5) != 5:
                    r5 = random.choice(bingo)
                    str5 = str(r5)
                    if str5 in b1:
                        continue
                    elif str5 in b2:
                        continue
                    elif str5 in b3:
                        continue
                    elif str5 in b4:
                        continue
                    elif str5 in b5:
                        continue
                    else:
                        b5.append(str5)
                        i+=1
                        if len(b5) == 5:
                            print(' '.join(b5))
