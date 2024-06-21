from django.shortcuts import render
from fashion.models import styles

# Create your views here.
def show_fashion(request):
    result = styles.objects.all()
    my_data = {'fashion_list': result}
    return render(request,'fashion/show_fashion.html', context=my_data)
