class LoggableList(list, Loggable):
    def append(self, element):
        super().append(element)
        self.log(element)

