from django.views.generic import TemplateView

from django.core.paginator import Paginator

from django.conf import settings

from recommend_api import models as api_models


class LandingPageView(TemplateView):
    template_name = 'index.html'

    anime_list = api_models.Anime.objects.all()
    paginator = Paginator(anime_list, settings.PAGINATE_BY)

    def get_context_data(self):

        page = self.request.GET.get('page', 1)

        context = {}
        context['animes'] = self.paginator.page(page)

        return context
