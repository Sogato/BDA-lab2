import pandas as pd


def load_data(file_path, column_names):
    """Загрузка исходных данных из CSV файла."""
    # Загрузка данных с указанием названий столбцов
    df = pd.read_csv(file_path, names=column_names)
    return df


def transform_data(df):
    """Преобразование данных для уменьшения избыточности."""
    # Переименование столбцов для более понятного представления
    df_renamed = df.rename(columns={
        'Measure A': 'Ping (ms)',
        'Measure B': 'Download (Mbit/s)',
        'Measure C': 'Upload (Mbit/s)'
    })

    # Удаление ненужных столбцов
    df_reduced = df_renamed.drop(['Type A', 'Type B', 'Type C', 'Units A', 'Units B', 'Units C'], axis=1)

    # Добавление столбцов с датой и временем
    df_reduced['Date'] = pd.to_datetime(df_reduced['Datetime']).dt.date
    df_reduced['Time'] = pd.to_datetime(df_reduced['Datetime']).dt.time

    return df_reduced


def save_data(df, file_path):
    """Сохранение преобразованных данных в новый CSV файл."""
    df.to_csv(file_path, index=False)


# Основная часть программы
if __name__ == "__main__":
    data_file = 'rpi_data_long.csv'
    column_names = ['Type A', 'Measure A', 'Units A', 'Type B', 'Measure B', 'Units B', 'Type C', 'Measure C',
                    'Units C', 'Datetime']

    # Загрузка исходных данных
    df_initial = load_data(data_file, column_names)
    print("Исходные данные:")
    print(df_initial.head())  # Вывод первых пяти строк исходного набора данных

    # Преобразование данных
    df_compact = transform_data(df_initial)
    print("\nПреобразованные данные:")
    print(df_compact.head())  # Вывод первых пяти строк преобразованного набора данных

    # Сохранение преобразованных данных
    save_data(df_compact, 'rpi_data_compact.csv')

    # Вывод типов данных для демонстрации
    print("\nПример типов данных в преобразованных данных:")
    print(f"Дата первой записи: {df_compact['Date'][0]}, тип: {type(df_compact['Date'][0])}")
    print(f"Время первой записи: {df_compact['Time'][0]}, тип: {type(df_compact['Time'][0])}")
