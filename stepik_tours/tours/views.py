from django.shortcuts import render

from django.views import View

from django.http import Http404

from tours.data import title as tit, subtitle as sub, description as des, departures as dep, tours as tour

from tours.mainview import masiv, new_dict

# Create your views here.


class MainView(View):
    def get(self, request):
        context = {
            'new_dict': new_dict,
            'masiv': masiv,
            'title': tit,
            'subtitle': sub,
            'description': des,
            'departures': dep,
            'tours': tour
        }
        return render(request, 'tours/index.html', context=context)


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        kol_tours = 0
        dict = {}
        mas = []
        max_price = 0
        min_price = 100000
        max_nights = 0
        min_nights = 1000
        for key, value in tour.items():
            for key1, value1 in value.items():
                if departure == value1:
                    kol_tours += 1
                    dict.update({key: value})       # формирования словаря
        for key, value in dict.items():
            for key1, value1 in value.items():
                if key1 == 'price':
                    if value1 > max_price:
                        max_price = value1
                    if value1 < min_price:
                        min_price = value1
                if key1 == 'nights':
                    if value1 > max_nights:
                        max_nights = value1
                    if value1 < min_nights:
                        min_nights = value1

        for k, v in dict.items():
            v.update({'KEY': k})                    # добовляем номер нашего тура в словарь
            mas.append(v)                           # делаем из словаря - список, для удобства
        context = {
            'departures': dep[departure],
            'kol_tours': kol_tours,
            'max_price': max_price,
            'min_price': min_price,
            'max_nights': max_nights,
            'min_nights': min_nights,
            'mas': mas
        }
        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        city = ""
        for k, v in tour.items():
            if id == k:
                for k1, v1 in v.items():
                    if k1 == "departure":
                        for key, value in dep.items():
                            if key == v1:
                                city = value
        if id not in tour.keys():
            raise Http404

        context = {
            'tours': tour[id],
            'city': city
        }

        return render(request, 'tours/tour.html', context=context)
