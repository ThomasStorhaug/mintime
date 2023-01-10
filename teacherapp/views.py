from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from baseapp.models import Assessment, AssessmentGroup, User


@login_required
def teacherindex(request):
    user = request.user
    users = User.objects.all()
    assessment_group = AssessmentGroup.objects.all()
    context = {"Assessments": assessment_group, "Users": users, "User": user}
    return render(request, "teacherindex.html", context=context)
