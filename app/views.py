import datetime
import os
# import sys

from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    files_list = list()

    fl = os.listdir(settings.FILES_PATH)
    for item in fl:
        file_description = dict()
        file_path = os.path.join(os.path.abspath(settings.FILES_PATH), item)
        file_attr = os.stat(file_path)
        st_ctime = datetime.datetime.fromtimestamp(file_attr.st_ctime)
        st_mtime = datetime.datetime.fromtimestamp(file_attr.st_mtime)
        ctime = datetime.datetime(st_ctime.year, st_ctime.month, st_ctime.day)
        mtime = datetime.datetime(st_mtime.year, st_mtime.month, st_mtime.day)
        if not(date) or date == ctime or date == mtime:
            file_description["name"] = item
            file_description["ctime"] = st_ctime
            file_description["mtime"] = st_mtime
            files_list.append(file_description)

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files_list,
        'date': (None if not(date) else datetime.date(date.year, date.month, date.day))
    }
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = os.path.join(os.path.abspath(settings.FILES_PATH), name)
    with open(file_path) as text_file:
        file_content = text_file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name,
                 'file_content': file_content}
    )
