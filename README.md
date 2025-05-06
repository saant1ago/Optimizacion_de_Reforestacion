# 🌳 Optimización del Transporte en la Logística de Reforestación

Este proyecto aborda la optimización de rutas para la reforestación en una línea de transmisión eléctrica en Dominica. El objetivo es diseñar un modelo matemático y una solución heurística para minimizar los tiempos y costos de transporte de plantas a distintos polígonos.

## 📖 Resumen

México enfrenta una alta tasa de deforestación, impactando ecosistemas, biodiversidad y comunidades. Este proyecto desarrolla un modelo que considera la demanda de plantas por polígono, capacidad de transporte, tiempos de viaje y restricciones operativas para optimizar la logística de reforestación.

## 📂 Contenido del proyecto

- 📄 **RetoEtapa3.pdf** → Documento con introducción, modelo matemático, resultados y conclusiones.
- 💻 **Código Python (A\*)** → Implementación de un algoritmo heurístico para encontrar rutas eficientes.
- 📊 **Matriz de costos (Excel)** → Tiempos de viaje entre polígonos.

## ⚙️ Tecnologías y herramientas

- Python 3.12.2
- simpleai 0.8.3
- GAMS (no implementado por limitaciones)
- Excel

## 🚀 Cómo correr el código

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/nombre-del-repo.git
    cd nombre-del-repo
    ```

2. Instala las dependencias:
    ```bash
    pip install simpleai
    ```

3. Corre el script de Python para ejecutar el algoritmo A\*.

4. Consulta el PDF para entender el planteamiento, supuestos, modelo y resultados.

## 📊 Resultados

- Algoritmos probados:
  - A\* (mejor solución: 9 días, 6 horas)
  - Búsqueda en profundidad (10 días)
  - Greedy (10 días)

- Número de nodos visitados: 88  
- Tiempo máximo de ejecución: ~1.7 segundos para 13 polígonos

<img width="486" alt="Image" src="https://github.com/user-attachments/assets/2329e4af-6d55-4144-8827-ebb179c5a452" />
<img width="509" alt="Image" src="https://github.com/user-attachments/assets/c6459f06-b44f-472b-acbd-ac1cfabc3760" />

## 📌 Conclusiones

El uso de A\* permitió encontrar soluciones eficientes dadas las limitaciones computacionales. A futuro, se plantea implementar modelos exactos (GAMS) y considerar transporte con carga sobrante para optimizar aún más las rutas.


## 📎 Recursos

- 📥 [Anexos (código + Excel)](https://drive.google.com/file/d/1Q_p1ApTLg0WZowWjBJYkuG4oktcmYGds/view?usp=sharing)


## 📄 Licencia

MIT

