from typing import Union, List, Dict
from src.insights import jobs


def get_max_salary(path: str) -> int:
    data = jobs.read(path)
    salary_types = []
    for salary in data:
        if salary["max_salary"].isnumeric():
            salary_types.append(int(salary["max_salary"]))
    return max(salary_types)


def get_min_salary(path: str) -> int:
    data = jobs.read(path)
    salary_types = []
    for salary in data:
        if salary["min_salary"].isnumeric():
            salary_types.append(int(salary["min_salary"]))
    return min(salary_types)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (
          not str(job["min_salary"]).isnumeric()
          or not str(job["max_salary"]).isnumeric()
          ):
        raise ValueError
    if type(salary) not in [int, str]:
        raise ValueError
    if int(job["max_salary"]) < int(job["min_salary"]):
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    
    raise NotImplementedError
