from django.shortcuts import render

def pagina_login(request):
    return render(request, 'projeto/login.html')

def pagina_barbearia(request):
    return render(request, 'projeto/barbearia.html')
