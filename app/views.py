from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from dataclasses import dataclass

@dataclass
class Teams:
    name: str
    desc: str
    members: list

team_desc = {
    "procurement": "Procurement is the team that makes food for basecamp everyday.",
    "management": "Management is the team that keeps order in basecamp.",
    "documentation": "Documentation manages the social media and yearbook for that year.",
    "community": "Community organizes events every other Friday."
}
team_members = {
    "documentation": ['Conner','Kaleigh','Blair','Mina','Jay','Joshua','Kayleah'],
    "management": ['Owen','Jeremiah','Nick','Ab','Abigail','Mathew'],
    "procurement": ['Adrian','Bryce','Big John','Blaine','Wyatt'],
    "community": ['Jordan','Joby','Aj','Micah','Caleb']
}
def team_view(request: HttpRequest, team=None) -> HttpResponse:
    if team is not None:
        team = team.lower()
        if team in team_desc:
            team_ = Teams(name=team.capitalize(), desc=team_desc[team], members=team_members[team])
            context = {"team": team_}
            return render(request, 'teams_.html', context)

    groups = [Teams(name=team_name, desc=team_desc[team_name], members=team_members[team_name]) for team_name in team_desc]
    context = {"groups": groups}
    return render(request, "teams_.html", context)
