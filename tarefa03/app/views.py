from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {'nome': 'pedro', 'matricula': '02301', 'idade': 60, 'cidade': 'riachuelo'},
        {'nome': 'carlos', 'matricula': '02302', 'idade': 32, 'cidade': 'boa saude'},
        {'nome': 'artur', 'matricula': '01203', 'idade': 65, 'cidade': 'santa maria'},
        {'nome': 'murilo', 'matricula': '0204', 'idade': 33, 'cidade': 'são tomé'},
        {'nome': 'gustavo', 'matricula': '0305', 'idade': 61, 'cidade': 'são paulo do potengi'},
    ]
    return render(request, 'usuarios.html', {'usuarios': lista_usuarios})    
