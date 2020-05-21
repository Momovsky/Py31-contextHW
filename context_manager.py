from datetime import datetime


class open_time_log():
    def __init__(self, file_path, log_path):
        self.log_path = log_path
        self.file_path = file_path

    def __enter__(self):
        self.start_time = datetime.now()
        self.file = open(self.file_path, 'r', encoding='utf-8')
        self.log = open(self.log_path, 'a', encoding='utf-8')
        self.log.write(f'Время начала работы программы: {datetime.utcnow()}')
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.log.write(f'Время завершения работы программы: {datetime.utcnow()}')
        self.log.write(f'Время, затраченное на выполнение программы: {datetime.now() - self.start_time}')
        self.log.close()