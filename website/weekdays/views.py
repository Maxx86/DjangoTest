from django.shortcuts import render
import datetime

def today(request):
    days = {
        0: ('Понеділок', 'monday.jpg'),
        1: ('Вівторок', 'tuesday.jpg'),
        2: ('Середа', 'wednesday.jpg'),
        3: ('Четвер', 'thursday.jpg'),
        4: ('П’ятниця', 'friday.jpg'),
        5: ('Субота', 'saturday.jpg'),
        6: ('Неділя', 'sunday.jpg'),
    }

    now = datetime.datetime.now()
    day_name, image = days[now.weekday()]

    return render(request, 'weekdays/today.html', {
        'day_name': day_name,
        'image': image
    })
