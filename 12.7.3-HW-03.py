per_cent = {'ТКБ': 5.6, 'КСБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input('Введите сумму депозита'))
deposit=['ТКБ','СКБ', 'ВТБ', 'СБЕР' ]

deposit[0]=int(money/100*per_cent['ТКБ'])
deposit[1]=int(money/100*per_cent['КСБ'])
deposit[2]=int(money/100*per_cent['ВТБ'])
deposit[3]=int(money/100*per_cent['СБЕР'])
print(deposit)

max_earn= max(deposit)
print('Максимальная сумма, которую вы можете заработать —', max_earn)


