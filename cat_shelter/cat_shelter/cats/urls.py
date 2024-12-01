from django.urls import path, include

from cat_shelter.cats.views import \
    OurCatsListView, \
    OurBoyListView, OurBoyDetailView, \
    OurGirlListView, OurGirlDetailView, \
    KittenListView, KittenDetailView

urlpatterns = (
    path('our_cats/', include([
        #  Our Cats Url
        path('', OurCatsListView.as_view(), name='our_cats'),
        
        # Our Boys Urls
        path('our_boys/', include([   
            path('', OurBoyListView.as_view(), name='our_boys'),
            # path('add_our_boys_cbv/', CreateOurBoysView.as_view(), name='add our boys cbv'),
            path('<int:pk>/', include([
                path('', OurBoyDetailView.as_view(), name='our boy details'),
                # path('edit_our_boys/', EditOurBoysView.as_view(), name='edit our boys'),
                # path('delete_our_boys/', DeleteOurBoysView.as_view(), name='delete our boys'),
            ])),
        ])),
        
        # Our Girls Urls
        path('our_girls/', include([   
            path('', OurGirlListView.as_view(), name='our_girls'),
            # path('add_our_girlsv_cbv/', CreateOurGirlsView.as_view(), name='add our girls cbv'),
            path('<int:pk>/', include([
                path('', OurGirlDetailView.as_view(), name='our girl details'),
                # path('edit_our_girls/', EditOurGirlsView.as_view(), name='edit our girls'),
                # path('delete_our_girls/', DeleteOurGirlsView.as_view(), name='delete our girls'),
            ])),
        ])),

        # Our Kittens Urls
        path('kittens/', include([   
            path('', KittenListView.as_view(), name='kittens'),
            # path('add_kittens_cbv/', CreateKittensView.as_view(), name='add kittens cbv'),
            path('<int:pk>/', include([
                path('', KittenDetailView.as_view(), name='kitten details'),
                # path('edit_kittens/', EditKittensView.as_view(), name='edit our kittens'),
                # path('delete_kittens/', DeleteKittensView.as_view(), name='delete our kittens'),
            ])),
        ])),
    ])),
)
