from django.shortcuts import render
from django.views.generic import TemplateView,FormView
# Create your views here.
from rest_framework.parsers import FormParser, MultiPartParser,FileUploadParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from model_assist.models import SubmittedImage,ImageClass2
from model_assist.serializers import SubmittedImageSerializer,ImageClass2Serializer
from analyzer.label_image import returnImageStat


# class FileUploadViewSet(ModelViewSet):
#
#     queryset = SubmittedImage.objects.all()
#     serializer_class = SubmittedImageSerializer
#     parser_classes = (MultiPartParser, FormParser,)
#
#     def perform_create(self, serializer):
#         serializer.save(image=self.request.data.get('image'))

class HandlePost(APIView):
    # parser_classes = (FileUploadParser,MultiPartParser,FormParser)

    def post(self, request, format=None):
        file_obj = request.data['image']
        a = SubmittedImage.objects.create(image=file_obj)
        print(a.path)
        res = returnImageStat(a.path)
        return Response(res)
