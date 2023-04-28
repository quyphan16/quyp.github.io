services_dict = {"Air freshener":1, "Rain repellent":2, "Tire shine":2, "Wax":3, "Vaccum":5}

user_input = input("Enter services: ")
user_services = user_input.split(',')
print("Base car wash: $10")
services_total = 10

for services in user_services:
    if len(services) == 0:
        break
    else:
        total = services_dict[services]
        services_total += total
        print(f'{services}: ${total}')

print("-------------")
print(f'Total price: ${services_total}')
