from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# Simple REST API Examples

@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint that returns the API status.
    Demonstrates a basic GET request with JSON response.
    """
    return Response({
        'status': 'healthy',
        'message': 'OctoFit Tracker API is running',
        'version': '1.0.0'
    })

@api_view(['POST'])
def echo(request):
    """
    Simple echo endpoint that returns the data sent in the request.
    Demonstrates a basic POST request with request/response handling.
    """
    data = request.data
    return Response({
        'received': data,
        'message': 'Echo successful',
        'timestamp': request.META.get('HTTP_DATE', 'N/A')
    }, status=status.HTTP_200_OK)
