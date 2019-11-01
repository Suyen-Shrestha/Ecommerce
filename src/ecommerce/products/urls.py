from django.urls import path

from .views import ProductListView, ProductDetailSlugView


urlpatterns = [
    path('', ProductListView.as_view()),
    path('<slug>/', ProductDetailSlugView.as_view()),
    # path('products/<int:pk>', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>', ProductDetailSlugView.as_view()),


]

