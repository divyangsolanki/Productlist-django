from django.http import HttpResponse
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product,Review
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework import status
from django.shortcuts import render
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import TemplateHTMLRenderer
import json
class ProductList(APIView):

    def get(self, request, format=None):
        template_name = 'product.html'
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_obj = json.loads(json.dumps(serializer.data))
        return render(request,template_name,{'serializer1':json_obj,'status':Response.status_code})

    def post(self, request, format=None):
        template_name = 'product.html'
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request,template_name,serializer.data, status=status.HTTP_201_CREATED)
        return render(request,template_name,serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        template_name='productdetail.html'
        print(serializer.data,pk)
        return render(request,template_name,{'serializer':serializer.data,'pk':pk})


    def put(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        print("--",product)
        template_name='productdetail.html'
        serializer = ProductSerializer(product, data=request.data)
    
        if serializer.is_valid():
            print("__")
            serializer.save()
            return render(request,template_name,{'serializer':serializer,'pk':pk})
        return render(serializer.errors, status=status.HTTP_400_BAD_REQUEST,template_name='productdetail.html')

    def delete(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,template_name='productdetail.html')


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(
        created_by=self.request.user,
        pk=self.kwargs['pk'])

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return Review.objects.filter(id=review)
