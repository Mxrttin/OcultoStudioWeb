from django.shortcuts import render 
from user_agents import parse

# Create your views here.

def inicio(request):
    device_type = 'Desconocido'

    user_agent = request.META.get('HTTP_USER_AGENT','')

    if user_agent:
        user_agent_parsed = parse(user_agent)
        if user_agent_parsed.is_mobile:
            device_type = 'Movil';
        elif user_agent_parsed.is_tablet:
            device_type = 'Tablet'
        else:
            device_type = 'Escritorio'
    return render(request, "inicio.html",{'device_type': device_type})


