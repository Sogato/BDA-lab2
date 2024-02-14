import csv
import datetime
import speedtest


def speedtest_run():
    """Выполнение теста скорости и возврат результатов."""
    # Получаем текущее время и дату для записи времени выполнения теста
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Создаём объект Speedtest и выбираем лучший сервер
    st = speedtest.Speedtest()
    best_server = st.get_best_server()

    # Тестирование скорости загрузки и отдачи
    download_speed = st.download() / 1024 / 1024  # Преобразуем в Mbit/s
    upload_speed = st.upload() / 1024 / 1024  # Преобразуем в Mbit/s
    ping = best_server['latency']

    # Форматируем результаты для записи в CSV
    results = [date_time, f"{ping:.2f} ms", f"{download_speed:.2f} Mbit/s", f"{upload_speed:.2f} Mbit/s"]

    return results


def save_to_csv(data, filename="rpi_data_test"):
    """Сохранение результатов теста в CSV-файл."""
    file_path = f"{filename}.csv"
    file_exists = False

    # Проверяем, существует ли файл, для определения необходимости добавления заголовков
    try:
        with open(file_path, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    # Открываем файл для добавления или создания
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Если файл не существовал, добавляем заголовки
            writer.writerow(['DateTime', 'Ping', 'Download Speed', 'Upload Speed'])
        writer.writerow(data)


# Основной блок выполнения
if __name__ == "__main__":
    for i in range(5):
        results = speedtest_run()
        print(f'Номер теста: {i + 1}')
        for result in results:
            print(result)
        save_to_csv(results)
