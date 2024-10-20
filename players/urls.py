from django.urls import path
from .views import auth_views, player_views, profile_views, favorite_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', auth_views.register),
    path('login/', auth_views.login),
    path('user/me/', auth_views.get_me, name='user-me'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # AVATAR
    path('user/update-avatar/', profile_views.update_avatar, name='update-avatar'),
    path('players/<int:player_id>/update-avatar/', player_views.update_player_avatar, name='update_player_avatar'),
    # PLAYERS
    path('players/', player_views.get_players),
    path('players/byPrice/', player_views.get_players_by_price),
    path('players/byRating/', player_views.get_players_by_rating),
    path('players/byWage/', player_views.get_players_by_wage),
    path('players/favorites/', favorite_views.get_favorite_players, name='get_favorite_players'),
    # INTS
    path('players/<int:player_id>/', player_views.get_player_by_id),
    path('players/<int:player_id>/favorite/', favorite_views.toggle_favorite_player, name='toggle_favorite_player'),
    # STRS
    path('players/<str:player_name>/', player_views.get_player_by_name),
]
