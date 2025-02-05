import json
import os
import xml.etree.ElementTree as ET

def create_collada_model(polygon, output_path):
    collada = ET.Element('COLLADA', version='1.4.1')

    asset = ET.SubElement(collada, 'asset')
    ET.SubElement(asset, 'unit', name='meter', meter='1.0')
    ET.SubElement(asset, 'up_axis').text = 'Z_UP'

    library_geometries = ET.SubElement(collada, 'library_geometries')
    geometry = ET.SubElement(library_geometries, 'geometry', id='geometry_1', name='geometry_1')
    mesh = ET.SubElement(geometry, 'mesh')

    # Converter coordenadas absolutas para relativas
    min_x = min(p[0] for p in polygon)
    min_y = min(p[1] for p in polygon)
    relative_polygon = [(x - min_x, y - min_y, z) for x, y, z in polygon]

    # Definindo os vértices
    positions = [f"{x} {y} {z}" for x, y, z in relative_polygon]
    positions_text = " ".join(positions)
    source = ET.SubElement(mesh, 'source', id='position_source')
    float_array = ET.SubElement(source, 'float_array', id='position_array', count=str(len(relative_polygon) * 3))
    float_array.text = positions_text

    technique_common = ET.SubElement(source, 'technique_common')
    accessor = ET.SubElement(technique_common, 'accessor', source='#position_array', count=str(len(relative_polygon)), stride='3')
    ET.SubElement(accessor, 'param', name='X', type='float')
    ET.SubElement(accessor, 'param', name='Y', type='float')
    ET.SubElement(accessor, 'param', name='Z', type='float')

    vertices = ET.SubElement(mesh, 'vertices', id='vertices')
    ET.SubElement(vertices, 'input', semantic='POSITION', source='#position_source')

    # Definindo os índices para criar um polígono
    triangles = ET.SubElement(mesh, 'triangles', count=str(len(relative_polygon) - 2))
    ET.SubElement(triangles, 'input', semantic='VERTEX', source='#vertices', offset='0')
    indices = []
    for i in range(1, len(relative_polygon) - 1):
        indices.extend([0, i, i + 1])
    ET.SubElement(triangles, 'p').text = " ".join(map(str, indices))

    # Adicionando cena visual
    library_visual_scenes = ET.SubElement(collada, 'library_visual_scenes')
    visual_scene = ET.SubElement(library_visual_scenes, 'visual_scene', id='Scene', name='Scene')
    node = ET.SubElement(visual_scene, 'node', id='node_1', name='geometry_1')
    ET.SubElement(node, 'instance_geometry', url='#geometry_1')

    scene = ET.SubElement(collada, 'scene')
    ET.SubElement(scene, 'instance_visual_scene', url='#Scene')

    tree = ET.ElementTree(collada)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

def process_json_file(json_file, output_directory):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for item in data:
        setor = item['setor']
        quadra = item['quadra']
        lote = item['lote']
        polygon = item['polygon']

        filename = f"setor_{setor}_quadra_{quadra}_lote_{lote}.dae"
        output_path = os.path.join(output_directory, filename)

        create_collada_model(polygon, output_path)
        print(f"Arquivo gerado: {output_path}")

# Caminho do arquivo JSON e diretório de saída
json_file = 'resultados.json'
output_directory = 'output_dae'

process_json_file(json_file, output_directory)