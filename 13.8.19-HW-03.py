#13.8.19 (HW-03) Герасименко QAP 1013



all_bil = int(input('Введите количество билетов'))
matrix = {}

for count in range(all_bil):
    if count < all_bil:
        matrix[count] = int(input('Введите возраст'))
        if 18 > matrix[count]:
            matrix[count] = 0
        elif 18 <= matrix[count] <= 25:
            matrix[count] = 990
        else:
            matrix[count] = 1390

cost = sum(matrix.values())
if all_bil > 3:
    final_cost = cost - (cost / 10)
    print('Предворительная сумма= ',cost)
    print('Окончательная сумма с учетом скидки 10%= ', final_cost)
else:
    final_cost = cost
    print('Окончательная сумма= ', final_cost)

