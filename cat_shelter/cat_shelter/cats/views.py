from django.shortcuts import render
from django.views.generic import \
    DeleteView, CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy

from cat_shelter.cats.models import \
    Cat, OurBoy, OurGirl, Kitten
    

# Our Cats
class OurCatsListView(ListView):
    model = Cat
    template_name = 'cats/our_cats.html'
    context_object_name = 'our_boys'


# Our Boys
class OurBoyListView(ListView):
    model = OurBoy
    template_name = 'cats/our_boys/our_boys.html'
    context_object_name = 'our_boys'


class OurBoyDetailView(DetailView):
    model = OurBoy
    template_name = 'cats/our_boys/our_boy_detail.html'
    context_object_name = 'our_boy'


# Our Girls
class OurGirlListView(ListView):
    model = OurGirl
    template_name = 'cats/our_girls/our_girls.html'
    context_object_name = 'our_girls'


class OurGirlDetailView(DetailView):
    model = OurGirl
    template_name = 'cats/our_girls/our_girl_detail.html'
    context_object_name = 'our_girl'


# Kitten
class KittenListView(ListView):
    model = Kitten
    template_name = 'cats/kittens/kittens.html'
    context_object_name = 'kittens'


class KittenDetailView(DetailView):
    model = Kitten
    template_name = 'cats/kittens/kitten_detail.html'
    context_object_name = 'kitten'
    
    

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

    