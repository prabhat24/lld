from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BookItem, Category
from .serializers import BookItemSerializer

# Create your views here.
class SearchBook(APIView):

    def get(self, request, *args, **kwargs):
        print(request.query_params)
        query = Q()

        if request.query_params.get("title"):
            print("title", request.query_params.get("title"))
            query = Q(book__title__icontains=request.query_params["title"].lower())
        if request.query_params.get("author"):
            query = query & Q(book__author__name__icontains=request.query_params["author"].lower())
        if request.query_params.get("subject"):
            subjects = Category.objects.filter(label__icontains=request.query_params["subject"].lower())[:3]
            print(subjects)
            query = query & Q(book__category__in=subjects)
        if request.query_params.get("pub_date"):
            pass

        queryset = BookItem.objects.filter(query)[:10]


        # values("id", 
        #                                               "rack__location_identifier", 
        #                                               "price",
        #                                               "format",
        #                                               "publication_date", 
        #                                               "book__title", 
        #                                               "book__author")
        
        serializer = BookItemSerializer(queryset, many=True)
        # response = []

        # for obj in queryset:
        #     single_obj = {}
        #     single_obj['id'] = obj['id']
        #     single_obj['rack'] = obj['rack__location_identifier']
        #     single_obj['price'] = obj['price']
        #     single_obj['format'] = obj['format']
        #     single_obj['publication_date'] = obj['publication_date'].strftime("%Y %m %d") if obj['publication_date'] else None
        #     single_obj['title'] = obj['book__title']
        #     single_obj['author'] = obj['book__author']
        #     response.append(single_obj)
        # print(response)
        return Response(serializer.data)

