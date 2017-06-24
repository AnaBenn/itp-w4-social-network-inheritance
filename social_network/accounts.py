
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []
    
    def add_post(self, post):
        post.user = self    
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for follow in self.following:
            for post in follow.posts:
                timeline.append(post)
        return sorted(timeline, key=lambda post: post.timestamp, reverse=False)
        #  sorted(time, key=lambda student: student.age)
        #sort by timestamp when done with posts.py  https://wiki.python.org/moin/HowTo/Sorting  THANKS :)

    def follow(self, other):
        #users you are following
        self.following.append(other)


# [User1post, user1post2, user2post, user3post, user3post2]
# [[user1post, user1post2], [user2post], ]
