import pygame  # Imports Pygame for loading images and managing screen positions.

from pathlib import Path  # Provides tools for building file paths safely.


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        # Store a reference to the game's screen and settings.
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Get a rectangle representing the boundaries of the game window.
        self.screen_rect = ai_game.screen.get_rect()

        # Build the path to the ship image relative to this Python file.
        # This allows the image to be found even if the game is run from another directory.
        image_path = Path(__file__).parent / 'images' / 'ship.bmp'

        # Load the ship image from the specified file.
        self.image = pygame.image.load(str(image_path))

        # Get a rectangle that represents the image's size and position.
        self.rect = self.image.get_rect()

        # Position the ship at the bottom-center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the ship's horizontal position as a float.
        # This allows movement using decimal speeds, such as 1.5 pixels per frame.
        self.x = float(self.rect.x)

        # Movement flags indicate whether the player is holding a movement key.
        # Both are False initially, so the ship starts stationary.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""

        # Move the ship right if the right key is held down.
        # Check the right boundary to prevent the ship from leaving the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Move the ship left if the left key is held down.
        # Check the left boundary to prevent the ship from leaving the screen.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Copy the updated floating-point position into the rectangle.
        # Pygame uses the rectangle to position and draw the ship.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""

        # Draw the ship image at the position stored in its rectangle.
        self.screen.blit(self.image, self.rect)
