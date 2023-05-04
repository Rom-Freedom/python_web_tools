from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

web_tools_dict = {
    'core': 'Python core - базовой синтаксисс и конструкции',
    'oop': 'ООП - в Python  все является объектом',
    'flask': 'Flask — фреймворк для создания веб-приложений',
    'django': 'Django - фреймворк для создания веб-приложений',
    'git': 'Git (Global Information Tracker) Система контроля версий',
    'sql': 'SQL (Structured Query Language) Язык структурированных запросов',
    'algorithms': 'Алгоритмы и структуры данных',
    'htmlCss': 'HyperText Markup Language — «язык гипертекстовой разметки»'}


def get_yyyy_converters(request, web_tool):
    return HttpResponse(f'Вы передали число из 4 цифр - {web_tool}')

def get_my_float_converters(request, web_tool):
    return HttpResponse(f'Вы передали вещественное число - {web_tool}')

def get_my_date_converters(request, web_tool):
    return HttpResponse(f'Вы передали дату - {web_tool}')


def index(request):
    tools = list(web_tools_dict)
    #f'<li> <a href="{redirect_path}">{i.title()}</a> </li>'
    context = {
        'tools': tools,
        'web_tools_dict': web_tools_dict
    }
    return render(request, 'basicPythonTools/index.html', context=context)


def show_information_about_tool(request, web_tool: str):
    description = web_tools_dict.get(web_tool)
    tools = list(web_tools_dict)
    data = {
        'description_tool': description,
        'tool': web_tool,
        'tools': tools,
    }

    return render(request, 'basicPythonTools/info_tools.html', context=data)


def show_information_about_tool_by_number(request, web_tool: int):
    tools = list(web_tools_dict)
    if web_tool > len(tools):
        return HttpResponseNotFound(f'Несуществующий номер - {web_tool}')
    name_tool = tools[web_tool - 1]
    redirect_url = reverse('python_tools', args=[name_tool])
    return HttpResponseRedirect(f'/basicPythonTools/{name_tool}')
