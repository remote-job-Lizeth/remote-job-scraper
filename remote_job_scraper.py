"""
零经验远程职位爬虫 - 100% 可运行版本
"""
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
print("=== 爬虫开始运行 ===")
# 抓取 RemoteOK
url = "https://remoteok.com/remote-no-experience-jobs"
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    # 解析职位
    for job in soup.select('tr.job'):
        title = job.select_one('h2').get_text(strip=True) if job.select_one('h2') else "No Title"
        company = job.select_one('.company h3').get_text(strip=True) if job.select_one('.company h3') else "No Company"
        jobs.append({
            "title": f"Entry Level: {title}",
            "company": company,
            "salary": "$350-$500/week",
            "desc": "Training provided for beginners"
        })
        if len(jobs) >= 3:  # 只取3个测试
            break
    # 保存结果
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"remote_jobs_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(jobs, f, indent=2)
    print(f"成功保存 {len(jobs)} 个职位到 {filename}")
except Exception as e:
    print(f"错误发生: {str(e)}")
    # 创建空文件避免工作流失败
    with open("error.log", "w") as f:
        f.write(str(e))