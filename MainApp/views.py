from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

author = {"name": "Игорь",
        "middle": "Михайлович",
        "surname": "Музычук",
        "phone": "8-910-447-21-02",
        "email": "immuzychuk@mts.ru"
          }
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #             <strong>Автор</strong>: <i>Музычук И.М.</i>
    #         """
    # return HttpResponse(text)
    return render(request, "index.html")

def about(request):
    text = f"""Имя: <b>{author["name"]}</b><br>
        Отчество: <b>{author["middle"]}</b><br>
        Фамилия: <b>{author["surname"]}</b><br>
        телефон: <b>{author["phone"]}</b><br>
        email: <b>{author["email"]}</b><br>
        """
    return HttpResponse(text)

def get_item(request, id):
    for item in items:
        if item['id'] == id:
            result =  f"""
            <h2>Имя: {item["name"]} </h2>
            <p>Количество: {item["quantity"]}</p>
            <a href='/items'>Назад</a>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with {id} = id not found')

def items_list(request):
    result = "<h2> List items</2><ol>"
    for item in items:
        result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    result += '</ol>'
    return HttpResponse(result)
