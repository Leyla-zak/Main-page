from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from authentication.models import User

class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        """
        Обрабатывает GET-запросы на этот эндпоинт.
        Возвращает список всех зарегистрированных пользователей.
        """    
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
