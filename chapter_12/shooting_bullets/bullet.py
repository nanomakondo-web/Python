import pygame  # Imports Pygame for creating rectangles and drawing bullets.
from pygame.sprite import Sprite  # Imports Sprite, the base class for game objects.


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""

        super().__init__()  # Initialize the parent Sprite class.

        # Access the game's screen and settings through the main game object.
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Store the color that will be used to draw the bullet.
        self.color = self.settings.bullet_color

        # Create a rectangular area representing the bullet.
        # Its initial position is (0, 0), with the configured width and height.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        # Position the bullet at the top-center of the player's ship.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's vertical position as a float for precise movement.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""

        # Decrease the vertical position to move the bullet upward.
        self.y -= self.settings.bullet_speed

        # Update the rectangle's vertical position for drawing and collision checks.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""

        # Draw a filled rectangle using the bullet's color and position.
        pygame.draw.rect(self.screen, self.color, self.rect)