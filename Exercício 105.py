

def notas(*args, sit=False):
    """
    notas(*args, sit=False)
        -> Função para analisar notas de alunos.
        :param n: uma ou mais notas dos alunos
        :param sit: Quando Verdadeiro, mostra a situação da média das notas
        :return: retorna um dicionário com as informações das notas."""
    soma = 0
    notas_class = {}
    notas_class['Total'] = len(args)
    notas_class['Maior'] = max(args)
    notas_class['Menor'] = min(args)

    for n in args:
        soma += n
    notas_class['Média'] = soma / len(args)

    if sit:
        if notas_class['Média'] >= 8:
            notas_class['Situação'] = 'Boa'
        elif 6 <= notas_class['Média'] <= 8:
            notas_class['Situação'] = 'Razoável'
        elif notas_class['Média'] < 6:
            notas_class['Situação'] = 'Ruim'

    return notas_class


resp = notas(3, 2.5, 7.5, 5, sit=True)
print(resp)
