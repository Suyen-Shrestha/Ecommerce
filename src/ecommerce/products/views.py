from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

from django.http import Http404


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     slug = self.kwargs.get('slug')
    #     try:
    #         instance = Product.objects.get(slug=slug, active=True)
    #     except Product.DoesNotExist:
    #         raise Http404("Not Found..")
    #     except Product.MultipleObjectsReturned:
    #         qs = Product.objects.get(slug=slug, active=True)
    #         instance = qs.first()
    #     except:
    #         raise Http404("Uhmm")
    #     return instance


def product_detail_view(request, pk):
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.filter(pk=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist.")
    # except:
    #     print("Huh?")
    #
    # qs = Product.objects.filter(pk=pk)
    # if qs.exists() and qs.count == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist.")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist.")
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
