from django.shortcuts import render, get_object_or_404

from isucon.portal.authentication.decorators import admin_is_authenticated


def get_base_context(user):
    return {
    }

@admin_is_authenticated
def dashboard(request):
    context = get_base_context(request.user)

    # FIXME: Query
    processiong_jobs = []
    top_teams = []

    context.update({
        "processiong_jobs": processiong_jobs,
        "top_teams": top_teams,
    })
    return render(request, "administration/dashboard.html", context)

@admin_is_authenticated
def jobs(request):
    context = get_base_context(request.user)

    # FIXME: Query
    jobs = []

    context.update({
        "jobs": jobs,
    })
    return render(request, "administration/jobs.html", context)

@admin_is_authenticated
def job_detail(request, pk):

    # FIXME: Query
    # job = get_object_or_404(Job, pk=pk)
    job = {
        "id": pk,
        "state": "dummy",
    } # Dummy

    context = get_base_context(request.user)

    context.update({
        "job": job,
    })
    return render(request, "administration/job_detail.html", context)


@admin_is_authenticated
def scores(request):
    context = get_base_context(request.user)

    # FIXME: Query
    teams = []

    context.update({
        "teams": teams,
    })
    return render(request, "administration/scores.html", context)

@admin_is_authenticated
def servers(request):
    context = get_base_context(request.user)

    # FIXME: Query
    servers = []

    context.update({
        "servers": servers,
    })
    return render(request, "administration/servers.html", context)
