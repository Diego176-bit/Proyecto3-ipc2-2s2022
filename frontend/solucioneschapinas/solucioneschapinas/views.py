from django.shortcuts import render, redirect
import requests
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        user_name = request.POST['uname']
        password = request.POST['psw']
        print('hola 2')
        response = requests.post('http://127.0.0.1:5000/',json={"user_name": user_name, "password": password}, headers={'Connection': 'close'})
        if response.status_code == 200:
            response.close()
            return redirect('/inicio/')
        else:
            return render(request, 'index.html')
        
        
        
        
def inicio(request):
    response = requests.get('http://127.0.0.1:5000/consultarDatos').json()
    return render(request, 'inicio.html', {'response': response})

def instancias(request):
    response = requests.get('http://127.0.0.1:5000/consultarDatos').json()
    return render(request, 'instancias.html', {'response': response})