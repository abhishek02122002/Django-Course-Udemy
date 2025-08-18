from datetime import date
from django.shortcuts import render, get_object_or_404

# ==============================
# POSTS DATA
# ==============================
posts = [
    {
        "slug": "hike-in-mountain",
        "image": "woods.jpg",
        "author": "Abhishek",
        "date": date(2025, 8, 13),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like mountain hiking",
        "content": """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris. Nisi ut aliquip ex ea commodo
            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
            cillum dolore. Eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
            non proident. Sunt in culpa qui officia deserunt mollit anim id est laborum.
            Praesent sapien massa, convallis a pellentesque nec, egestas non nisi.
            Curabitur arcu erat, accumsan id imperdiet et, porttitor at sem.
        """
    },
    {
        "slug": "adventure-in-forest",
        "image": "woods.jpg",
        "author": "Abhishek",
        "date": date(2025, 8, 10),
        "title": "Forest Adventure",
        "excerpt": "Exploring the green wilderness is pure joy",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
        """
    },
    {
        "slug": "sunset-on-beach",
        "image": "woods.jpg",
        "author": "Abhishek",
        "date": date(2025, 8, 8),
        "title": "Beach Sunset",
        "excerpt": "Watching the sun meet the sea is magical",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
        """
    },
    {
        "slug": "desert-camping",
        "image": "woods.jpg",
        "author": "Abhishek",
        "date": date(2025, 8, 5),
        "title": "Desert Camping",
        "excerpt": "The desert has a beauty of its own",
        "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
        """
    }
]

# ==============================
# HELPER FUNCTION
# ==============================
def get_post_date(post):
    return post["date"]

# ==============================
# VIEWS
# ==============================
def starting_page(request):
    latest_posts = sorted(posts, key=get_post_date, reverse=True)[:3]
    return render(request, "myblog/index.html", {
        "posts": latest_posts
    })

def all_posts(request):
    ordered_posts = sorted(posts, key=get_post_date, reverse=True)
    return render(request, "myblog/all-posts.html", {
        "all_posts": ordered_posts
    })

def post_details(request, slug):
     identified_post = next(post for post in posts if post['slug'] == slug)
     return render(request, "myblog/post-details.html", {
        "post": identified_post
    })
