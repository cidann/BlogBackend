from rest_framework import permissions
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
INDIVIDUAL_METHODS=('DELETE','PUT','PATCH')
class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if(view.action in SAFE_METHODS):
            return True
        if(view.user):
            if(view.user.is_staff):
                return True
            if(view.user.id==view.kwargs.get('id') and view.action in INDIVIDUAL_METHODS):
                return True
        return False