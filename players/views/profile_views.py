from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from ..serializers import UserSerializer
from ..models import Profile

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_avatar(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response({'error': 'User profile does not exist.'}, status=404)

    avatar_file = request.FILES.get('avatar')
    if avatar_file:
        profile.avatar = avatar_file
        profile.save()
        avatar_url = profile.avatar.url
        return Response({
            'message': 'Avatar updated successfully.',
            'user': UserSerializer(request.user).data,
            'avatar_url': avatar_url
        })
    return Response({'error': 'No avatar file provided.'}, status=400)
