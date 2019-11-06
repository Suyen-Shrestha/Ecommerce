from django.urls import path

from .views import cart_home, cart_update, checkout_home, checkout_done_view

app_name = 'cart'

urlpatterns = [
    path('', cart_home, name='home'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update'),
    # path('products/<int:pk>', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>', ProductDetailSlugView.as_view()),


]

