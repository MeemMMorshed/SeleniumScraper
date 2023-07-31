import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_URL = "https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  driver.get(YOUTUBE_URL)
  VIDE0_DIV_TAG = 'ytd-video-renderer'
  videos = driver.find_elements(By.TAG_NAME, VIDE0_DIV_TAG)
  return videos

def parse_video(video):
  title_tag = driver.find_element(By.ID, "video-title")
  title = title_tag.text
  url = title_tag.get_attribute("href")

  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element(By.ID, 'description-text').text

  return{
    'Title': title,
    'URL': url,
    'Thumbnail URL': thumbnail_url,
    'Channel Name': channel_name,
    'Description': description
  }

if __name__ == "__main__":
  print("Creating driver")
  driver = get_driver()
  
  print("Fetching page")
  videos = get_videos(driver)
  
  print(f'Found {len(videos)} videos')
  print("Parsing top 10 videos")

  videos_data = [parse_video(video) for video in videos[:10]]
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv("Trending.csv", index = None)