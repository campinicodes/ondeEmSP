import * as THREE from 'three';
import { ColladaLoader } from 'three/addons/loaders/ColladaLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let container = document.getElementById("container");
let scene, camera, renderer, controls;
let modelsLoaded = 0; // Contador de modelos carregados
let modelPaths = []; // Para armazenar os caminhos dos modelos carregados
let terreno = null;

function calculateArea(geometry) {
    let area = 0;
    const vertices = geometry.attributes.position.array;
    
    // Supondo que a geometria seja um polígono simples (convexo)
    for (let i = 0; i < vertices.length; i += 9) {
        // Cria 3 vértices de cada triângulo
        const x1 = vertices[i], y1 = vertices[i + 1], z1 = vertices[i + 2];
        const x2 = vertices[i + 3], y2 = vertices[i + 4], z2 = vertices[i + 5];
        const x3 = vertices[i + 6], y3 = vertices[i + 7], z3 = vertices[i + 8];

        // Calcular a área do triângulo usando a fórmula de área de um triângulo no espaço 3D
        const a = new THREE.Vector3(x1, y1, z1);
        const b = new THREE.Vector3(x2, y2, z2);
        const c = new THREE.Vector3(x3, y3, z3);

        const ab = new THREE.Vector3().subVectors(b, a);
        const ac = new THREE.Vector3().subVectors(c, a);
        const crossProduct = new THREE.Vector3().crossVectors(ab, ac);

        area += crossProduct.length() / 2;
    }
    return area;
}

function init() {
    scene = new THREE.Scene();

    // Ajuste da câmera para ocupar toda a tela
    const aspect = window.innerWidth / window.innerHeight;
    camera = new THREE.PerspectiveCamera(75, aspect, 0.1, 1000);
    camera.position.set(10, 10, 10);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor(0xffffff, 1);
    renderer.shadowMap.enabled = false;
    container.appendChild(renderer.domElement);

    const ambientLight = new THREE.AmbientLight(0x808080);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(10, 10, 10).normalize();
    scene.add(directionalLight);

    controls = new OrbitControls(camera, renderer.domElement);

    window.addEventListener('resize', onWindowResize, false);

    animate();
}

function onWindowResize() {
    const width = window.innerWidth;
    const height = window.innerHeight;
    
    camera.aspect = width / height;
    camera.updateProjectionMatrix();

    renderer.setSize(width, height);
}

function carregarTerreno(nomeArquivoDAE) {
    const caminhoDAE = `static/models/${nomeArquivoDAE}`;

    const loader = new ColladaLoader();
    loader.load(caminhoDAE, function (collada) {
        terreno = collada.scene;
        terreno.rotation.x = Math.PI;

        // Centralizar o terreno
        const box = new THREE.Box3().setFromObject(terreno);
        const center = box.getCenter(new THREE.Vector3());
        terreno.position.sub(center);

        // Ajustar a escala do terreno
        const terrenoBox = new THREE.Box3().setFromObject(terreno);
        const size = terrenoBox.getSize(new THREE.Vector3());
        const maxSize = Math.max(size.x, size.y, size.z);
        const scale = 10 / maxSize;  // Ajuste para que o maior modelo ocupe a tela
        terreno.scale.set(scale, scale, scale);

        // Definir cor azul para o terreno
        terreno.traverse((child) => {
            if (child.isMesh) {
                child.material = new THREE.MeshPhongMaterial({ color: 0x3498db });
            }
        });

        scene.add(terreno);
        console.log("Terreno carregado.");
    });
}

function loadModel(url, modelNumber) {
    const loader = new ColladaLoader();
    loader.load(url, function (collada) {
        const model = collada.scene;

        // Centralizar o modelo
        const box = new THREE.Box3().setFromObject(model);
        const center = box.getCenter(new THREE.Vector3());
        model.position.sub(center); // Centraliza o modelo no ponto (0,0,0)

        // Ajustar a escala do modelo
        const modelBox = new THREE.Box3().setFromObject(model);
        const size = modelBox.getSize(new THREE.Vector3());
        const maxSize = Math.max(size.x, size.y, size.z);
        const scale = 10 / maxSize;  // Ajuste para que o maior modelo ocupe a tela
        model.scale.set(scale, scale, scale);

        // Aplicar cor diferente para cada modelo
        model.traverse((child) => {
            if (child.isMesh) {
                child.material = new THREE.MeshPhongMaterial({
                    color: modelNumber === 1 ? 0x3498db : 0xe74c3c, // Azul ou vermelho
                });

                // Calcular e exibir a área do modelo
                const area = calculateArea(child.geometry);
                console.log(`Área do modelo ${modelNumber}: ${area.toFixed(2)} unidades quadradas`);
                
                document.getElementById('area').textContent = area.toFixed(2) + "m²";
            }
        });

        scene.add(model);
        console.log(`Modelo ${modelNumber} carregado e centralizado.`);

        modelsLoaded++;
        if (modelsLoaded === 2) {
            console.log("Ambos os modelos carregados. Inicializando visualizador.");
            animate();
        }
    });
}

function carregarEdificacao(file) {
    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error("Erro no upload:", data.error);
                return;
            }

            const loader = new ColladaLoader();
            const caminhoDAE = `static/models/${data.filename}`;

            loader.load(caminhoDAE, function (collada) {
                const edificacao = collada.scene;

                // Centralizar
                const box = new THREE.Box3().setFromObject(edificacao);
                const centerEdificacao = box.getCenter(new THREE.Vector3());
                edificacao.position.sub(centerEdificacao);

                // Ajustar a escala para que a edificação fique proporcional ao terreno

                // Centralizar a edificação sobre o terreno
                if (terreno) {
                    const terrenoBox = new THREE.Box3().setFromObject(terreno);
                    const edificacaoBox = new THREE.Box3().setFromObject(edificacao);

                    // Calcular o centro do terreno e centralizar a edificação
                    const centroTerreno = terrenoBox.getCenter(new THREE.Vector3());
                    const centroEdificacao = edificacaoBox.getCenter(new THREE.Vector3());

                    // Ajustar a posição da edificação
                    edificacao.position.set(
                        centroTerreno.x - centroEdificacao.x,
                        edificacao.position.y, // Não queremos mudar a altura
                        centroTerreno.z - centroEdificacao.z
                    );
                }

                // Aplicar cor vermelha para a edificação
                edificacao.traverse((child) => {
                    if (child.isMesh) {
                        child.material = new THREE.MeshPhongMaterial({ color: 0xe74c3c });
                    }
                });

                scene.add(edificacao);
                console.log("Edificação carregada e centralizada.");
            });
        })
        .catch(error => console.error("Erro ao enviar o arquivo:", error));
}


function handleUpload() {
    const fileInput = document.getElementById("uploadEdificacao");
    if (fileInput.files.length > 0) {
        carregarEdificacao(fileInput.files[0]);
    } else {
        console.log("Nenhum arquivo selecionado.");
    }
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

window.carregarTerreno = carregarTerreno;
window.handleUpload = handleUpload;

init();
