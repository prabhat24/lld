from rest_framework import serializers

from .models import LendingModel

from books.serializers import BookItemSerializer





class LendingModelSerializer(serializers.ModelSerializer):

    issued_by = serializers.CharField(source="issued_by.user.username", read_only=True)
    item = BookItemSerializer(read_only=True)
    member = serializers.CharField(source="member.user.username", read_only=True)
    class Meta:
        model = LendingModel
        fields = ('issued_by', 
                'status',
                'due_date',
                'return_date',
                "item",
                "member")
