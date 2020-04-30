import difflib


babyshark = '''
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…
'''

starter = ('Baby ', 'Mommy ', 'Daddy ', 'Grandma ',  'Grandpa ', 'Let\'s go hunt, ')


print('\n\n')

texto_prueba =  (
                (starter[0] + 'shark, ' + ('doo ')*6 + '\n')*3 + starter[0] + 'shark!\n' +
                (starter[1] + 'shark, ' + ('doo ')*6 + '\n')*3 + starter[1] + 'shark!\n' +
                (starter[2] + 'shark, ' + ('doo ')*6 + '\n')*3 + starter[2] + 'shark!\n' +
                (starter[3] + 'shark, ' + ('doo ')*6 + '\n')*3 + starter[3] + 'shark!\n' +
                (starter[4] + 'shark, ' + ('doo ')*6 + '\n')*3 + starter[4] + 'shark!\n' +
                ((starter[5] + ('doo ')*6 + '\n'))*3 + starter[5][:13] + '!\n' + 
                'Run away,…'
                )


def song():
        lyric = ''
        starter = ('Baby ', 'Mommy ', 'Daddy ', 'Grandma ',  'Grandpa ', 'Let\'s go hunt, ')
        for i in starter[:5]: 
                lyric= lyric +((i + 'shark, ' + ('doo ')*6 + '\n')*3 + i + 'shark!\n')

        lyric = lyric + (starter[5] + ('doo ')*6 + '\n')*3 + starter[5][:13] + '!\n' + 'Run away,…'
        return lyric

print(song())



print(babyshark)
print(len(babyshark))
print(len(babyshark.replace(' ', '')))
print(babyshark.count(' '))

print(texto_prueba)
print(len(texto_prueba))
print(len(texto_prueba.replace(' ', '')))
print(texto_prueba.count(' '))

print(texto_prueba == babyshark)

text = open('/home/bob/Desktop/prework-datamad-no-solutions/lyrics/songs/baby-shark.txt', 'r')



def bottles_lyric():

        num = 99
        lyric = ''

        while num > 1:

                lyric = lyric + '{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.\n\n'.format(num, num, num-1)
                num -= 1

        lyric = lyric + '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'

        return lyric

print(bottles_lyric())