N = int(input())

for num in range(1, N+1):

    clap = 0
    for n in str(num):
        if n == '3' or n == '6' or n == '9':
            clap += 1

    if clap == 0:
        print(num, end = ' ')
    else:
        print('-' * clap, end = ' ')