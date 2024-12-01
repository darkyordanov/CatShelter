from django.shortcuts import render
from django.views.generic import \
    DeleteView, CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy

from cat_shelter.cats.forms import OurBoyForm
from cat_shelter.cats.models import \
    OurBoy, OurGirl, Kitten


# Our Boys
class OurBoyListView(ListView):
    model = OurBoy
    template_name = 'cat/our_boys.html'
    context_object_name = 'our_boys'


class OurBoyDetailView(DetailView):
    model = OurBoy
    template_name = 'cat/our_boy_detail.html'
    context_object_name = 'our_boy'


# class CreateOurBoyView(CreateView):
#     model = OurBoy
#     form_class = OurBoyForm
#     template_name = 'cats/add_our_boy.html'
#     success_url = reverse_lazy('our_boy_list')
    
#     def get_success_url(self):
#         return reverse_lazy('our boy details', kwargs={
#             'pk': self.object.pk
#         })v    

# class UpdateOurBoyView(UpdateView):
#     model = OurBoy
#     form_class = OurBoyForm
#     template_name = 'catalog/update_our_boy.html'
#     success_url = reverse_lazy('our_boy_list')

# class DeleteOurBoyView(DeleteView):
#     model = OurBoy
#     template_name = 'catalog/delete_our_boy.html'
#     success_url = reverse_lazy('our_boy_list')

    
# Our Girls
class OurGirlListView(ListView):
    model = OurGirl
    template_name = 'cat/our_girls.html'
    context_object_name = 'our_girls'


class OurGirlDetailView(DetailView):
    model = OurGirl
    template_name = 'cat/our_girl_detail.html'
    context_object_name = 'our_girl'


# Kitten
class KittenListView(ListView):
    model = OurGirl
    template_name = 'cat/kittens.html'
    context_object_name = 'kittens'


class OurGirlDetailView(DetailView):
    model = OurGirl
    template_name = 'cat/kitten_detail.html'
    context_object_name = 'kitten'

