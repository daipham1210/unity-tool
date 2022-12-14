from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubscriberSerializer

class SubscriberListView(APIView):
    def post(self, request):
        data = {
            'email': request.data.get('email'), 
        }
        serializer = SubscriberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
