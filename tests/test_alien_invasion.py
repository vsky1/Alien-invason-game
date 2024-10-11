import unittest
from alien_invasion import AlienInvasion

class TestAlienInvasion(unittest.TestCase):
    def setUp(self):
        """Create an instance of the game for testing."""
        self.ai = AlienInvasion()

    def test_initial_settings(self):
        """Test the initial settings of the game."""
        self.assertEqual(self.ai.settings.screen_width, 1200)
        self.assertEqual(self.ai.settings.screen_height, 800)
        self.assertEqual(self.ai.settings.bg_color, (0, 0, 255))

    def test_ship_initial_position(self):
        """Test the initial position of the ship."""
        self.assertEqual(self.ai.ship.rect.midbottom, (self.ai.screen.get_rect().midbottom))

if __name__ == '__main__':
    unittest.main()