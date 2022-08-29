from instaloader import Instaloader, Profile
from datetime import datetime, timedelta

data_inicio = datetime.today() - timedelta(days=14)
L=Instaloader()

PROFILE = "ifmtcuiabaoficial"
profile = Profile.from_username(L.context, PROFILE)
post_sorted = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

for post in post_sorted:
    if post.date > data_inicio:
        if post.is_video:
            L.download_videos(post,PROFILE)
        else:
            L.download_pictures(post,PROFILE)