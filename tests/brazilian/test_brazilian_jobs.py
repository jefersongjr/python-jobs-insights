from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    keys_english = read_brazilian_file(path)

    for key in keys_english:
        assert "title" in key
        assert "salary" in key
        assert "type" in key
