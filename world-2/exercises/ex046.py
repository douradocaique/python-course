import emoji
from time import sleep

sparkles = emoji.emojize(':sparkles:')

print('{:=^22}'.format(' COUNTDOWN '))
for c in range(10,0,-1):
    sleep(1)
    print(c)
print('{} BOOOOM! {}'.format(sparkles,sparkles))

