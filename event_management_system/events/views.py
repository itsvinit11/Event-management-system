from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Event, Registration, Venue
from .serializers import EventSerializer, RegistrationSerializer, VenueSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    authentication_classes = [JWTAuthentication]


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    authentication_classes = [JWTAuthentication]

    
    def perform_update(self, serializer):
        event = self.get_object()
        # Only allow the event creator to update/delete the event
        if event.creator != self.request.user:
            raise permissions.PermissionDenied("You are not allowed to modify this event.")
        serializer.save()

# Define similar views for other models (Registration, Venue, User) as per your requirements

# Create your views here.
