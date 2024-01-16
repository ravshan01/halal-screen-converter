class InvalidPercentageError(Exception):
    def __init__(self, percentage):
        self.percentage = percentage

        super().__init__(
            f"Invalid percentage: {percentage}, should be between 0 and 100"
        )
