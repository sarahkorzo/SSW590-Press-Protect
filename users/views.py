from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

# Helper functions to check roles
def is_editor(user):
    return user.role == 'editor'

def is_marketer(user):
    return user.role == 'marketer'

def is_viewer(user):
    return user.role == 'viewer'

# Views for each role
@login_required
@user_passes_test(is_editor)
def editor_dashboard(request):
    return HttpResponse("Welcome, Editor! You can create and edit content.")

@login_required
@user_passes_test(is_marketer)
def marketer_dashboard(request):
    return HttpResponse("Welcome, Marketer! You can view and schedule content.")

@login_required
@user_passes_test(is_viewer)
def viewer_dashboard(request):
    return HttpResponse("Welcome, Viewer! You have read-only access.")
