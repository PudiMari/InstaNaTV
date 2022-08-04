from instaloader import Instaloader, Profile

L=Instaloader()

PROFILE = "kt.cardosos"
profile =Profile.from_username(L.context, PROFILE)
post_sorted = sorted(profile.get_posts(),key=lambda post: post.likes, reverse=True)

for post in post_sorted:
    L.download_post(post,PROFILE)