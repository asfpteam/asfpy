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

def asfp_rank(applicant):
    """
    Rank an applicant by attribute combinations by the standard ASFP method of
    ranking by underrepresented minority (URM) status, whether an applicant has
    limited access (LIM) to mentors in academia and research, and if the applicant
    is affiliated with the University of Denver (DU).

    Parameters
    ----------
    applicant: dict
        An object that represents an applicant (often within a list) with 
        attributes including:
            - "id" a unique string identifier
            - "urm" a boolean designation of URM status
            - "lim" a boolean designation of LIM status
            - "du" a boolean designation of DU affiliation

    Returns
    -------
    rank: integer
        A ranking that represents an applicant's pool relative to an
        ASFP-designed schema, as clarified through boolean logic in code below.
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

def prioritize(applicants, rank_method = asfp_rank):
    """
    Prioritize applicants by rank of attributes.

    Parameters
    ----------
    applicants: list
        The list `applicants` of dicts of each applicant.
    rank_method: function
        The method of assinging ranks under label "rank" based on attributes
        that are necessarily present in items of `applicants`.

    Returns
    -------
    applicants: list
        A copy of applicants is returned, sorted by rank as determined by
        `rank_method`.
    """
    for a in applicants:
        a["rank"] = rank_method(a)
    return sorted(applicants, key = operator.itemgetter("rank"))

#################################################
# EDITOR-ONLY METHODS
#################################################

def editors_by_role(editors, role):
    """
    Get a sublist of editors by role.
    """
    return [e for e in editors if e["role"] == role]

def editors_by_categories(editors, categories):
    """
    Get a sublist of editors by category
    """
    return [e for e in editors if e["categories"].intersection(categories)]

def capacity(editors):
    """
    Compute editing capacity, the number of statements an editor
    can read, for a list of editors.
    """
    return sum(e["capacity"] for e in editors)

def sort_editors_by_capacity(editors):
    """
    Sort editors by capacity.
    """
    editors.sort(key = operator.itemgetter("capacity"), reverse = True)
    return editors
