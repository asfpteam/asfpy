"""
ASFPy methods

Say some things about it here.
"""

import operator

#################################################
# Constants
#
# NOTE: These constants refer to data fields that
#       are collected in forms, so may be changed
#       accordingly.
#
#################################################

URM = "urm"
LIM = "lim"
SCHOOL = "du"

#################################################
# APPLICANT-ONLY METHODS
#################################################

def rank(applicant):
    """
    Rank an applicant by attribute combinations.
    """
    is_urm = applicant[URM]
    is_lim = applicant[LIM]
    is_school = applicant[SCHOOL]

    if (is_urm and is_lim and is_school):
        rank = 0
    elif (is_urm and is_lim):
        rank = 1
    elif (is_urm or is_lim) and is_school:
        rank = 2
    elif (is_urm or is_lim):
        rank = 3
    elif is_school:
        rank = 4
    else:
        rank = 5

    return rank

def prioritize(applicants):
    """
    Prioritize applicants by rank of attributes.
    """
    for a in applicants:
        a["rank"] = rank(a)
    applicants.sort(key = operator.itemgetter("rank"))
    return applicants

#################################################
# EDITOR-ONLY METHODS
#################################################

def editors_by_role(editors, role):
    """
    Get a sublist of editors by role.
    """
    return [e for e in editors if e["role"] == role]

def editors_by_category(editors, category):
    """
    Get a sublist of editors by category
    """
    return [e for e in editors if category in e["categories"]]

def capacity(editors):
    """
    Compute editing capacity, the number of statements an editor
    can read, for a list of editors.
    """
    return sum(e["capacity"] for e in editors)

