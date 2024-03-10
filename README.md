# projeto_Analise_Cobertura_Solo
Análise de Cobertura do Solo


tecnologias pesquisadas até o momento

NASA Earthdata

Google Earth Engine


analizar o tipo do solo selecionado







# Análise de Cobertura do Solo com Imagens de Satélite Sentinel-2

## Descrição

Este projeto tem como objetivo analisar a cobertura do solo em uma área definida utilizando imagens de satélite do Sentinel-2. A análise foca em classificar diferentes tipos de cobertura do solo, como áreas urbanas, corpos d'água, florestas e terras agrícolas, e em identificar mudanças na cobertura do solo ao longo do tempo. Utilizamos o Google Earth Engine para acessar e processar imagens de satélite, aplicando técnicas de processamento de imagens e aprendizado de máquina para a classificação da cobertura do solo.

## Recursos e Tecnologias

-   **Google Earth Engine**: Plataforma de processamento geoespacial que permite visualizar e analisar imagens de satélite.
-   **Python**: Linguagem de programação utilizada para scripting e análise de dados.
-   **Folium**: Biblioteca Python para visualização de dados geoespaciais interativos em um mapa.
-   **Earth Engine Python API**: API utilizada para acessar o Google Earth Engine a partir de scripts Python.

## Metodologia

1.  **Definição da Área de Interesse (AOI)**: Escolhemos uma área específica para a análise, utilizando coordenadas geográficas para definir a AOI.
2.  **Coleta de Dados**: Acessamos imagens de satélite do Sentinel-2 correspondentes à nossa AOI e ao período de estudo, filtrando imagens com baixa cobertura de nuvens.
3.  **Pré-processamento**: Aplicamos técnicas de pré-processamento nas imagens selecionadas para melhorar a qualidade dos dados para análise.
4.  **Classificação da Cobertura do Solo**: Utilizamos algoritmos de aprendizado de máquina para classificar os pixels das imagens em categorias de cobertura do solo.
5.  **Análise de Mudanças**: Comparamos imagens de diferentes períodos para identificar mudanças na cobertura do solo ao longo do tempo.
6.  **Visualização dos Resultados**: Criamos mapas interativos utilizando a biblioteca Folium para visualizar a distribuição da cobertura do solo e as áreas de mudança.

## Resultados

Apresentamos os resultados da classificação da cobertura do solo, destacando as principais categorias identificadas e as áreas onde foram observadas mudanças significativas na cobertura do solo ao longo do período estudado. Os mapas interativos gerados oferecem uma visualização clara da distribuição espacial da cobertura do solo e das mudanças ocorridas.

## Conclusão

Este projeto demonstra o poder do processamento de imagens de satélite e da análise geoespacial para entender a dinâmica da cobertura do solo em uma região. Os insights gerados podem ser valiosos para estudos ambientais, planejamento urbano, e gestão de recursos naturais.