#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro, na ordem de colocação, Depois mostre:
#Apenas os 5 primeiros colocados.
#Os Ultimos 4 colocados da tabela
#Uma lista com os times em ordem alfabética
#Em que posição na tabela está o time da Chapecoense

time = 'Atlético-MG','Flamengo','São Paulo','Internacional','Palmeiras','Fluminense','Santos','Sport','Fortaleza EC','Vasco da Gama','Grêmio','Bahia','Corinthians','Atlético Goianiense','Botafogo','Athletico-PR','Ceará','Coritiba','Bragantino','Goiás'

print(f'Os cinco primeiros colocados são {time[:5]}')
print(f'Os Últimos 4 colocados são {time[-4:]}')
print(sorted(time))