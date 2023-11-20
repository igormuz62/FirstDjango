from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

author = {"name": "Игорь",
        "middle": "Михайлович",
        "surname": "Музычук",
        "phone": "8-910-447-21-02",
        "email": "immuzychuk@mts.ru"
          }



def home(request):
    text = """<h1>"Изучаем django"</h1>
                <strong>Автор</strong>: <i>Музычук И.М.</i>
            """
    return HttpResponse(text)

def about(request):
    text = f"""Имя: <b>{author["name"]}</b><br>
        Отчество: <b>{author["middle"]}</b><br>
        Фамилия: <b>{author["surname"]}</b><br>
        телефон: <b>{author["phone"]}</b><br>
        email: <b>{author["email"]}</b><br>
        """
    return HttpResponse(text)