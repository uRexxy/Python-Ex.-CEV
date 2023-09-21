alunos = []
alunos_notas = []
notas = []
cont = 0
c = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    try:
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
    except:
        print('Dados inválidos, tente novamente.')
    media = (n1 + n2) / 2
    alunos_notas.append(nome)
    alunos_notas.append(media)
    notas.append(n1)
    notas.append(n2)
    alunos_notas.append(notas[:])
    alunos.append(alunos_notas[:])
    alunos_notas.clear()
    notas.clear()

    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if r == 'N':
        break
print('=-'*15)
print('No.   NOME      MÉDIA')
print('-----------------------')
for p in alunos:
    print(f'{cont:<4}   {alunos[c][0]:<8}   {alunos[c][1]:>3}')
    cont += 1
    c += 1
print('-----------------------')
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if escolha == 0:
        print(f'As notas do(a) {alunos[0][0]} são: {alunos[0][2]}')
    elif escolha == 1:
        print(f'As notas do(a) {alunos[1][0]} são: {alunos[1][2]}')
    elif escolha == 2:
        print(f'As notas do(a) {alunos[2][0]} são: {alunos[2][2]}')
    elif escolha == 3:
        print(f'As notas do(a) {alunos[3][0]} são: {alunos[3][2]}')
    elif escolha == 4:
        print(f'As notas do(a) {alunos[4][0]} são: {alunos[4][2]}')
    elif escolha == 999:
        print('Fim do programa.')
        break
    print('---------------------')
