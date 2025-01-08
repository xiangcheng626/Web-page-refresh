import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 定義需要刷新的網址列表
urls = [
    "https://www.google.com.tw/?hl=zh_TW"
]

# 設定刷新間隔 (秒)
refresh_interval = 60  # 例如 60 秒

# 建立瀏覽器 (這裡以 Chrome 為例，如果路徑沒有放在 PATH，需要自行指定)
driver = webdriver.Chrome()  

def refresh_urls_synchronously(url_list, interval):
    while True:
        # 1. 依序在新標籤頁中打開所有 URL
        for url in url_list:
            driver.execute_script(f"window.open('{url}', '_blank');")
        print("已打開所有標籤頁，停留 10 秒後關閉...")

        # 2. 等待 10 秒
        time.sleep(10)

        # 3. 關閉所有除第一個以外的標籤頁
        handles = driver.window_handles
        main_handle = handles[0]
        for h in handles[1:]:
            driver.switch_to.window(h)
            driver.close()

        # 把焦點切回主頁籤（預防下次執行出錯）
        driver.switch_to.window(main_handle)

        print(f"已關閉所有標籤頁，等待 {interval} 秒後再次刷新...\n")
        time.sleep(interval)

# 執行
refresh_urls_synchronously(urls, refresh_interval)
