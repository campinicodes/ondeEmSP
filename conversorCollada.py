import collada
import numpy as np
import json

# JSON de exemplo
json_data = [
    [
                -46.7442958348371,
                -23.4946250714703,
                0.0
            ],
            [
                -46.7441915232143,
                -23.494654792321,
                0.0
            ],
            [
                -46.7439329435241,
                -23.494729584241,
                0.0
            ],
            [
                -46.7438732112987,
                -23.4947438340586,
                0.0
            ],
            [
                -46.7438266886229,
                -23.4947559855029,
                0.0
            ],
            [
                -46.743722652134,
                -23.4947865427606,
                0.0
            ],
            [
                -46.743701380519,
                -23.4947927858215,
                0.0
            ],
            [
                -46.743674726054,
                -23.4948029088275,
                0.0
            ],
            [
                -46.7435664174965,
                -23.494828014521,
                0.0
            ],
            [
                -46.7435692684807,
                -23.4948370848692,
                0.0
            ],
            [
                -46.7435128139856,
                -23.4948504309852,
                0.0
            ],
            [
                -46.7434842626502,
                -23.4948473552436,
                0.0
            ],
            [
                -46.7434150700321,
                -23.4948532406124,
                0.0
            ],
            [
                -46.7434166712668,
                -23.4948774592605,
                0.0
            ],
            [
                -46.7434170622141,
                -23.494883360517,
                0.0
            ],
            [
                -46.7433566170286,
                -23.4948992435243,
                0.0
            ],
            [
                -46.7433580158459,
                -23.4949080772879,
                0.0
            ],
            [
                -46.7432975885263,
                -23.4949171333794,
                0.0
            ],
            [
                -46.7432935196358,
                -23.4948988389459,
                0.0
            ],
            [
                -46.7432581549681,
                -23.4949070095414,
                0.0
            ],
            [
                -46.7432297793031,
                -23.4949135668174,
                0.0
            ],
            [
                -46.7431711537462,
                -23.4949271086775,
                0.0
            ],
            [
                -46.7431710475568,
                -23.4949279677176,
                0.0
            ],
            [
                -46.7431412588889,
                -23.4949394982695,
                0.0
            ],
            [
                -46.7430916662533,
                -23.4949586911468,
                0.0
            ],
            [
                -46.7430932889248,
                -23.4949391410592,
                0.0
            ],
            [
                -46.743015434351,
                -23.4949512094079,
                0.0
            ],
            [
                -46.7430099088969,
                -23.4950439914682,
                0.0
            ],
            [
                -46.742971099559,
                -23.4950478300137,
                0.0
            ],
            [
                -46.7429729621719,
                -23.4949735733853,
                0.0
            ],
            [
                -46.7429254664843,
                -23.4949854555237,
                0.0
            ],
            [
                -46.7428861983587,
                -23.4949946088319,
                0.0
            ],
            [
                -46.7428771402844,
                -23.4949967238684,
                0.0
            ],
            [
                -46.7428751294884,
                -23.4949971888361,
                0.0
            ],
            [
                -46.7428372466989,
                -23.4950059654324,
                0.0
            ],
            [
                -46.7428439189687,
                -23.4950234451427,
                0.0
            ],
            [
                -46.7428165542775,
                -23.4950287087722,
                0.0
            ],
            [
                -46.7428115242576,
                -23.495029640958,
                0.0
            ],
            [
                -46.7427559691142,
                -23.4950399155683,
                0.0
            ],
            [
                -46.7427554802242,
                -23.4950384762345,
                0.0
            ],
            [
                -46.7427548279355,
                -23.4950365240175,
                0.0
            ],
            [
                -46.7427542270874,
                -23.4950347608554,
                0.0
            ],
            [
                -46.7427045639922,
                -23.4950478591382,
                0.0
            ],
            [
                -46.7426919170675,
                -23.4950510527646,
                0.0
            ],
            [
                -46.7426612461185,
                -23.4950587824292,
                0.0
            ],
            [
                -46.7425659250894,
                -23.4950828030351,
                0.0
            ],
            [
                -46.7425171900047,
                -23.4950979768138,
                0.0
            ],
            [
                -46.7424730591221,
                -23.4951118529349,
                0.0
            ],
            [
                -46.7424219858153,
                -23.4951249307839,
                0.0
            ],
            [
                -46.7424165602398,
                -23.4951263098527,
                0.0
            ],
            [
                -46.7423767374213,
                -23.4951364715725,
                0.0
            ],
            [
                -46.7422847087747,
                -23.495159958535,
                0.0
            ],
            [
                -46.7422939298429,
                -23.4951866203871,
                0.0
            ],
            [
                -46.7422479588422,
                -23.4951990541637,
                0.0
            ],
            [
                -46.7422408975472,
                -23.4951802784526,
                0.0
            ],
            [
                -46.7421944784774,
                -23.4951913988415,
                0.0
            ],
            [
                -46.7422037829423,
                -23.4952169581043,
                0.0
            ],
            [
                -46.7421069220374,
                -23.4952422779227,
                0.0
            ],
            [
                -46.742098098569,
                -23.4952153226511,
                0.0
            ],
            [
                -46.7420521691239,
                -23.495227196045,
                0.0
            ],
            [
                -46.7420041906582,
                -23.4952396070504,
                0.0
            ],
            [
                -46.742017369209,
                -23.4952805733715,
                0.0
            ],
            [
                -46.7420188086269,
                -23.4952850542262,
                0.0
            ],
            [
                -46.7419720714992,
                -23.4952987968145,
                0.0
            ],
            [
                -46.7419694035337,
                -23.4952924695128,
                0.0
            ],
            [
                -46.7419226011329,
                -23.4953057161653,
                0.0
            ],
            [
                -46.7418773594511,
                -23.4953185209417,
                0.0
            ],
            [
                -46.7418289037471,
                -23.4953326168157,
                0.0
            ],
            [
                -46.7418179718469,
                -23.4952986958635,
                0.0
            ],
            [
                -46.741718616217,
                -23.4953278991606,
                0.0
            ],
            [
                -46.741704191301,
                -23.4953321420109,
                0.0
            ],
            [
                -46.7416233959475,
                -23.4953558912896,
                0.0
            ],
            [
                -46.7416341720044,
                -23.4953898772099,
                0.0
            ],
            [
                -46.7416018887916,
                -23.49539860897,
                0.0
            ],
            [
                -46.7415871764102,
                -23.4954025841232,
                0.0
            ],
            [
                -46.7415353417428,
                -23.4954166002946,
                0.0
            ],
            [
                -46.7414362054116,
                -23.4954483474333,
                0.0
            ],
            [
                -46.7414157092424,
                -23.4954540126314,
                0.0
            ],
            [
                -46.7413724338828,
                -23.4954659554922,
                0.0
            ],
            [
                -46.7413418796828,
                -23.4954743879415,
                0.0
            ],
            [
                -46.7412891903672,
                -23.4954889373284,
                0.0
            ],
            [
                -46.7412416323683,
                -23.4955020658081,
                0.0
            ],
            [
                -46.7412383252571,
                -23.4955029786863,
                0.0
            ],
            [
                -46.7411904550528,
                -23.4955161919109,
                0.0
            ],
            [
                -46.7411577157041,
                -23.4955252357009,
                0.0
            ],
            [
                -46.7411427702442,
                -23.4955293578988,
                0.0
            ],
            [
                -46.7410953780408,
                -23.4955424393319,
                0.0
            ],
            [
                -46.7410454787188,
                -23.4955562169936,
                0.0
            ],
            [
                -46.741036818041,
                -23.4955349306896,
                0.0
            ],
            [
                -46.7409876605147,
                -23.495549277964,
                0.0
            ],
            [
                -46.7409892120937,
                -23.4955541007169,
                0.0
            ],
            [
                -46.7409390371698,
                -23.4955670235729,
                0.0
            ],
            [
                -46.7409384331898,
                -23.4955672560735,
                0.0
            ],
            [
                -46.7409180040105,
                -23.4955750425152,
                0.0
            ],
            [
                -46.7409175169107,
                -23.4955752285594,
                0.0
            ],
            [
                -46.7409027487073,
                -23.4955809199784,
                0.0
            ],
            [
                -46.7408821258697,
                -23.4955888711202,
                0.0
            ],
            [
                -46.7408485760117,
                -23.4956018068158,
                0.0
            ],
            [
                -46.7408519460302,
                -23.495610898511,
                0.0
            ],
            [
                -46.7408076713711,
                -23.495625037653,
                0.0
            ],
            [
                -46.7407274582001,
                -23.4956506491914,
                0.0
            ],
            [
                -46.7405969257526,
                -23.4956893837129,
                0.0
            ],
            [
                -46.7405829558781,
                -23.4956932421171,
                0.0
            ],
            [
                -46.7404185175847,
                -23.4957386944165,
                0.0
            ],
            [
                -46.7402652965754,
                -23.4957854118576,
                0.0
            ],
            [
                -46.7400374859584,
                -23.4958520789116,
                0.0
            ],
            [
                -46.7398608874593,
                -23.4959035359881,
                0.0
            ],
            [
                -46.7393380880831,
                -23.4960486895458,
                0.0
            ],
            [
                -46.7393832158549,
                -23.4960741560239,
                0.0
            ],
            [
                -46.7395372640855,
                -23.4961142629476,
                0.0
            ],
            [
                -46.7397223256725,
                -23.4961421037168,
                0.0
            ],
            [
                -46.7398802929872,
                -23.4961585439688,
                0.0
            ],
            [
                -46.7400374823163,
                -23.4961709111763,
                0.0
            ],
            [
                -46.7400491064096,
                -23.4961718288156,
                0.0
            ],
            [
                -46.7401913860352,
                -23.4961746461015,
                0.0
            ],
            [
                -46.740295085832,
                -23.4961742100192,
                0.0
            ],
            [
                -46.7403421180875,
                -23.4961769353842,
                0.0
            ],
            [
                -46.7403812935614,
                -23.4961837939661,
                0.0
            ],
            [
                -46.7404157382535,
                -23.4961942451638,
                0.0
            ],
            [
                -46.7404556797286,
                -23.4962117144792,
                0.0
            ],
            [
                -46.7404842479762,
                -23.496234692754,
                0.0
            ],
            [
                -46.7405022096451,
                -23.496248497636,
                0.0
            ],
            [
                -46.740528186585,
                -23.4962821602857,
                0.0
            ],
            [
                -46.7405813590455,
                -23.4962641111201,
                0.0
            ],
            [
                -46.7405910382686,
                -23.4962608243977,
                0.0
            ],
            [
                -46.7405993820231,
                -23.4962579860383,
                0.0
            ],
            [
                -46.7406058543773,
                -23.4962557916611,
                0.0
            ],
            [
                -46.7406096266639,
                -23.4962545123965,
                0.0
            ],
            [
                -46.7406397072963,
                -23.4962442974274,
                0.0
            ],
            [
                -46.7406423098241,
                -23.496243410494,
                0.0
            ],
            [
                -46.7406531393416,
                -23.4962397406834,
                0.0
            ],
            [
                -46.7406759678953,
                -23.4962319906702,
                0.0
            ],
            [
                -46.740702383442,
                -23.4962230176377,
                0.0
            ],
            [
                -46.7407249585301,
                -23.4962153517202,
                0.0
            ],
            [
                -46.7407266448771,
                -23.4962147820443,
                0.0
            ],
            [
                -46.7407373845603,
                -23.4962117272735,
                0.0
            ],
            [
                -46.7407768704458,
                -23.4962004770851,
                0.0
            ],
            [
                -46.7408248915251,
                -23.4961868017575,
                0.0
            ],
            [
                -46.7408264522686,
                -23.4961863599048,
                0.0
            ],
            [
                -46.7408347070767,
                -23.4961834593169,
                0.0
            ],
            [
                -46.7408557584288,
                -23.4961760722801,
                0.0
            ],
            [
                -46.7408759228494,
                -23.4961689931432,
                0.0
            ],
            [
                -46.7409263245795,
                -23.4961534183532,
                0.0
            ],
            [
                -46.7409744600934,
                -23.4961385443208,
                0.0
            ],
            [
                -46.7409782435856,
                -23.4961373732826,
                0.0
            ],
            [
                -46.740979953228,
                -23.4961423026287,
                0.0
            ],
            [
                -46.7409806857116,
                -23.496144398438,
                0.0
            ],
            [
                -46.7410836164278,
                -23.4961144964275,
                0.0
            ],
            [
                -46.7411343063504,
                -23.4960997707853,
                0.0
            ],
            [
                -46.7411508291092,
                -23.4960949717636,
                0.0
            ],
            [
                -46.7411741598916,
                -23.4960881913088,
                0.0
            ],
            [
                -46.7411799828567,
                -23.4960865008183,
                0.0
            ],
            [
                -46.7412681073864,
                -23.4960608999361,
                0.0
            ],
            [
                -46.7412870490266,
                -23.4960553966103,
                0.0
            ],
            [
                -46.7412881902429,
                -23.4960550678027,
                0.0
            ],
            [
                -46.7413211650127,
                -23.4960460484383,
                0.0
            ],
            [
                -46.741394363319,
                -23.4960260413816,
                0.0
            ],
            [
                -46.7414482938388,
                -23.4960113065041,
                0.0
            ],
            [
                -46.7414594614934,
                -23.4960080392101,
                0.0
            ],
            [
                -46.741485532523,
                -23.4960004244041,
                0.0
            ],
            [
                -46.7414929549013,
                -23.4959982554905,
                0.0
            ],
            [
                -46.7415299009613,
                -23.4959874579218,
                0.0
            ],
            [
                -46.7415989065746,
                -23.4959672899543,
                0.0
            ],
            [
                -46.7416001842484,
                -23.4959669144688,
                0.0
            ],
            [
                -46.7417014044711,
                -23.4959372569364,
                0.0
            ],
            [
                -46.7417027113941,
                -23.495936872093,
                0.0
            ],
            [
                -46.7417528278611,
                -23.495922477748,
                0.0
            ],
            [
                -46.7418048074577,
                -23.4959075568737,
                0.0
            ],
            [
                -46.7418466817125,
                -23.4958955302248,
                0.0
            ],
            [
                -46.7418528564862,
                -23.4958937906261,
                0.0
            ],
            [
                -46.7418618016163,
                -23.4958912705576,
                0.0
            ],
            [
                -46.7418746097244,
                -23.4958876688408,
                0.0
            ],
            [
                -46.7419056007045,
                -23.4958789424395,
                0.0
            ],
            [
                -46.7419588813124,
                -23.495863934727,
                0.0
            ],
            [
                -46.7419662949527,
                -23.4958618471596,
                0.0
            ],
            [
                -46.7419766349858,
                -23.4958589322254,
                0.0
            ],
            [
                -46.742007284507,
                -23.495850299923,
                0.0
            ],
            [
                -46.7420382754679,
                -23.4958415734963,
                0.0
            ],
            [
                -46.7420557072696,
                -23.4958366648855,
                0.0
            ],
            [
                -46.7420981893709,
                -23.4958247036136,
                0.0
            ],
            [
                -46.7421121484662,
                -23.4958207729552,
                0.0
            ],
            [
                -46.7421109465408,
                -23.4958172285684,
                0.0
            ],
            [
                -46.7421411357633,
                -23.4958093328199,
                0.0
            ],
            [
                -46.7421584647392,
                -23.4958047955788,
                0.0
            ],
            [
                -46.7421635385184,
                -23.4958034656023,
                0.0
            ],
            [
                -46.7421696174063,
                -23.4958018805739,
                0.0
            ],
            [
                -46.742194059507,
                -23.4957954848632,
                0.0
            ],
            [
                -46.7422159841169,
                -23.4957897403759,
                0.0
            ],
            [
                -46.7422425923486,
                -23.4957827786304,
                0.0
            ],
            [
                -46.7422823437579,
                -23.4957723829539,
                0.0
            ],
            [
                -46.7423014635259,
                -23.4957655410731,
                0.0
            ],
            [
                -46.7423191123169,
                -23.4957577765202,
                0.0
            ],
            [
                -46.7423210105753,
                -23.4957569425868,
                0.0
            ],
            [
                -46.7423812268015,
                -23.495739987947,
                0.0
            ],
            [
                -46.7424220602375,
                -23.4957284875008,
                0.0
            ],
            [
                -46.7425240366438,
                -23.495699778174,
                0.0
            ],
            [
                -46.7425253925088,
                -23.4956993927765,
                0.0
            ],
            [
                -46.7426254986731,
                -23.4956714176774,
                0.0
            ],
            [
                -46.7426414969591,
                -23.4956669494501,
                0.0
            ],
            [
                -46.7426552807586,
                -23.4956630929456,
                0.0
            ],
            [
                -46.7426737567739,
                -23.4956579287758,
                0.0
            ],
            [
                -46.7426961641584,
                -23.495651673141,
                0.0
            ],
            [
                -46.7427183470959,
                -23.4956454741941,
                0.0
            ],
            [
                -46.7427286580803,
                -23.4956425866265,
                0.0
            ],
            [
                -46.7427297799474,
                -23.4956422760852,
                0.0
            ],
            [
                -46.7427895393993,
                -23.4956255882727,
                0.0
            ],
            [
                -46.74285678097,
                -23.4956068120632,
                0.0
            ],
            [
                -46.7429459907789,
                -23.4955818934295,
                0.0
            ],
            [
                -46.7429469562515,
                -23.4955816026966,
                0.0
            ],
            [
                -46.7432147777418,
                -23.4955021126175,
                0.0
            ],
            [
                -46.7434790303021,
                -23.495425985082,
                0.0
            ],
            [
                -46.7439732882947,
                -23.4952805956636,
                0.0
            ],
            [
                -46.7440572721111,
                -23.4952558884285,
                0.0
            ],
            [
                -46.7444011878457,
                -23.4951578997763,
                0.0
            ],
            [
                -46.7446950149727,
                -23.4950741789339,
                0.0
            ],
            [
                -46.7448494137762,
                -23.4950315978555,
                0.0
            ],
            [
                -46.7448228926058,
                -23.4949983032598,
                0.0
            ],
            [
                -46.7448092157388,
                -23.4949708607266,
                0.0
            ],
            [
                -46.7447901982742,
                -23.4949244788601,
                0.0
            ],
            [
                -46.7447798062265,
                -23.4948907146432,
                0.0
            ],
            [
                -46.7447660777732,
                -23.4948296087923,
                0.0
            ],
            [
                -46.7447616979216,
                -23.4947944046739,
                0.0
            ],
            [
                -46.7447593983798,
                -23.4947387333048,
                0.0
            ],
            [
                -46.7447589172021,
                -23.4946843418915,
                0.0
            ],
            [
                -46.7447598805503,
                -23.4946385308723,
                0.0
            ],
            [
                -46.7447645966842,
                -23.494586248452,
                0.0
            ],
            [
                -46.7447750948366,
                -23.4945150466038,
                0.0
            ],
            [
                -46.7447409594825,
                -23.4944923843214,
                0.0
            ],
            [
                -46.7444464593901,
                -23.494582153808,
                0.0
            ],
            [
                -46.7442958348371,
                -23.4946250714703,
                0.0
            ]
    # ... Adicione todos os pontos do JSON aqui
]

# Converter JSON para numpy array
vertices_geo = np.array(json_data, dtype=np.float32)

# Normalizar para coordenadas relativas
min_long = vertices_geo[:, 0].min()  # Menor longitude
min_lat = vertices_geo[:, 1].min()   # Menor latitude
vertices_rel = vertices_geo.copy()
vertices_rel[:, 0] -= min_long  # Ajustar longitude
vertices_rel[:, 1] -= min_lat   # Ajustar latitude

# Converter para o formato 1D esperado
vertices_flat = vertices_rel.flatten()

# Gerar índices para os triângulos (exemplo simples para polígonos convexos)
indices = []
for i in range(1, len(json_data) - 1):
    indices.extend([0, i, i + 1])
indices = np.array(indices, dtype=np.int32)

# Criar a malha COLLADA
mesh = collada.Collada()

# Criar um material básico
effect = collada.material.Effect("effect0", [], "phong", diffuse=(0.0, 0.5, 1.0))
material = collada.material.Material("material0", "MyMaterial", effect)
mesh.materials.append(material)

# Fonte de vértices
vert_src = collada.source.FloatSource("verts-array", vertices_flat, ('X', 'Y', 'Z'))
geom = collada.geometry.Geometry(mesh, "geometry0", "MyGeometry", [vert_src])

# Lista de inputs para os vértices
input_list = collada.source.InputList()
input_list.addInput(0, 'VERTEX', "#verts-array")

# Criar o conjunto de triângulos
triset = geom.createTriangleSet(indices, input_list, "materialref")
geom.primitives.append(triset)

# Adicionar a geometria à malha
mesh.geometries.append(geom)

# Criar um nó para a cena
matnode = collada.scene.MaterialNode("materialref", material, inputs=[])
geomnode = collada.scene.GeometryNode(geom, [matnode])
node = collada.scene.Node("node0", children=[geomnode])

# Adicionar o nó à cena principal
myscene = collada.scene.Scene("myscene", [node])
mesh.scenes.append(myscene)
mesh.scene = myscene

# Salvar o arquivo DAE
mesh.write("TESTEZAO.dae")
print("Arquivo DAE gerado com sucesso!")
