from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Player
from ..serializers import PlayerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

class PlayerPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_players(request):
    players = Player.objects.all()
    paginator = PlayerPagination()
    paginated_players = paginator.paginate_queryset(players, request)
    serializer = PlayerSerializer(paginated_players, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_player_avatar(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=404)

    if 'avatar_url' in request.FILES:
        player.avatar_url = request.FILES['avatar_url']
        player.save()
        return Response({'message': 'Avatar updated successfully'}, status=200)
    else:
        return Response({'error': 'No image provided'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_player_by_id(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
        serializer = PlayerSerializer(player, context={'request': request})
        return Response(serializer.data)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_player_by_name(request, player_name):
    try:
        players = Player.objects.filter(name__icontains=player_name)
        if players.exists():
            serializer = PlayerSerializer(players, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            return Response({'error': 'Player not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_player_by_nation(request, player_nation):
    try:
        players = Player.objects.filter(nation__icontains=player_nation)
        if players.exists():
            serializer = PlayerSerializer(players, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            return Response({'error': 'Player not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_players_by_price(request):
    try:
        players = Player.objects.filter(value_euro__isnull=False).order_by('-value_euro')
        paginator = PlayerPagination()
        paginated_players = paginator.paginate_queryset(players, request)
        serializer = PlayerSerializer(paginated_players, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_players_by_rating(request):
    try:
        players = Player.objects.all().order_by('-overall_rating')
        paginator = PlayerPagination()
        paginated_players = paginator.paginate_queryset(players, request)
        serializer = PlayerSerializer(paginated_players, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_players_by_wage(request):
    try:
        players = Player.objects.filter(wage_euro__isnull=False).order_by('-wage_euro')
        paginator = PlayerPagination()
        paginated_players = paginator.paginate_queryset(players, request)
        serializer = PlayerSerializer(paginated_players, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)