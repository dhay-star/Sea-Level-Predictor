import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sea_level_predictor

class TestSeaLevelPredictor(unittest.TestCase):
    def test_plot_exists(self):
        # Call the draw_plot function
        ax = sea_level_predictor.draw_plot()

        # Check that something was plotted
        self.assertTrue(len(ax.lines) >= 2, "There should be at least two lines plotted (for the two regressions).")

    def test_labels_and_title(self):
        ax = sea_level_predictor.draw_plot()
        self.assertEqual(ax.get_xlabel(), "Year", "X-axis label should be 'Year'")
        self.assertEqual(ax.get_ylabel(), "Sea Level (inches)", "Y-axis label should be 'Sea Level (inches)'")
        self.assertEqual(ax.get_title(), "Rise in Sea Level", "Title should be 'Rise in Sea Level'")

if __name__ == "__main__":
    unittest.main()
