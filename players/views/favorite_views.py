from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from ..models import FavoritePlayer, Player
from ..serializers import FavoritePlayerSerializer
from rest_framework import status

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def toggle_favorite_player(request, player_id):
    user = request.user
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        favorite, created = FavoritePlayer.objects.get_or_create(user=user, player=player)
        if created:
            return Response({'message': 'Player added to favorites'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Player is already in favorites'}, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            favorite = FavoritePlayer.objects.get(user=user, player=player)
            favorite.delete()
            return Response({'message': 'Player removed from favorites'}, status=status.HTTP_200_OK)
        except FavoritePlayer.DoesNotExist:
            return Response({'error': 'Player not in favorites'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorite_players(request):
    user = request.user
    favorites = FavoritePlayer.objects.filter(user=user)
    serializer = FavoritePlayerSerializer(favorites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
