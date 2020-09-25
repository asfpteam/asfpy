"""
ASFPy methods

Say some things about it here.
"""

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
# Methods
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
