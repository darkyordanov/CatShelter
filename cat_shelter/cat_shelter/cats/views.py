from django.shortcuts import render
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from cat_shelter.cats.models import \
    OurBoy, OurGirl, Kitten


def our_cats(request):
    context = {}
    
    return render(
        request,
        'template/our_cats.html',
        context
    )
    
    
def our_boys(request):
    context = {}
    
    return render(
        request,
        'template/our_boys.html',
        context
    )
  
  
class CreateOurBoysView(CreateView):
    model = OurBoy
    # form_class = OurBoysCreateForm
    template_name = 'catalog/add_our_boys.html'

    def get_success_url(self):
        return reverse_lazy('our boy details', kwargs={
            'pk': self.object.pk
        })


def our_boy_details(request):
    pass

        
class EditOurBoysView(CreateView):
    model = OurBoy
        
        
class DeleteOurBoysView(CreateView):
    model = OurBoy
    
    
# Our Girls
def our_girls(request):
    context = {}
    
    return render(
        request,
        'template/our_girls.html',
        context
    )
    
    
class CreateOurGirlsView(CreateView):
    model = OurGirl
    # form_class = OurGirlsCreateForm
    template_name = 'catalog/add_our_girls.html'

    def get_success_url(self):
        return reverse_lazy('our girl details', kwargs={
            'pk': self.object.pk
        })


def our_girl_details(request):
    pass

        
class EditOurGirlsView(CreateView):
    model = OurGirl
        
        
class DeleteOurGirlsView(CreateView):
    model = OurGirl


# Kitten
def kittens(request):
    context = {}
    
    return render(
        request,
        'template/kittens.html',
        context
    )
    
    
class CreateKittensView(CreateView):
    model = Kitten
    # form_class = KittensCreateForm
    template_name = 'catalog/add_kittens.html'

    def get_success_url(self):
        return reverse_lazy('kitten details', kwargs={
            'pk': self.object.pk
        })


def kitten_details(request):
    pass

        
class EditKittensView(CreateView):
    model = Kitten
        
        
class DeleteKittensView(CreateView):
    model = Kitten
