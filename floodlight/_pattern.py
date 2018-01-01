"""Light patterns for FloodLight module"""

from _pixel import Pixel


class Pattern(Pixel):
    """Inherits Pixel class to create LED patterns"""
    def __init__(self, config):
        """Accepts configuration object, returns Patterns object"""
        self.config = config
        Pixel.__init__(self, self.config['fadecandy']['led_strip_length'])

    def error(self):
        """Set the first LED to red, clear all others"""
        pixels = self.all((0, 0, 0))
        return (self.one(pixels, 0, self.config['colors']['red']))

    def online(self):
        """Set the first LED to green, clear all others"""
        pixels = self.all((0, 0, 0))
        return (self.one(pixels, 0, self.config['colors']['green']))

    def all_blue(self):
        """Set all LEDs to blue for new report alert"""
        return (self.all(self.config['colors']['blue']))

    def report_count(self, num_reports):
        """Set LEDs to number of reports"""
        pixels = self.all((0, 0, 0))
        return (self.span(pixels, num_reports, self.config['colors']['blue']))

    def raindrop(self, n):
        """Set a single LED as blue, with all others off"""
        pixels = self.all((0, 0, 0))
        self.one(pixels, n, self.config['colors']['blue'])
        return (pixels)
