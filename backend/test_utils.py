class Method:
    def __init__(self, mocked_func):
        self.mocked_func = mocked_func
        self.mock_calls = mocked_func.mock_calls

    def was_called_with(self, *args):
        for call in self.mock_calls:
            if len(call) < 2:
                continue
            if len(call[1]) < 1:
                continue
            if call[1] == args:
                return True
        raise AssertionError(
            f"No call to {self.mocked_func} with args {args}:\n {self.mock_calls}"
        )
