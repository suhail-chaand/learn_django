from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #SAFE_METHODS = [GET, HEAD, OPTIONS] are allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        #Write opertaions are restricted only to the owner
        return obj.owner == request.user