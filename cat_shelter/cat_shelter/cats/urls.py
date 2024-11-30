from django.urls import path, include

from cat_shelter.cats.views import \
    our_cats, \
    our_boys, CreateOurBoysView, our_boy_details, EditOurBoysView, DeleteOurBoysView, \
    our_girls, CreateOurGirlsView, our_girl_details, EditOurGirlsView, DeleteOurGirlsView, \
    kittens, CreateKittensView, kitten_details, EditKittensView, DeleteKittensView

urlpatterns = (
    path('our_cats/', include([
        #  Our Cats Url
        path('', our_cats, name='our_cats'),
        
        # Our Boys Urls
        path('our_boys/', include([   
            path('', our_boys, name='our_boys'),
            path('add_our_boys_cbv/', CreateOurBoysView.as_view(), name='add our boys cbv'),
            path('<int:pk>/', include([
                path('', our_boy_details, name='our boy details'),
                path('edit_our_boys/', EditOurBoysView.as_view(), name='edit our boys'),
                path('delete_our_boys/', DeleteOurBoysView.as_view(), name='delete our boys'),
            ])),
        ])),
        
        # Our Girls Urls
        path('our_girls/', include([   
            path('', our_girls, name='our_girls'),
            path('add_our_girlsv_cbv/', CreateOurGirlsView.as_view(), name='add our girls cbv'),
            path('<int:pk>/', include([
                path('', our_girl_details, name='our girl details'),
                path('edit_our_girls/', EditOurGirlsView.as_view(), name='edit our girls'),
                path('delete_our_girls/', DeleteOurGirlsView.as_view(), name='delete our girls'),
            ])),
        ])),

        # Our Kittens Urls
        path('kittens/', include([   
            path('', kittens, name='kittens'),
            path('add_kittens_cbv/', CreateKittensView.as_view(), name='add kittens cbv'),
            path('<int:pk>/', include([
                path('', kitten_details, name='kitten details'),
                path('edit_kittens/', EditKittensView.as_view(), name='edit our kittens'),
                path('delete_kittens/', DeleteKittensView.as_view(), name='delete our kittens'),
            ])),
        ])),
    ])),
)
