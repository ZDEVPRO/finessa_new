from home.models import HomeAboutSection, HomeLogo, HomeTitle
from home.models import FImages


def fimages_view(request):
    fimages = FImages.objects.all().order_by('-id')[:1]
    context = {
        'fimages': fimages,
    }
    return context


def home_title_view(request):
    home_title = HomeTitle.objects.all().order_by('-id')[:1]
    context = {
        'home_title': home_title,
    }
    return context


def home_about_view(request):
    home_about = HomeAboutSection.objects.all().order_by('-id')[:1]
    context = {
        'home_about': home_about,
    }
    return context


def home_logo_view(request):
    home_logo = HomeLogo.objects.all().order_by('-id')[:1]
    context = {
        'home_logo': home_logo,
    }
    return context
