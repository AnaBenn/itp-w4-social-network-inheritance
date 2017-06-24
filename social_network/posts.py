from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = 'Saturday, Jun 24, 2017'
        self.text = text
        self.user = None
        
        
    def set_user(self, user):
        self.user = user

class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
    
    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime('%A, %b %d, %Y'))

# self.assertEqual(
#             str(post1),
#             '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'
#         )
#         self.assertEqual(
#             str(post2),
#             '@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'
#         )
#         self.assertEqual(
#             str(post3),
#             '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
#         )


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp) # __init__ from (parent) Post init
        self.image_url = image_url
        

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))


"""
John Lennon: "Check my new guitar"
  Pic URL: imgur.com/guitar.png
  Friday, Feb 03, 2017
"""

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        
    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp.strftime('%A, %b %d, %Y'))

"""
John Checked In: "At Abbey Road Studios"
  19.111, -9.2222
  Friday, Feb 03, 2017
"""