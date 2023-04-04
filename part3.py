def convertSalary(salary, country):
    if country == "Canada":
       salary = salary * 1.48
       currency_name = "CAD"
       average_salary = 64000
    elif country == "USA":
        salary = salary * 1.18
        currency_name = "USD"
        average_salary = 56,516
    elif country == "UK":
        salary = salary * 0.91
        currency_name = "pound"
        average_salary = 35423
    elif country == "Cambodia":
        salary = salary * 4847.38
        currency_name ="Cambodian riel"
        average_salary = 5649856
    else:
        print("Invalid country entered")
    return salary, currency_name, average_salary

salary = int(input("Please enter yur salary in Germany:"))
country = str (input("Enter the country you want to migrate to:"))


salary, currency_name, average_salary = convertSalary(salary, country)

#comparison    
if salary > average_salary:
    print(f"You will be rich in {country} with a salary of {salary}{currency_name}")

else:
    print(f"You will be poor in {country} with a salary of {salary}{currency_name}")

    