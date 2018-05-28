frase = ' Curso em Video Python '
print('''\nWhen this began I had nothing to say
And I'd get lost in the nothingness inside of me
(I was confused)
And I let it all out to find that
I'm not the only person with these things in mind
(Inside of me)
but all the vacancy the words revealed
Is the only real thing that I've got left to feel
(Nothing to lose)
Just stuck, hollow and alone
And the fault is my own
And the fault is my own''')
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase.upper().count('O'))
frase = frase.strip()
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
dividido = frase.split()
print(dividido[2][3])


