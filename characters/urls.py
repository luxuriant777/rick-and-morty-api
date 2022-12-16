from django.urls import path

from characters.views import get_random_character

app_name = "characters"

urlpatterns = [
    path("characters/random/", get_random_character, name="character-random"),
]
