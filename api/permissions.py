from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    message = "You must be the author of this item."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.added_by or request.user.is_staff:
            return True
        else:
            return False