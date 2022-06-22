from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Объявления', 'url_name': 'advertisements'},
        {'title': 'Контакты', 'url_name': 'contacts'},
        {'title': 'О компании', 'url_name': 'about'},
        ]


# def advertisement_list(request, *args, **kwargs):
#     advertisements = [
#         'Мастер на час',
#         'Выведение из запоя',
#         'Услуги экскаватора-погрузчика, гидромолота, ямобура'
#     ]
#     advertisements_1 = [
#         'Мастер на час',
#         'Выведение из запоя',
#         'Услуги экскаватора-погрузчика, гидромолота, ямобура'
#     ]
#     return render(request, 'advertisements/advertisement_list.html',
#                   {'advertisements': advertisements, 'advertisements_1': advertisements_1})

class Home(View):
    def get(self, request):
        title = 'Главная'
        category_list = ('Личные вещи', 'Транспорт', 'Хобби', 'Отдых')
        regions = ('Москва', 'Московская область', 'республика Алтай', 'Вологодская область')
        return render(request, 'advertisements/index.html',
                      {'title': title,
                       'menu': menu,
                       'category_list': category_list,
                       'regions': regions})

    def post(self, request):
        title = 'Главная'
        category_list = ('Личные вещи', 'Транспорт', 'Хобби', 'Отдых')
        regions = ('Москва', 'Московская область', 'республика Алтай', 'Вологодская область')
        try:
            category = request.POST['category']
        except:
            category = None
        try:
            region = request.POST['regions']
        except:
            region = None
        try:
            q = request.POST['q']
        except:
            q = None
        return render(request, 'advertisements/index.html',
                      {'title': title,
                       'menu': menu,
                       'category_list': category_list,
                       'regions': regions,
                       'category': category,
                       'region': region,
                       'q': q
                       })


class Advertisements(View):

    def get(self, request):
        announcing = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Вологодская область',
            'Побелка квартир, офисов'
        ]
        return render(request, 'advertisements/advertisements.html',
                      {'menu': menu,
                       'announcing': announcing})

    def post(self, request):
        announcing = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Вологодская область',
            'Побелка квартир, офисов'
        ]
        key = True

        return render(request, 'advertisements/advertisements.html',
                      {'menu': menu,
                       'announcing': announcing,
                       'key': key})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'title': 'Контакты',
            'menu': menu,
            'phone': '8-800-708-19-45',
            'email': 'sales@company.com',
        }
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'title': 'О компании',
            'menu': menu,
            'name': 'ООО "Рога и копыта"',
            'description': 'Бесплатные объявления в вашем городе!',
        }
        return context
