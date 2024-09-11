from rest_framework.views import APIView
from django.http import JsonResponse

class HelloWorldView(APIView):

    def get(self, request):
        
        name = request.query_params.get('name', '')
        return JsonResponse(dict(
            status='OK',
            message='조회에 성공하셨습니다.',
            data='Hello world!! {}'.format(name)
        ))