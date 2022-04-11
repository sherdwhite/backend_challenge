from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend_challenge.serializers import QuotesSerializer
from quotes.models import Quote


class IndexView(TemplateView):
    template_name = 'backend_challenge/index.html'


class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all quotes to be viewed.
    """
    queryset = Quote.objects.all().order_by('-modified')
    serializer_class = QuotesSerializer


@api_view(['POST'])
def create_quote(request):
    """
    Create a new quote.
    """
    if request.method == 'POST':
        print(request.data)
        serializer = QuotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
