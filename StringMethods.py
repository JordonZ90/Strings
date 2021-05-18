box = 'Hello world!'.partition('w')

print(box)

box = 'Hello world!'.partition('o')

print(box)

'''
If the separator string you pass to partition occurs multiple times in the string that partition() calls on.
The method splits the string only on the first occurrence 
'''