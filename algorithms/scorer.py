from .levenshtein import levenshtein_score
from .soundex import soundex_score
from .jaro_winkler import jaro_winkler_score
from .token import jaccard_similarity

def combined_score(name1, name2, weights=(0.4, 0.2, 0.3, 0.1)):   
    lev_w, sdx_w, jw_w, jac_w = weights

    lev = levenshtein_score(name1, name2)
    sdx = soundex_score(name1, name2)
    jw = jaro_winkler_score(name1, name2)
    jac = jaccard_similarity(name1, name2)

    return (lev * lev_w) + (sdx * sdx_w) + (jw * jw_w) + (jac * jac_w)