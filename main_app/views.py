from django.shortcuts import render

dogs = [
  {'name': 'Pompom', 'breed': 'maltipoo', 'description': 'Sweet little child', 'age': 3.5},
  {'name': 'Polly', 'breed': 'cocapoo', 'description': 'Sweetheart', 'age': 2},
  {'name': 'Pixie', 'breed': 'maltese', 'description': 'Lovable & playful', 'age': 4},
  {'name': 'Pari', 'breed': 'maltipoo', 'description': 'Amazing Furbaby', 'age': 4.5},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
    })
