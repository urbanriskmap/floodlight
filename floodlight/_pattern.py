"""Light patterns for FloodLight module - represents states of LED strip"""


class Pattern:
    """LED states at one point in time"""
    def __init__(self, config):
        """Accepts configuration object, returns Patterns object"""

        self.config = config

    def one_pixel(self, id, rgb):
        """Sets a single pixel based on array index and specified color"""
        pixels = [(0, 0, 0)] * self.config['fadecandy']['led_strip_length']
        pixels[id] = rgb
        return (pixels)

    def all_pixels(self, rgb):
        """Set all LEDs to specified color"""
        pixels = ([rgb] * self.config['fadecandy']['led_strip_length'])
        return (pixels)

    def n_pixels(self, n, rgb):
        """Sets n LEDs to specified color, from start of array"""
        pixels = [(0, 0, 0)] * self.config['fadecandy']['led_strip_length']
        for i in range(0,  n):
            pixels[i] = rgb
        return (pixels)

    def error(self):
        """Set the first LED to red"""
        return (self.one_pixel(0, self.config['colors']['red']))

    def online(self):
        """Set the first LED to green"""
        return (self.one_pixel(0, self.config['colors']['green']))

    def new_report(self):
        """Set all LEDs to blue for new report alert"""
        return (self.all_pixels(self.config['colors']['blue']))

    def flood(self, num_reports):
        """Set LEDs to number of reports"""
        return (self.n_pixels(num_reports, self.config['colors']['blue']))
