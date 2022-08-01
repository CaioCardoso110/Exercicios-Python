classificacao = ('Palmeiras', 'Corinthians', 'Internacional', 'Atletico - MG',
                'Fluminense', 'Atletico - PR', 'São Paulo', 'Santos', 'Flamengo',
                 'Botafogo', 'Bragantino', 'Goias', 'Cuiaba', 'Coritiba', 'America - Mg',
                 'Avaí', 'Ceara', 'Atletico - GO', 'Juventude', 'Fortaleza')
print('=-' * 20)
print(f'Lista de times do Brasileirão: {classificacao}')
print('-=' * 20)
print(f'Os 5 primeiros são {classificacao[:5]}')
print('=-' * 20)
print(f'Os 4 ultimos são {classificacao[16:]}')
print('=-' * 20)
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print('=-' * 20)
time = classificacao.index('Corinthians')
print(f'O Corinthians esta na posição {time + 1}° lugar')
