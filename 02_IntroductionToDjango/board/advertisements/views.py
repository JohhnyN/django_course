from django.shortcuts import render


# Create your views here.


def advertisement_list(request, *args, **kwargs):
    course_pages = [{'title': 'Старт в DevOps: системное администрирование для начинающих', 'url_name': 'devops'},
                    {'title': 'Веб-дизайн 3.0', 'url_name': 'web-design-3'},
                    {'title': 'Управляющий рестораном', 'url_name': 'restaurant-manager'},
                    {'title': 'Excel + Google Таблицы с нуля до PRO', 'url_name': 'excel-gsheets'},
                    {'title': 'Музыкальный менеджер', 'url_name': 'music-manager'}]
    return render(request, 'advertisement/advertisement_list.html',
                  {'title': 'advertisement_list', 'course_pages': course_pages})


def web_design_3(request, *args, **kwargs):
    context = {
        'title': 'web-design-3',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_2_262ebbb0b9720b2314fe4d9ce45cc3609e942716.webp',
        'link_to_the_course': 'https://skillbox.ru/course/web-design-3/',
        'course_name': 'Веб-дизайн 3.0',
        'price': '102 960'
    }
    return render(request, 'advertisement/devops.html', context)


def devops(request, *args, **kwargs):
    context = {
        'title': 'devops',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_2_bd5c75285fc4a318ae23886b16f51b2b110ea1b1.webp',
        'link_to_the_course': 'https://skillbox.ru/course/devops/',
        'course_name': 'Старт в DevOps',
        'price': '4 514'
    }
    return render(request, 'advertisement/devops.html', context)


def restaurant_manager(request, *args, **kwargs):
    context = {
        'title': 'restaurant-manager',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_2_70fe1c9221c549f772e76482718b4c3d663dcfe6.webp',
        'link_to_the_course': 'https://skillbox.ru/course/restaurant-manager/',
        'course_name': 'Управляющий рестораном',
        'price': '68 345'
    }
    return render(request, 'advertisement/restaurant-manager.html', context)


def excel_gsheets(request, *args, **kwargs):
    context = {
        'title': 'excel-gsheets',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_2_b609db3df74c3b33f9819476d65eef1ed431af6f.webp',
        'link_to_the_course': 'https://skillbox.ru/course/excel-gsheets/',
        'course_name': 'Excel + Google Таблицы с нуля до PRO',
        'price': '31 597'
    }
    return render(request, 'advertisement/restaurant-manager.html', context)


def music_manager(request, *args, **kwargs):
    context = {
        'title': 'music-manager',
        'img_url': 'https://248006.selcdn.ru/LandGen/desktop_2_4280e43b6ab85f950b81ec1f4be9d2170943f145.webp',
        'link_to_the_course': 'https://skillbox.ru/course/music-manager/',
        'course_name': 'Музыкальный менеджер',
        'price': '5 382'
    }
    return render(request, 'advertisement/restaurant-manager.html', context)
