class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # -------------------- Screen settings --------------------

        # Set the width of the game window in pixels.
        self.screen_width = 1200

        # Set the height of the game window in pixels.
        self.screen_height = 800

        # Set the background color using an RGB tuple (red, green, blue).
        # Each color value ranges from 0 to 255.
        self.bg_color = (230, 230, 230)

        # -------------------- Ship settings --------------------

        # Set the horizontal movement speed of the player's ship.
        self.ship_speed = 1.5

        # -------------------- Bullet settings --------------------

        # Set how quickly bullets move upward, in pixels per frame.
        self.bullet_speed = 2.0

        # Set the width of each bullet in pixels.
        self.bullet_width = 3

        # Set the height of each bullet in pixels.
        self.bullet_height = 15

        # Set the bullet color using an RGB tuple.
        self.bullet_color = (60, 60, 60)

        # Limit the number of bullets that can be active on the screen.
        self.bullets_allowed = 3
