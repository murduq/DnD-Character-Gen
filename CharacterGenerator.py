import random

def randomize(st, dex, cnst, intel, wis, chrs):
    st = random.randint(1,10)
    dex = random.randint(1,10)
    cnst = random.randint(1,10)
    intel = random.randint(1,10)
    wis = random.randint(1,10)
    chrs = random.randint(1,10)
    return [st,dex,cnst,intel,wis,chrs]

st=0
dex=0
cnst=0
intel=0
wis=0
chrs=0
tot = 0

stats = randomize(st, dex, cnst, intel, wis, chrs)
while tot < 25 or tot > 35:
    stats = randomize(st, dex, cnst, intel, wis, chrs)
    tot = sum(stats)
print("""\n Strength: %d \n Dexterity: %d\n Constitution: %d\n Intelligence: %d\n Wisdom: %d\n Charisma: %d\n Stat total: %d"""
        % (stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], tot))