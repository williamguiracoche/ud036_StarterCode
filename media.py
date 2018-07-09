""" Defining the Movie class

In this file, we create the Movie() class.Import media.py to access to create
Movie instances.

"""

import webbrowser


class Movie():
    """ Movie Class.

    This class allows you to define a movie and store its title,
    poster image link and youtube trailer link. An instance contains a movie
    title (string), the poster image url (string) and a youtube url (string).

    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Creates title(str), image url(str) and video url(str) attributes."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Uses webbrowser to open the youtube movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
