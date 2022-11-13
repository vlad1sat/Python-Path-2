import task as tax

count_money = float(input("Введите количество денег: ").replace(',', '.'))
sum_purchases = 0
while True:
    command = int(input('\nЧто вы хотите купить? 1- Квартиру, 2- Машину, 3- Дачу? '))
    if command > 3 or command < 1:
        print("\nПодсчет закончен!")
        break
    cost_purchase = float(input("\nВведите стоимость покупки без налога: ").replace(',', '.'))
    sum_purchases += cost_purchase
    if command == 1:
        sum_purchases += tax.Apartment(cost_purchase).get_tax()
    elif command == 2:
        sum_purchases += tax.Car(cost_purchase).get_tax()
    else:
        sum_purchases += tax.CountryHouse(cost_purchase).get_tax()

if count_money >= sum_purchases:
    print("Вам хватает на покупку!")
else:
    print("Вам не хватает на покупку", sum_purchases - count_money)
