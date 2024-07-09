from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import User
from .serializers import UserSerializer, DataSerializer
from .tasks import send_email


class UserAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(request.data)


