class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        if not 1 <= comfort_class <= 7:
            raise ValueError("Comfort class must be between 1 and 7.")
        if not 1 <= clean_mark <= 10:
            raise ValueError("Clean mark must be between 1 and 10.")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int):
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("Distance from city center must be between 1.0 and 10.0.")
        if not 1 <= clean_power <= 10:
            raise ValueError("Clean power must be between 1 and 10.")
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError("Average rating must be between 1.0 and 5.0.")
        if count_of_ratings < 0:
            raise ValueError("Count of ratings cannot be negative.")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0

        price = (car.comfort_class * (
                    self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> bool:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
            return True
        return False

    def serve_cars(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            washing_price = self.calculate_washing_price(car)
            if self.wash_single_car(car):
                income += washing_price
        return round(income, 1)

    def rate_service(self, new_rating: float) -> None:
        if not (1.0 <= new_rating <= 5.0):
            raise ValueError("Rating must be between 1.0 and 5.0.")

        total_rating = (self.average_rating * self.count_of_ratings) + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
