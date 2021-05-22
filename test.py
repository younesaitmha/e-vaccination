import random, string

print(''.join(random.choice(string.ascii_letters) for _ in range(22)))
