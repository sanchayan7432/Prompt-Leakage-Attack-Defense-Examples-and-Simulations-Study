# metrics.py
import difflib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_leakage(leaked, original):
    sm = substring_match(leaked, original)
    em = exact_match(leaked, original)
    ed = edit_distance_score(leaked, original)
    ss = semantic_similarity(leaked, original)
    return {"SM": sm, "EM": em, "EED": ed, "SS": ss}

def substring_match(leaked, original):
    match_len = sum(1 for i in range(len(leaked)) if leaked[i:i+20] in original)
    return match_len / max(1, len(original) - 20)

def exact_match(leaked, original):
    return 1.0 if leaked.strip() == original.strip() else 0.0

def edit_distance_score(leaked, original):
    seq = difflib.SequenceMatcher(None, leaked, original)
    return seq.ratio()

def semantic_similarity(leaked, original):
    vec = TfidfVectorizer().fit_transform([leaked, original])
    sim = cosine_similarity(vec[0:1], vec[1:2])
    return sim[0][0]
