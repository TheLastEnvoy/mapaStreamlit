import streamlit as st
import geopandas as gpd
import folium
import requests
import zipfile
import io

# URLs dos arquivos shapefile no GitHub (com permalinks)
bandeirantes_url = 'https://github.com/seu_usuario/seu_repositorio/raw/versao_arquivos/bandeirantesDashboard.zip'
perimetro_url = 'https://github.com/TheLastEnvoy/mapaStreamlit/blob/635b3f171d80097385127ca7e9bffae0e0469580/shpsBandeirantes.zip'

# Função para carregar e exibir o mapa a partir de um arquivo shapefile
def show_map(shapefile_url):
    # Faz o download e extrai o arquivo shapefile
    response = requests.get(shapefile_url)
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        zip_ref.extractall('temp')

    # Carrega o arquivo shapefile
    gdf = gpd.read_file('temp/bandeirantesDashboard.shp')

    # Cria um mapa básico com o Folium
    m = folium.Map(location=[-25.4284, -49.2733], zoom_start=12)

    # Adiciona as geometrias do shapefile ao mapa
    for idx, row in gdf.iterrows():
        folium.GeoJson(row['geometry']).add_to(m)

    # Exibe o mapa no Streamlit
    st.write(m)

# Título da página
st.title('Mapa Interativo')

# Seção para exibir o mapa
st.header('Mapa de Bandeirantes')
show_map(bandeirantes_url)

st.header('Perímetro de Bandeirantes')
show_map(perimetro_url)
