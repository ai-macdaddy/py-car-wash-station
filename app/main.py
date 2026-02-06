class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = max(1, min(comfort_class, 7))
        self.clean_mark = max(1, min(clean_mark, 10))
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = round(
            max(1.0, min(distance_from_city_center, 10.0)), 1
        )
        self.clean_power = max(1, min(clean_power, 10))
        self.average_rating = round(
            max(1.0, min(average_rating, 5.0)), 1
        )
        self.count_of_ratings = count_of_ratings


