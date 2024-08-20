from datetime import date, timedelta

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR_FEE = 1000

car_register = {
 "toyotaBZ4X": {
 "brand": "Toyota",
 "model": "Corolla",
 "price": 96_000,
 "year": 2012,
 "month": 8,
 "new": False,
 "km": 163_000
 },
 "pugeot408": {
 "brand": "Pugeot",
 "model": "408",
 "price": 330_000,
 "year": 2019,
 "month": 1,
 "new": False,
 "km": 40_000
 },
 "audiRS3": {
 "brand": "Audi",
 "model": "RS3",
 "price": 473_000,
 "year": 2022,
 "month": 2,
 "new": True,
 "km": 0
 },
}

# case 2 oppgave 1
def print_car_information(car):
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price: {car['price']},-")
    print(f"Manufactured: {car['year']}-{car['month']}")
    condition = "New" if car['new'] else "Used"
    print(f"Condition: {condition}\n")

# case 2 oppgave 2
def create_car(brand, model, price, year, month, new, km):
    car = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km
    }
    car_register[brand + " " + model] = car
    return car

# case 2 oppgave 3
def get_car_age(car):
    current_year = date.today().year
    return current_year - car["year"]

# case 2 oppgave 4
def rent_car_monthly_price(car):
    annual_price = car["price"] * RENT_CAR_PERCENTAGE
    if car["new"]:
        annual_price += RENT_NEW_CAR_FEE
    return round(annual_price / 12, 2)

# case oppgave 5
def next_eu_control(car):
    production_date = date(car["year"], car["month"], 1)
    next_eu_control_date = production_date + timedelta(days=365 * 2)
    return next_eu_control_date

# case oppgave 6
def calculate_total_price(car):
    age = get_car_age(car)
    if is_new(car):
        return car["price"] + NEW_CAR_REGISTRATION_FEE
    elif 0 <= age <= 3:
        return car["price"] + 6681
    elif 4 <= age <= 11:
        return car["price"] + 4034
    elif 12 <= age <= 29:
        return car["price"] + 1729
    else:
        return car["price"]

def is_new(car):
    return car["new"]

if __name__ == '__main__':
    toyota = create_car("Toyota", "BZ4X", 30000, 2021, 1, True, 10000)
    print_car_information(toyota)
    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)} kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)} kr.")

    audi = create_car("Audi", "RS3", 50000, 2022, 3, True, 5000)
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)} kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)} kr.")

# case 2 oppgave 7
class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_information(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price},-")
        print(f"Manufactured: {self.year}-{self.month}")
        condition = "New" if self.new else "Used"
        print(f"Condition: {condition}\n")

    def get_age(self):
        current_year = date.today().year
        return current_year - self.year
        

    def next_eu_control(self):
        production_date = date(self.year, self.month, 1)
        next_eu_control_date = production_date + timedelta(days=365 * 2)
        return next_eu_control_date

    def rent_monthly_price(self):
        annual_price = self.price * RENT_CAR_PERCENTAGE
        if self.new:
            annual_price += RENT_NEW_CAR_FEE
        return round(annual_price / 12, 2)

    def calculate_total_price(self):
        age = self.get_age()
        if self.is_new():
            return self.price + NEW_CAR_REGISTRATION_FEE
        elif 0 <= age <= 3:
            return self.price + 6681
        elif 4 <= age <= 11:
            return self.price + 4034
        elif 12 <= age <= 29:
            return self.price + 1729
        else:
            return self.price

    def is_new(self):
        return self.new