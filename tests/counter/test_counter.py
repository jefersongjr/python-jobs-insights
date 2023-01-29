from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word1 = "TEMPORARY"
    word2 = "temporary"
    word3 = "BiKE"
    word4 = "bike"
    assert (count_ocurrences(path, word1) == 76)
    assert (count_ocurrences(path, word2) == 76)
    assert (count_ocurrences(path, word3) == 63)
    assert (count_ocurrences(path, word4) == 63)
