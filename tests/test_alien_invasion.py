import unittest
from alien_invasion.alien_invasion import AlienInvasion


class TestAlienInvasion(unittest.TestCase):
    def setUp(self):
        """Create an instance of the game for testing."""
        self.ai = AlienInvasion()

    def test_initial_settings(self):
        """Test the initial settings of the game."""
        self.assertEqual(self.ai.settings.screen_width, 1200)
        self.assertEqual(self.ai.settings.screen_height, 800)
        self.assertEqual(self.ai.settings.bg_color, (230, 230, 230))

    def test_ship_initial_position(self):
        """Test the initial position of the ship."""
        self.assertEqual(self.ai.ship.rect.midbottom, self.ai.screen.get_rect().midbottom)

    def test_bullet_creation(self):
        """Test bullet creation and update."""
        initial_bullet_count = len(self.ai.bullets)
        self.ai._fire_bullet()
        self.assertEqual(len(self.ai.bullets), initial_bullet_count + 1)
        bullet = self.ai.bullets.sprites()[0]
        initial_y = bullet.rect.y
        bullet.update()
        self.assertNotEqual(bullet.rect.y, initial_y)

    def test_alien_creation(self):
        """Test alien creation and update."""
        self.ai._create_fleet()
        self.assertGreater(len(self.ai.aliens), 0)
        alien = self.ai.aliens.sprites()[0]
        initial_x = alien.rect.x
        alien.update()
        self.assertNotEqual(alien.rect.x, initial_x)

    def test_scoreboard_update(self):
        """Test scoreboard update."""
        initial_score = self.ai.stats.score
        self.ai.stats.score += 10
        self.ai.scoreboard.prep_score()
        self.assertNotEqual(self.ai.scoreboard.score_image, None)

if __name__ == '__main__':
    unittest.main()