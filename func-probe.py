def update_car_info(**car):
    car.update({'is_available':'True'})
    return car


res = update_car_info(brand='Toyota', price=100000)
print(res)
