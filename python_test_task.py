s  = input()
pos1 = 0
pos2 = 0
length = 0
word = str

counter = s.count(' ')
print(counter)
if (counter == 0):
    print('Cамое длинное слово в строке: ' + s)
else:
    for i in range(counter + 1):
        pos2 = s.find(' ', pos1)
        print(str(i), ', ', str(pos2))
        if (pos2 == -1):
            if (length < (len(s) - pos1)):
                word = s[pos1:pos2]
                break
        if (length < (pos2 - pos1)):
            length = pos2 - pos1
            word = s[pos1:pos2]
            pos1 = pos2 + 1
        else:
            pos1 = pos2 + 1
    print('Самое длинное слово в строке: ' + word)