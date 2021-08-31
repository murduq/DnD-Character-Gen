import random

def randomize(st, dex, cnst, intel, wis, chrs):
    st = random.randint(8, 15)
    dex = random.randint(8, 15)
    cnst = random.randint(8, 15)
    intel = random.randint(8, 15)
    wis = random.randint(8, 15)
    chrs = random.randint(8, 15)
    return [st, dex, cnst, intel, wis, chrs]

def randomize_extreme(st, dex, cnst, intel, wis, chrs):
    st = random.randint(1, 30)
    dex = random.randint(1, 30)
    cnst = random.randint(1, 30)
    intel = random.randint(1, 30)
    wis = random.randint(1, 30)
    chrs = random.randint(1, 30)
    return [st, dex, cnst, intel, wis, chrs]



who = open('who.txt', 'r')
races = who.readline().split()
classes = who.readline().split()
st = dex = cnst = intel = wis = chrs = tot = tries = 0
race = random.choice(races)
_class = random.choice(classes)
print (classes)

stats = randomize(st, dex, cnst, intel, wis, chrs)
while tot < 70 or tot > 74:
    tries += 1
    stats = randomize(st, dex, cnst, intel, wis, chrs)
    tot = sum(stats)
print('\n I made a ' + race + ' ' + _class + '!')
print("""\n STR: %d \n DEX: %d\n CON: %d\n INT: %d\n WIS: %d\n CHA: %d\n Stat total: %d"""
      % (stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], tot))
print("This took me " + str(tries) + " tries")
