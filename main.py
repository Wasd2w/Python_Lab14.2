import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('input_file.csv')

def plot_country_data(country1, country2):
    plt.figure(figsize=(11, 7))

    country1_data = data[data['Country Name'] == country1]
    country2_data = data[data['Country Name'] == country2]

    plt.plot(country1_data['Year'], country1_data['Indicator Value'], label=country1, marker='o')

    plt.plot(country2_data['Year'], country2_data['Indicator Value'], label=country2, marker='o')

    plt.title('Динаміка показника за останні роки')
    plt.xlabel('Рік')
    plt.ylabel('Значення показника')
    plt.legend()
    plt.grid(True)

    plt.show()

def plot_bar_chart(country):
    plt.figure(figsize=(8, 5))

    country_data = data[data['Country Name'] == country]

    plt.bar(country_data['Year'], country_data['Indicator Value'], color='skyblue')

    plt.title(f'Значення показника для {country}')
    plt.xlabel('Рік')
    plt.ylabel('Значення показника')
    plt.grid(axis='y')

    plt.show()

country1 = input('Введіть назву першої країни: ')
country2 = input('Введіть назву другої країни: ')

plot_country_data(country1, country2)

selected_country = input('Введіть назву країни для побудови стовпчастої діаграми: ')

plot_bar_chart(selected_country)
