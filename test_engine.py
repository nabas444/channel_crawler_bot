from engine import is_relevant, clean_message

sample_posts = [
    "We are hiring a software engineering internship in Addis Ababa",
    "Bitcoin price is increasing today",
    "Graduate trainee program at bank",
    "Funny meme channel post"
]

for post in sample_posts:
    if is_relevant(post):
        print("\n✅ MATCH:")
        print(clean_message(post))