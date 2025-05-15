from root.models import Team, FrequnlyQuestion, Leader, Pricing
from django.contrib.auth.models import User
from services.models import Category


def repeated_objects(request):
    pricings = Pricing.objects.filter(status=True).order_by("-created_at")
    users_count = User.objects.all().count()
    teams = Team.objects.filter(status=True)
    categories = Category.objects.all()
    team_count = teams.count()
    questions = FrequnlyQuestion.objects.filter(status=True)
    context = {
        "teams" : teams,
        "questions" : questions, 
        "tc" : team_count,
        "uc" : users_count,
        "categories" : categories,
        "pricing" : pricings,
    }
    return context