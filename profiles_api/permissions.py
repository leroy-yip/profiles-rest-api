from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # read only
        if request.method in permissions.SAFE_METHODS:
            return True
        # user can edit his/her profile only
        return obj.id == request.user.id
