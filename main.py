import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Устанавливаем заголовок и фавиконку
st.set_page_config(
    page_title="Анализ данных и сравнение",
    page_icon="📊",
    layout="wide",
)

# Загрузка данных для каждой страны и года
df_kaz14 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kaz14.xlsx")
df_kaz15 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kaz15.xlsx")
df_kaz16 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kaz16.xlsx")
df_kaz17 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kaz17.xlsx")

df_kgz14 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kgz14.xlsx")
df_kgz15 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kgz15.xlsx")
df_kgz16 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kgz16.xlsx")
df_kgz17 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/kgz17.xlsx")

df_tjk14 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/tjk14.xlsx")
df_tjk15 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/tjk15.xlsx")
df_tjk16 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/tjk16.xlsx")
df_tjk17 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/tjk17.xlsx")

df_uzb14 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/uzb14.xlsx")
df_uzb15 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/uzb15.xlsx")
df_uzb16 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/uzb16.xlsx")
df_uzb17 = pd.read_excel("C:/Users/ADMIN/OneDrive/Рабочий стол/uzb17.xlsx")
# Объединение данных в один общий DataFrame
dfs = [df_kaz14, df_kaz15, df_kaz16, df_kaz17,
       df_kgz14, df_kgz15, df_kgz16, df_kgz17,
       df_tjk14, df_tjk15, df_tjk16, df_tjk17,
       df_uzb14, df_uzb15, df_uzb16, df_uzb17]

for i, df in enumerate(dfs):
    country = df.columns[0]  # Имя файла содержит информацию о стране
    df['Страна'] = country

combined_df = pd.concat(dfs)

country_flags = {
     'Казахстан': "flag_kaz.jpg",
     'Кыргызстан': "flag_kgz.webp",
     'Таджикистан': "flag_tjk.webp",
     'Узбекистан': "flag_uzb.png",
}


# Отобразим флаги стран и добавим кнопки для анализа данных по каждой стране
for country, flag_path in country_flags.items():
    st.sidebar.image(flag_path, caption=country, use_column_width=True)
    if st.sidebar.button(f"Анализ данных {country}"):
        st.subheader(f'{country.upper()}: Сравнение F_tot_mod_sev и F_tot_sev')
        st.markdown('Сравнение средних значений F_tot_mod_sev и F_tot_sev по годам.')

        # Создайте графики для каждой страны
        if country == 'Казахстан':
            years = [2014, 2015, 2016, 2017]
            F_tot_mod_sev_data = [0.07470399364185949, 0.043239845487344386, 0.07410125894209195, 0.10554721258685143]
            F_tot_sev_data = [0.006350497954260995, 0.003817208853959072, 0.016271748483839686, 0.020902191916558836]
        elif country == 'Кыргызстан':
            years = [2014, 2015, 2016, 2017]
            F_tot_mod_sev_data = [0.19675139601119712, 0.22023197703571712, 0.20562631043293914, 0.21145583484612496]
            F_tot_sev_data = [0.044372911327137894, 0.04796852385681155, 0.04065799588039921, 0.03906410424456007]

        elif country == 'Таджикистан':
            years = [2014, 2015, 2016, 2017]
            F_tot_mod_sev_data = [0.1367302959512903, 0.1113603385558924, 0.20387140413636218, 0.24254491727991936]
            F_tot_sev_data = [0.033797274145563404, 0.02005530752592039, 0.0705966889114674, 0.08311215502779194]
        elif country == 'Узбекистан':
            years = [2014, 2015, 2016, 2017]
            F_tot_mod_sev_data = [0.1009570476430609, 0.12472939556255395, 0.1046331887031038, 0.16500924388511157]
            F_tot_sev_data = [0.01901274104350718, 0.020876762084646536, 0.015474613904076789, 0.02618446883456733]
        # Добавьте код для других стран, если необходимо

        # Создайте графики
        fig = px.line(x=years, y=[F_tot_mod_sev_data, F_tot_sev_data], labels={'x': 'Год', 'y': 'Значение F_tot'},
                      title=f'{country.upper()}: Сравнение F_tot_mod_sev и F_tot_sev')
        st.plotly_chart(fig)


# Заголовок и описание
st.title("Анализ данных и сравнение")
st.write("Добро пожаловать в наше приложение для анализа и вычислении данных.")



# Данные для сравнения
years = [2014, 2015, 2016, 2017]
countries = ['kaz', 'kgz', 'tjk', 'uzb']

F_tot_mod_sev_data = [
    [0.07470399364185949, 0.043239845487344386, 0.07410125894209195, 0.10554721258685143],
    [0.19675139601119712, 0.22023197703571712, 0.20562631043293914, 0.21145583484612496],
    [0.1367302959512903, 0.1113603385558924, 0.20387140413636218, 0.24254491727991936],
    [0.1009570476430609, 0.12472939556255395, 0.1046331887031038, 0.16500924388511157]
]

F_tot_sev_data = [
    [0.006350497954260995, 0.003817208853959072, 0.016271748483839686, 0.020902191916558836],
    [0.044372911327137894, 0.04796852385681155, 0.04065799588039921, 0.03906410424456007],
    [0.033797274145563404, 0.02005530752592039, 0.0705966889114674, 0.08311215502779194],
    [0.01901274104350718, 0.020876762084646536, 0.015474613904076789, 0.02618446883456733]
]


# Графики средних значений по странам
avg_F_tot_mod_sev_data = [sum(data) / len(data) for data in F_tot_mod_sev_data]
avg_F_tot_sev_data = [sum(data) / len(data) for data in F_tot_sev_data]

st.subheader('Сравнение средних значений F_tot_mod_sev и F_tot_sev по странам')
avg_fig = px.bar(x=countries, y=[avg_F_tot_mod_sev_data, avg_F_tot_sev_data],
                 labels={'x': 'Страна', 'y': 'Среднее значение'},
                 title='Сравнение средних значений F_tot_mod_sev и F_tot_sev по странам')
st.plotly_chart(avg_fig)

# Футер
st.sidebar.text("Разработчик сайта: Сүлейменов Мырзакелді 21-05")
