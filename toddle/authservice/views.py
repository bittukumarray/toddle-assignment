from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import urllib.request
from PIL import Image
from resizeimage import resizeimage
import boto3
# from botocore.exceptions import NoCredentialsError


class Signup(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            user=User.objects.create(username=username)
            user.set_password(password)
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token),})
        except:
            return Response({"msg":"This username already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)



ACCESS_KEY='AKIAZYNKOZNBATD2MWFX'
SECRET_KEY='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'
class ThumbNail(APIView):
    def post(self, request):
        url_data = request.data["url"]
        image_name=url_data.split("/")[-1]
        urllib.request.urlretrieve(url_data, 'Media-Images/'+image_name)
        with open('Media-Images/'+image_name, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [50, 50])
                cover.save("Resized-Media-Images/"+image_name, image.format)
                try:
                    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
                    s3.upload_file('Resized-Media-Images/'+image_name, 'toddle-bucket-resized', image_name, ExtraArgs={'ContentType': 'image/jpeg', 'ACL':'public-read'})
                    return Response({"resized_url":"https://toddle-bucket-resized.s3.ap-south-1.amazonaws.com/"+image_name})
                except FileNotFoundError:
                    return Response({"msg":"file not found/unable to download the image"}, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response({"msg":"AWS Credential was not valid"}, status=status.HTTP_401_UNAUTHORIZED)


