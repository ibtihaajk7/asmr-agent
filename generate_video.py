from pexels_utils import search_pexels_video, download_video

# Choose video type based on the voice script or audio background
video_type = "ocean"  # you can vary this dynamically later
video_url = search_pexels_video(query=video_type, duration=30)
download_video(video_url)
