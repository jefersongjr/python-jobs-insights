from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        file_data = csv.DictReader(file)
        data = []
        for row in file_data:
            data.append(row)
        return data


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    jobs_types = []
    for job in jobs:
        if job["job_type"] in jobs_types:
            pass
        else:
            jobs_types.append(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
