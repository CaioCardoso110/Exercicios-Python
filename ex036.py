valor = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))
prestaçao = valor / (ano * 12)
porcetagem = salario * 30 / 100
print(f'Para pagar uma casa de R${valor:.2f} em {ano} ano(s) a prestação será de {prestaçao:.2f}')
if prestaçao > porcetagem:
    print('Emprestimo \033[;30;41mNEGADO\033[m!')
else:
    print('Emprestimo \033[;30;42mCONCEDIDO\033[m!')
