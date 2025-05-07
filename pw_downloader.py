import requests
import os

def download_pw_video(url: str, token: str, quality: str = '720p') -> str:
    """
    Downloads the video from PW using the given token and quality.
    """
    headers = {"Authorization": f"Bearer {token}"}
    video_url = f"https://cdn.study.pw.live/videos/{url}/{quality}.mp4"
    
    response = requests.get(video_url, headers=headers, stream=True)

    if response.status_code == 200:
        file_path = f"downloads/{url}_{quality}.mp4"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return file_path
    return None
