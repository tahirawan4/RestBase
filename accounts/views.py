from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer


class UserCreate(APIView):
    """
    Creates the user.
    """
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Test(APIView):
    def get(self, request):
        return Response('data', status=status.HTTP_200_OK)
