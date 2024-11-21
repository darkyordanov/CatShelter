from django.shortcuts import render


def home(request):
    context = {}
    
    return render(
        request,
        'core/home.html',
        context
)
    
    
def about_us(request):
    context = {}
    
    return render(
        request,
        'core/about_us.html',
        context
)
    
    
def faq(request):
    context = {}
    
    return render(
        request,
        'core/faq.html',
        context
)
    
    
def contact_us(request):
    context = {}
    
    return render(
        request,
        'core/contact_us.html',
        context
)