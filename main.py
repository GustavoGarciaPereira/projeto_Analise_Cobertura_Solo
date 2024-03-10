import ee  # Importa a Earth Engine Python API
import folium  # Para visualização de mapas

import os

project = os.getenv('PROJECT')


# print(project)
# Inicializa a biblioteca.
ee.Authenticate()
ee.Initialize(project=project)

# Define a área de interesse (AOI) com uma caixa de delimitação.
# Exemplo: Latitude e Longitude do centro do Rio de Janeiro, Brasil.
latitude = -30.16630791380963
longitude = -53.568136475533386
aoi = ee.Geometry.Point(longitude, latitude).buffer(10)  # Buffer de 10km ao redor do ponto central.

# Define o período de observação.
inicio = '2023-01-01'
fim = '2023-01-31'

# Carrega a coleção de imagens do Sentinel-2.
sentinel_images = ee.ImageCollection('COPERNICUS/S2') \
    .filterBounds(aoi) \
    .filterDate(ee.Date(inicio), ee.Date(fim)) \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))  # Filtra imagens com menos de 20% de cobertura de nuvens.

# Seleciona a imagem com menor cobertura de nuvens.
image = sentinel_images.sort('CLOUDY_PIXEL_PERCENTAGE').first()

# Função para adicionar a camada ao mapa.
def add_ee_layer(self, ee_image_object, vis_params, name):
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles=map_id_dict['tile_fetcher'].url_format,
        attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name=name,
        overlay=True,
        control=True
    ).add_to(self)

# Adiciona o método ao folium.
folium.Map.add_ee_layer = add_ee_layer

# Define os parâmetros de visualização para imagens do Sentinel-2.
vis_params = {
    'min': 0,
    'max': 3000,
    'bands': ['B4', 'B3', 'B2']
}

# Cria um mapa Folium centrado na AOI.
map = folium.Map(location=[latitude, longitude], zoom_start=10)
map.add_ee_layer(image, vis_params, 'Imagem Sentinel-2')

# Adiciona um controle de camadas ao mapa.
map.add_child(folium.LayerControl())

# Mostra o mapa.
map
map.save('mapa_sentinel.html')
map.show_in_browser()