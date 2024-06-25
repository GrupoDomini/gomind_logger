from typing import Union, Literal
import datetime
import logging
import os

class Logger:
    def __init__(
        self, robot_name: str, filename: Union[str, None] = None, folder: Union[str, None] = "logs"
    ) -> None:
        self.start_time = datetime.datetime.now()
        self.robot_name = robot_name

        if filename:
            if folder:
                self.filename = os.path.join(folder, filename)
                if not os.path.exists(folder):
                    os.makedirs(folder)
            else:
                self.filename = filename
        else:
            current_time = self.start_time.strftime("%d-%m-%Y %Hh%Mm")
            if folder:
                self.filename = os.path.join(folder, f"{self.robot_name}_logs_{current_time}.txt")
                if not os.path.exists(folder):
                    os.makedirs(folder)
            else:
                self.filename = f"{self.robot_name}_logs_{current_time}.txt"

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(robot_name)s - %(message)s")

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
        extra = {'robot_name': self.robot_name}
        self.logger.__getattribute__(type)(message, extra=extra)

    def get_execution_time(self):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time
        return execution_time