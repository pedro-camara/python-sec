import random
import string

lenght = 16
chars = string.ascii_letters + string.digits + '!@#$%^&*()'

rnd = random.SystemRandom()

print (''.join(rnd.choice(chars) for i in range(lenght)))
