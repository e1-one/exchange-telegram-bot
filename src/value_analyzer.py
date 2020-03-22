import threading
import logging
from helper.tables_finance_page_parser import get_data_for_date_from_cache


class ChangeAnalyzer:

    def __init__(self) -> None:
        super().__init__()
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def analyze_avg_task(self):
        threading.Timer(300.0, self.analyze_avg_task).start()
        logging.info(f"analyze_avg_task ")
        for listener in self.listeners:
            listener.send_message(f"For now, avg val is: {get_data_for_date_from_cache().avg_rate}")
