from typing import Union, Literal


class Logger:
    def __init__(
        self, filename: Union[str, None] = None, folder: Union[str, None] = "logs"
    ) -> None:
        import datetime
        import logging
        import os

        if filename:
            if folder:
                self.filename = os.path.join(folder, filename)
                if not os.path.exists(folder):
                    os.makedirs(folder)
            else:
                self.filename = filename
        else:
            current_time = datetime.datetime.now().strftime("%d-%m-%Y %Hh%Mm")
            if folder:
                self.filename = os.path.join(folder, f"process_logs_{current_time}.txt")
                if not os.path.exists(folder):
                    os.makedirs(folder)
            else:
                self.filename = f"process_logs_{current_time}.txt"

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(self.filename, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log(
        self,
        message: str,
        type: Literal["debug", "info", "warning", "error", "critical"] = "info",
    ):
        self.logger.__getattribute__(type)(message)
