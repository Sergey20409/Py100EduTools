def calculate_total_sales(sales_list):
    ... # TODO Вычислите общую стоимость проданных товаров из списка `sales_list`



sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]
sum=0
for s1 in sales_data:
    sales=(s1["quantity"]*s1["price_per_unit"])
    sum+=sales

total_sales =sum  # TODO Вызовете функцию calculate_total_sales и передайте в функцию значение переменной sales_data
print(f"Общая стоимость проданных товаров: {total_sales}")
#