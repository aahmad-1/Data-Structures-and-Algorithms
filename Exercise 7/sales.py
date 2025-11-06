def sales(cars, customers):
    possible_sales = 0
    car_prices_descending = sorted(cars, reverse=True)
    customer_maxPrice_descending = sorted(customers, reverse=True)
    customer_index = 0
    for i in range(len(cars)):
        if car_prices_descending[i] <= customer_maxPrice_descending[customer_index]:
            customer_index += 1
            possible_sales += 1

        if customer_index > len(customers) - 1: ## for preventing error for when total cars > total customers
            break

    return possible_sales

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))
    print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))
    print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))          
    print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))