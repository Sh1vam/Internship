from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'main.html')

def index2(request):
    return render(request, 'index.html')
    
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        if name:
            return render(request, 'hello.html', {'response': {'message': f'{name.capitalize()}!'}})
        return JsonResponse({'error': 'Name not provided'}, status=400)
    return render(request, 'hello.html')