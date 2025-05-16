import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_DIR)

OUTPUT_PATH=os.path.join(PROJECT_PATH, "output")
os.makedirs(OUTPUT_PATH, exist_ok=True)

# 경력 ~3년, 지역: 서울/경기
WANTED_FILTER_URL="https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=job.popularity_order&years=0&years=3&locations=seoul.all&locations=gyeonggi.all"
WANTED_DETAIL_PATH="https://www.wanted.co.kr/wd"
WANTED_COMPANY_INFO=os.path.join(PROJECT_PATH, "output","wanted_company_info.txt")