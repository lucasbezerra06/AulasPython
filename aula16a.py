lanche = ('Hambúrguer','Suco','Pizza','Pudim', 'Batata frita')
#Tuplas são imutáveis
#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche))
