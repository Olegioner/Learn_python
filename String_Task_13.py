message = input()
for i in range(len(message)):
    if message[i] == '[':
        cur_letter = chr(int(message[i+3:i+7]))
        print(cur_letter, end='')


    print(message[i],end='')
