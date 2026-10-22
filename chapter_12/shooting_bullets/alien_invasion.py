import sys  # Provides functions for interacting with the Python runtime, including exiting the game.

import pygame  # Imports Pygame, which is used to create and run the game.

# Import the classes needed to configure and manage the game.
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()  # Initialize all imported Pygame modules.
        self.clock = pygame.time.Clock()  # Controls the game's frame rate.
        self.settings = Settings()  # Load the game's screen, ship, and bullet settings.

        # Create the game window using the configured screen dimensions.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the title displayed at the top of the game window.
        pygame.display.set_caption("Alien Invasion")

        # Create the player's ship and a group to store all active bullets.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""

        # Keep the game running until the player closes it or quits.
        while True:
            self._check_events()  # Check for keyboard input and window events.
            self.ship.update()  # Update the ship's position.
            self._update_bullets()  # Move bullets and remove bullets off-screen.
            self._update_screen()  # Redraw the game window.
            self.clock.tick(60)  # Limit the game to approximately 60 frames per second.

    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # Retrieve all events that have occurred since the previous check.
        for event in pygame.event.get():

            # Exit the game when the window's close button is clicked.
            if event.type == pygame.QUIT:
                sys.exit()

            # Handle a key that has been pressed down.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # Handle a key that has been released.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        # Start moving the ship to the right when the right arrow is pressed.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        # Start moving the ship to the left when the left arrow is pressed.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # Quit the game when the Q key is pressed.
        elif event.key == pygame.K_q:
            sys.exit()

        # Fire a bullet when the spacebar is pressed.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        # Stop moving right when the right arrow is released.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        # Stop moving left when the left arrow is released.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

        # Only create a bullet if the number of active bullets is below the limit.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)  # Create a bullet at the ship's current position.
            self.bullets.add(new_bullet)  # Add the bullet to the group for updating and drawing.

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        # Update the position of every bullet in the group.
        self.bullets.update()

        # Use a copy of the group so bullets can safely be removed while iterating.
        for bullet in self.bullets.copy():

            # Remove a bullet when its bottom edge reaches the top of the screen.
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Clear the previous frame by filling the screen with the background color.
        self.screen.fill(self.settings.bg_color)

        # Draw each active bullet onto the screen.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the player's ship at its current position.
        self.ship.blitme()

        # Display the newly drawn frame.
        pygame.display.flip()


# Run this section only when this file is executed directly.
if __name__ == '__main__':

    # Create an instance of the AlienInvasion class.
    ai = AlienInvasion()

    # Start the game's main loop.
    ai.run_game()
