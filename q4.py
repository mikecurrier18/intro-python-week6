from datetime import datetime


def add_height(feet, inches):
    current_datetime = datetime.now()
    height_timedelta = timedelta(days=0, hours=feet, minutes=inches)
    updated_datetime = current_datetime + height_timedelta
    return updated_datetime

feet = 5
inches = 8

new_datetime = add_height(feet, inches)
print(new_datetime)
print('Type:', type(new_datetime))
