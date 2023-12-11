#Como podemos criar listas?
#riar listas usando loops e Range()
numeros =[]
for i in range(5):
    numeros.append(i)
print(numeros)

#Map
nomes = ['Larissa','Rafael', 'Marcus', 'John']

def aprovar_pessoa(nome):
    #aqui poderia ter uma lógivca mais complexa
    return nome + ' APROVADO!'

print(list(map(aprovar_pessoa,nomes)))