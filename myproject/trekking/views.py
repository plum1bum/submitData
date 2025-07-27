from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pass, User, Coordinates, Level, Image
from .serializers import PassSerializer

@api_view(['POST'])
def submit_data(request):
    if not request.data:
        return Response({"status": 400, "message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PassSerializer(data=request.data)
    if serializer.is_valid():
        # Сохранение связанных объектов
        user_data = serializer.validated_data.pop('user')
        coords_data = serializer.validated_data.pop('coords')
        level_data = serializer.validated_data.pop('level')
        images_data = serializer.validated_data.pop('images')

        user = User.objects.create(**user_data)

        coords = Coordinates.objects.create(**coords_data)
        level = Level.objects.create(**level_data)
        pass_obj = Pass.objects.create(user=user, coords=coords, level=level, **serializer.validated_data)

        for image_data in images_data:
            image = Image.objects.create(**image_data)
            pass_obj.images.add(image)

        return Response({"status": 200, "message": None, "id": pass_obj.id}, status=status.HTTP_200_OK)

    return Response({"status": 400, "message": "Не хватает полей"}, status=status.HTTP_400_BAD_REQUEST)
