from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer, UserSearchSerializer


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"code": 0, "data": {"id": user.id, "username": user.username}},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            return Response({
                'code': 0,
                'token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'data': user.username
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request):
        serializer = UserLogoutSerializer(data=request.data)
        if serializer.is_valid():
            token = request.auth
            token.blacklist()
            return Response({"message": "Logged out"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"code": 0, "data": serializer.data})


class SearchUsersView(APIView):
    def get(self, request):
        serializer = UserSearchSerializer(data=request.GET)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            users = User.objects.filter(username__icontains=username)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    def post(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({"message": "User deleted"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
