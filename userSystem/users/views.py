# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from users.models import User, Base


@csrf_exempt
def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        qualification = request.POST.get('qualification')

        engine = create_engine("mysql+mysqlconnector://root:root@localhost/test")
        Base.metadata.bind = engine
        sessionDB = sessionmaker()
        session = sessionDB()

        new_user = User(firstname=firstname,lastname=lastname,qualification=qualification)
        session.add(new_user)
        session.commit()

        context = {
            'firstname': firstname,
            'lastname': lastname,
            'qualification': qualification
        }

        template = loader.get_template('showdetail.html')
        return HttpResponse(template.render(context, request))

    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
