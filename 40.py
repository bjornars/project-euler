def get_nth(num):
    limit = 10
    offset1 = 0
    offset2 = 0
    tens = 1

    while 1:
        if num < limit:
            num1 = num - offset1
            num2 = num1 / tens
            return int(str(offset2 + num2)[num1 % tens])

        offset1 = limit
        offset2 = 10 ** tens
        limit += (9 * 10**tens) * (tens+1)
        tens += 1

s = 1
for x in range(0, 7):
    s *= get_nth(10**x)

print s
