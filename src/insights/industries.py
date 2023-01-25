from typing import List, Dict

from src.insights import jobs


def get_unique_industries(path: str) -> List[str]:
    industries = jobs.read(path)
    industry_types = []
    for industry in industries:
        if industry["industry"] in industry_types:
            pass
        elif industry["industry"] == '':
            pass
        else:
            industry_types.append(industry["industry"])
    return industry_types


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = [data
                     for data in jobs if data["industry"] == industry]
    return filtered_jobs
    raise NotImplementedError
