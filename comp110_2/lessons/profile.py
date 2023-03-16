"""Examples of a class & objects."""

class Profile:
    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str):
        """Constructor initializes attributes!"""
        self.handle = handle
        self.followers = 0
        self.is_private = False

    def tweet(self, message: str) -> None:
        """An example of a method."""
        print(f"@{self.handle} tweets {message}")


my_profile: Profile = Profile("michael_fehl")
my_profile.tweet("Hello, world.")