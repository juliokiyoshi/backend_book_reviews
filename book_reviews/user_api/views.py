from rest_framework.response import Response
from rest_framework import status, generics
import math
from .serializers import UserSerializer
from .models import UserModel

class UserRequests(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        users = UserModel.objects.all()
        total_of_users = users.count()
        if search_param:
            users = users.filter(title__icontains=search_param)
        serializer = self.serializer_class(users[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_of_users,
            "page": page_num,
            "last_page": math.ceil(total_of_users / limit_num),
            "notes": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"user": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class UserDetailRequest(generics.GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_user(self, pk):
        try:
            return UserModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        user = self.get_user(pk=pk)
        if user == None:
            return Response({"status": "fail", "message": f"User with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(user)
        return Response({"status": "success", "data": {"note": serializer.data}})

    def patch(self, request, pk):
        user = self.get_user(pk)
        if user == None:
            return Response({"status": "fail", "message": f"User with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"user": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_user(pk)
        if user == None:
            return Response({"status": "fail", "message": f"User with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


