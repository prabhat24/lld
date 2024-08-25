from datetime import datetime as dt
from datetime import date, timedelta
import pytz

from django.shortcuts import render
from books.models import BookItem
from transaction.models import LendingModel
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from books.serializers import BookItemSerializer
from transaction.serializers import LendingModelSerializer

# Create your views here.
class LendBook(APIView):


    def post(self, request, *args, **kwargs):
        print(request.data)
        _slug = self.kwargs['id']
        # print("bookslug", slug, _slug)
        book_item = BookItem.objects.get(slug=_slug)
        if book_item.status not in BookItem.StatusChoices.AVAILABLE:
            return Response({"error": f"current book with book status {book_item.status} cannot be loaned"},
                    status=status.HTTP_412_PRECONDITION_FAILED)

        # books issued to user
        books_lended = LendingModel.objects.filter(member__user=request.user, status=LendingModel.IssueStatus.LOANED)
        if books_lended.count() > 0:
            return Response({"error": f"members maximum quota exceeded", "lended_books": books_lended.count()}, 
                    status=status.HTTP_412_PRECONDITION_FAILED)
        
        lending_model = LendingModel.objects.create(item=book_item,
                member=request.user.member, 
                issued_by=request.user,
                due_date=dt.now(tz=pytz.timezone("Asia/Kolkata")) + timedelta(days=10)
                )
        book_item.status = BookItem.StatusChoices.LOANED
        book_item.save()
        return Response({"success": True, "book_lended": BookItemSerializer(book_item).data},
                status=status.HTTP_200_OK)


class ReturnBook(APIView):

    def post(self, request, *args, **kwargs):
        item_slug = self.kwargs["item_slug"]
        try:
            lending_model = LendingModel.objects.get(item__slug=item_slug, 
                    member=request.user.member,
                    status=LendingModel.IssueStatus.LOANED)
        except Exception as e:
            return Response({"error": "no loaned book record can be fetched"}, status=status.HTTP_400_BAD_REQUEST)
        panalty = lending_model.panalty
        if panalty:
            response = {
                "success": True,
                "lending_details": LendingModelSerializer(lending_model).data
            }
            print("response", response)
            return Response({"success": False, 
                            "fine": panalty,
                            "lending_model": LendingModelSerializer(lending_model).data }, 
                            status=status.HTTP_307_TEMPORARY_REDIRECT)
        
        bookItem = lending_model.item
        lending_model.return_date = dt.now(tz=pytz.timezone("Asia/Kolkata")).date()
        lending_model.status = LendingModel.IssueStatus.CLOSED
        lending_model.save()
        bookItem.status = BookItem.StatusChoices.AVAILABLE
        bookItem.save()
        return  Response({"success": True, "lending_model": LendingModelSerializer(lending_model).data }, status=status.HTTP_200_OK)



# Create your views here.
class RenewBook(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        _slug = self.kwargs['id']
        # print("bookslug", slug, _slug)
        try:
            book_item = BookItem.objects.get(slug=_slug)
        except:
            return Response({"error": f"item cannot be found"},
                    status=status.HTTP_412_PRECONDITION_FAILED)
        if book_item.status not in BookItem.StatusChoices.LOANED:
            return Response({"error": f"current book with book status {book_item.status} cannot be renewed"},
                    status=status.HTTP_412_PRECONDITION_FAILED)
        # books issued to user
        try:
            lending_model = LendingModel.objects.get(member__user=request.user, status=LendingModel.IssueStatus.LOANED, item=book_item)
        except:
            return Response({"error": f"this book is not loaned to the user"},
                    status=status.HTTP_412_PRECONDITION_FAILED)
        lending_model.status = LendingModel.IssueStatus.CLOSED
        lending_model.save()
        new_lending_model = LendingModel.objects.create(item=book_item,
                member=request.user.member, 
                issued_by=request.user,
                due_date=dt.now(tz=pytz.timezone("Asia/Kolkata")) + timedelta(days=10)
                )
        book_item.status = BookItem.StatusChoices.LOANED
        book_item.save()
        return Response({"success": True, "book_lended": BookItemSerializer(book_item).data},
                status=status.HTTP_200_OK)
