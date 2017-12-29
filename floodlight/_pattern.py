"""Light patterns for FloodLight module - represents states of LED strip"""


class Pattern:
    """LED states at one point in time"""
    def __init__(self, config):
        """Accepts configuration object, returns Patterns object"""

        self.config = config

    def error(self):
        """Set the first LED to red"""
        pixels = [(0, 0, 0)] * self.config['fadecandy']['led_strip_length']
        pixels[0] = self.config['colors']['red']
        return (pixels)

    def online(self):
        """Set the first LED to green"""
        pixels = [(0, 0, 0)] * self.config['fadecandy']['led_strip_length']
        pixels[0] = self.config['colors']['green']
        return (pixels)

    def new_report(self):
        """Set all LEDs to blue for new report alert"""
        pixels = [(self.config['colors']['blue'])] * self.config['fadecandy']['led_strip_length']
        return (pixels)

    def flood(self, num_reports):
        """Set LEDs to number of reports"""
        pixels = [(0, 0, 0)] * self.config['fadecandy']['led_strip_length']
        for i in range(0,  num_reports):
            pixels[i] = tuple(self.config['colors']['blue'])
        return (pixels)
