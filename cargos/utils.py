from geopy import distance


def calculate_distance(location1, location2):
    point1 = (location1.latitude, location1.longitude)
    point2 = (location2.latitude, location2.longitude)
    return distance.distance(point1, point2).miles


def get_nearest_cars(cargo, cars):
    pick_up_location = cargo.pick_up_location
    count = 0
    for car in cars:
        current_location = car.current_location
        dist = calculate_distance(pick_up_location, current_location)
        if dist <= 450 and car.load_capacity >= cargo.weight:
            count += 1
    return count


def get_all_cars_distance(cargo, cars):
    pick_up_location = cargo.pick_up_location
    car_distances = []
    for car in cars:
        current_location = car.current_location
        dist = calculate_distance(pick_up_location, current_location)
        car_distances.append({
            'car_number': car.number,
            'distance': dist
        })
    return car_distances
