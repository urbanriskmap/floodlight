"""Construct sequences of light patterns"""
from _pattern import Pattern


class Sequence():
    """Build light event sequences using Pattern class"""
    def __init__(self, config):
        """Accpets config returns Sequence class"""
        self.config = config
        self.pattern = Pattern(config)

    def online(self):
        """Returns online sequence"""
        # heartbeat
        sequence = [{'pattern': self.pattern.online(), 'timing': 0.1}]
        sequence.append({'pattern': self.pattern.online(), 'timing': 0})
        return (sequence)

    def error(self):
        return ([{'pattern': self.pattern.error(), 'timing': 0}])

    def flood(self, count):
        # heartbeat
        sequence = [{'pattern': self.pattern.online(), 'timing': 0.1}]
        sequence.append({'pattern': self.pattern.report_count(count), 'timing': 0})
        return (sequence)

    def new_report(self, last_count, new_count):
        """Flash all LEDs blue to alert new incoming report"""
        # Get raindrop from pattern
        sequence = []
        sequence.append({'pattern': self.pattern.all_blue(), 'timing': 2})
        sequence.append({'pattern': self.pattern.report_count(new_count), 'timing': 0})
        #sequence = raindrop(last_count, new_count)
        #sequence.append({'pattern': self.pattern.one_pixel()})
        return sequence

    def new_report_2(self, last_count, new_count):
        """Flash LEDs representing new reports"""
        # First, raindrop animation
        sequence = self.raindrop(last_count, new_count)
        # Next, show the old count
        sequence.append(self.report_count(last_count))
        # Now grow the LED count from the old value to the new one
        for i in range(last_count, new_count):
            sequence.append(self.append({'pattern': self.pattern.report_count(i), 'timing':0.5}))
        return (sequence)

    def raindrop(self, last_count, new_count):
        """Animate LEDs as falling raindrop"""
        sequence = []
        for i in range(self.config['fadecandy']['led_strip_length']-1, -1, -1):
            sequence.append({'pattern': self.pattern.raindrop(i), 'timing': 0.3})
        return (sequence)

    def build(self, last_count, new_count):
        """Accepts previous and new report counts, returns light sequence"""

        # Logic to set sequence based on latest report count
        if new_count == 0:
            return (self.online())
        elif new_count > last_count:
            self.raindrop(last_count, new_count)
            return (self.new_report(last_count, new_count))
        elif new_count > 0:
            return (self.flood(new_count))
        else:
            return (self.error())
