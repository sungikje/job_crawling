import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from config.config import PROJECT_PATH, WANTED_FILTER_URL, WANTED_COMPANY_INFO


def search_wanted(driver):
    # 원티드 페이지 열기
    driver.get(WANTED_FILTER_URL)

    # 페이지 로딩 대기
    time.sleep(5)

    # 페이지의 끝까지 스크롤 내리기
    scroll_pause_time = 2  # 스크롤 후 대기 시간
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # 스크롤 후 대기
        time.sleep(scroll_pause_time)
        
        # 새로운 높이를 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 새로운 높이가 이전 높이와 같다면 스크롤이 끝난 것
        if new_height == last_height:
            break
        last_height = new_height

    # 직무 정보 수집
    job_links = driver.find_elements(By.CSS_SELECTOR, "a[data-job-category]")  # 'data-job-category' 속성이 있는 <a> 태그 찾기

    info_data = []  # 직무 정보 (회사명, 직무명, 직무 ID)

    for idx, job_link in enumerate(job_links, start=1):
        company_name = job_link.get_attribute("data-company-name")  # 회사 이름
        position_name = job_link.get_attribute("data-position-name")  # 직무명
        position_id = job_link.get_attribute("data-position-id")  # 직무 ID
        
        job_data = {
            "id": idx,
            "company_name": company_name,
            "position_name": position_name,
            "position_id": position_id
        }
        info_data.append(job_data)

        print(f"{info_data[idx-1]['company_name']}, {info_data[idx-1]['position_id']}")

    with open(WANTED_COMPANY_INFO, "w", encoding="utf-8") as txt_file:
        for job in info_data:
            txt_file.write(str(job) + "\n")




# ChromeDriver 설정
driver = webdriver.Chrome()

search_wanted(driver)


# 브라우저 닫기
driver.quit()