class ClockIterator:
    def __iter__(self):
        self.hour = 0
        self.minute = 0
        self.switch = "min"
        return self

    def __next__(self):
        if self.switch == "min":
            self.minute = (self.minute + 1) % 60
            if self.minute == 59:
                self.switch = "hour"

        # change hour
        elif self.switch == "hour":
            self.hour = (self.hour + 1) % 24
            self.minute = 0
            self.switch = "min"

        # how to display hours and numbers
        if self.hour < 10:
            hour_display = "0" + str(self.hour)
        else:
            hour_display = str(self.hour)
        if self.minute < 10:
            min_display = "0" + str(self.minute)
        else:
            min_display = str(self.minute)
        return hour_display + ":" + min_display


clock = ClockIterator()
for time in clock:
    print(time)
