n1 = (float(input('Digite a primeira nota do aluno:')))
n2 = (float(input('Digite a segunda nota do aluno:')))
m = (n1 + n2) / 2

if m < 5.0:
    print('A média do aluno é {:.1f}. REPROVADO'.format(m))
elif 5.0 <= m < 7.0:
    print('A média do aluno é {:.1f}. RECUPERAÇÃO'.format(m))
else:
    print('A média do aluno é {:.1f}. APROVADO'.format(m))