from django.views.generic import TemplateView

from django.core.paginator import Paginator

from django.conf import settings

from recommend_anime import models as anime_models


class LandingPageView(TemplateView):
    template_name = 'index.html'

    anime_list = anime_models.Anime.objects.all()
    paginator = Paginator(anime_list, settings.PAGINATE_BY)

    def get_context_data(self):

        page = self.request.GET.get('page', 1)

        context = {}
        context['animes'] = self.paginator.page(page)

        return context

class AnimePageView(TemplateView):
    template_name = 'anime.html'

    def get_context_data(self, pk):
        context = {}
        context['anime'] = anime_models.Anime.objects.get(pk=pk).verify_data()
        context['meta_url'] = settings.API_KEYS['tvdb']['meta_url']
        return context


