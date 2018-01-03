"""Control a Fadecany LED Strip"""


class Pixel:
    """Manipulate individual LED states"""
    def __init__(self, led_strip_length):
        """Accepts configuration object, returns Pixel object"""
        self.led_strip_length = led_strip_length

    def all(self, rgb):
        """Set all LEDs in the strip to specified color"""
        pixels = ([rgb] * self.led_strip_length)
        return (pixels)

    def one(self, pixels, id, rgb):
        """Sets a single pixel based on array index and specified color"""
        pixels[id] = rgb
        return (pixels)

    def span(self, pixels, n, rgb):
        """Sets n LEDs from start of array to specified color"""
        for i in range(0,  n):
            pixels[i] = rgb
        return (pixels)
