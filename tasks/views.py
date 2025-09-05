from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ViewSet):

    def get_queryset(self):
        return Task.objects.order_by("-created_at")


    # GET /tasks/
    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


    # POST /tasks/
    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # GET /tasks/{id}/
    def retrieve(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


    # PUT /tasks/{id}/ — update title & description
    def update(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    # PATCH /tasks/{id}/ — toggle completed only
    def partial_update(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        # Only allow 'completed' in PATCH
        if set(request.data.keys()) - {"completed"}:
            return Response({"detail": "Only 'completed' can be patched."}, status=400)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    # DELETE /tasks/{id}/
    def destroy(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)