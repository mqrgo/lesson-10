from django.views.generic import ListView
from journalists import models, filters, serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class Index(ListView):
    template_name = 'journalists/index.html'
    context_object_name = 'journalists'
    model = models.Journalist

    def get_filters(self):
        return filters.Journalist(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filters'] = self.get_filters()

        return context


class JournalistAPIView(APIView):
    def get(self, request):
        qs = models.Journalist.objects.all()
        data = [f'{item.first_name} {item.last_name}' for item in qs]

        return Response(data=data)


class JournalistModelViewSet(ModelViewSet):
    queryset = models.Journalist.objects.all()
    filterset_class = filters.Journalist
    serializer_class = serializers.Journalist
