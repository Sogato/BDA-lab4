import pandas as pd
import matplotlib.pyplot as plt


def load_and_prepare_data(filepath):
    """Загрузка данных и их первичная подготовка."""
    data = pd.read_csv(filepath)
    print("Первые 5 записей в данных:")
    print(data.head())
    print("\nПоследние 5 записей в данных:")
    print(data.tail())
    print("\nОписательная статистика данных:")
    print(data.describe())

    # Округление веса до 2 знаков после запятой и добавление в новый столбец
    data['rounded'] = data.weight.round(2)
    print("\nДанные после округления веса (первые 5 записей):")
    print(data.head())

    # Вычисление разницы между округленным весом и 20, добавление в новый столбец
    data['diff'] = data['rounded'] - 20
    print("\nДанные после добавления разницы (первые 5 записей):")
    print(data.head())

    return data


def analyze_data(data):
    """Анализ данных и вывод основных статистик."""
    # Вычисление основных статистик
    count = data['rounded'].count()
    mean = data['rounded'].mean()
    median = data['rounded'].median()
    std = data['rounded'].std()
    rng = data['rounded'].max() - data['rounded'].min()

    # Форматирование строк для вывода
    countstring = "\nВ данных {} записей.".format(count)
    meanstring = "Среднее значение распределения {:.2f}, а медиана {:.2f}.".format(mean, median)
    stdstring = "Стандартное отклонение распределения {:.2f}.".format(std)
    rangestring = "Минимальное значение {:.2f}, максимальное значение {:.2f}, размах {:.2f}.".format(
        data['rounded'].min(), data['rounded'].max(), rng)

    print(countstring)
    print(meanstring)
    print(stdstring)
    print(rangestring)


def plot_data(data):
    """Визуализация данных."""
    freq = data['rounded'].value_counts().to_frame().reset_index()
    freq.columns = ['value', 'freq']

    # Создание графика
    plt.figure(figsize=(12, 8))  # Уменьшил размер графика для лучшей читаемости
    plt.scatter(freq.value, freq.freq, color='blue', alpha=0.7, edgecolors='black', s=50)  # Изменил тип и цвет точек, добавил черные края
    plt.title('Распределение веса', fontsize=16)  # Добавил заголовок и изменил размер шрифта
    plt.xlabel('Вес', fontsize=14)  # Добавил метку оси X и изменил размер шрифта
    plt.ylabel('Частота', fontsize=14)  # Добавил метку оси Y и изменил размер шрифта
    plt.grid(True)  # Добавил сетку для лучшей ориентации
    plt.xticks(fontsize=12)  # Изменил размер шрифта меток по оси X
    plt.yticks(fontsize=12)  # Изменил размер шрифта меток по оси Y
    plt.tight_layout()  # Улучшил компактность размещения элементов на графике

    # Сохранение графика в файл
    plt.savefig('weight_distribution.png')


# Основной блок
if __name__ == "__main__":
    filepath = "rpi_describe.csv"
    data = load_and_prepare_data(filepath)
    analyze_data(data)
    plot_data(data)
