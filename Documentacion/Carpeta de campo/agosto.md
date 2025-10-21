
### Semana 1 de agosto

**Objetivo de la semana:**
* Investigar y definir los componentes principales para la impresora 3D, incluyendo la placa base, el display y el firmware.
* Estudiar el funcionamiento del sensor LiDAR y su integración con la Raspberry Pi 4.

**Actividades realizadas:**
* Se investigaron diversas opciones de **placas madre** (`SKR`, `RAMPS`, `MKS`) para impresoras 3D, analizando sus características y compatibilidad con el proyecto.
* Se exploraron diferentes tipos de **displays** para la interfaz de usuario.
* Se llevó a cabo una investigación profunda sobre el **funcionamiento del sensor LiDAR** y su conexión con la **Raspberry Pi 4**.
* Se realizaron pruebas del sensor LiDAR utilizando un código genérico, y al no funcionar, se investigó y adaptó un nuevo código de internet para su correcto funcionamiento.

**Resultados obtenidos:**
* Se identificaron posibles opciones para la placa y el display.
* Se logró hacer funcionar el sensor LiDAR con la Raspberry Pi 4, permitiendo la lectura de datos. 

**Dificultades encontradas:**
* El código inicial para el sensor LiDAR no funcionaba, lo que requirió una investigación y adaptación adicionales para encontrar una solución.
* La gran variedad de placas y displays en el mercado hizo difícil la elección inicial.

**Próximos pasos:**
* Tomar una decisión final sobre la placa madre y el display que se comprarán.
* Comenzar con la investigación y adaptación del firmware (`Klipper`) para la placa seleccionada.

---

### Semana 2 de agosto

**Objetivo de la semana:**
* Decidir y adquirir los componentes clave del proyecto: la placa base y la cama magnética.
* Iniciar el diseño de la estructura del escáner.

**Actividades realizadas:**
* Se finalizó la investigación sobre las placas madre.
* Se investigo y compro la **camas magnéticas**.
* Se comenzó a diseñar la **estructura del escáner en AutoCAD**, basándose en las necesidades del proyecto y las dimensiones de los componentes.
* Se desarmó un extrusor para entender su funcionamiento interno y los componentes que lo integran.
* Se contacto a una metalurgia que fabrique y patrocine la estructura del escaner

**Resultados obtenidos:**
* Se realizó la compra de la placa madre (SKR) y la cama magnética .
* Se completó la primera versión del diseño de la estructura mecánica en AutoCAD.
* Se comprendió mejor el funcionamiento de un extrusor, lo que proporcionó conocimientos útiles para el proyecto.

**Dificultades encontradas:**
* Ajustar el diseño en AutoCAD para que fuera lo más eficiente posible en términos de materiales y funcionalidad.

**Próximos pasos:**
* Concretar una reunion con la metalurgia
* Conseguir el firmware para la placa madre
* Conseguir varillas para el sistema de ejes
---

### Semana 3 de agosto

**Objetivo de la semana:**
* Presentar el diseño de la estructura a la metalúrgica y coordinar su fabricación.
* Continuar con la investigación de los motores para el escáner.
* Conseguir las varillas

**Actividades realizadas:**
* Se realizó una reunión con la metalurgia para explicarles en detalle el plano. Sin embargo, debido a una falta de entendimiento por parte del fabricante, se tuvieron que hacer **correcciones y ajustes** en el diseño.
* Se compraron las varillas enroscadas y lisas
* Se mandaron a cortar a Newton par conseguir las medidas requeridas

**Resultados obtenidos:**
* Se corrigió el diseño de la estructura para que la metalúrgica pudiera entenderlo y fabricarlo correctamente.
* Se adquirieron conocimientos teóricos sobre el funcionamiento de los motores paso a paso.
* Se consiguieron y cortaron las varillas

**Dificultades encontradas:**
* La comunicación con la metalúrgica fue complicada al principio, lo que requirió una segunda reunión para aclarar el diseño.
* No se pudo conseguir una version adecuada de klipper para la SKR por lo que tuvimos que cambiar a Marlin

**Próximos pasos:**
* Esperar a que la metalúrgica fabrique la estructura y luego ir a buscarla.
* Encontar una version compatible de marlin

---

### Semana 4 de agosto

**Objetivo de la semana:**
* Recoger la estructura metálica finalizada.
* Haer funcionr un motor con la pi 4

**Actividades realizadas:**
* Se fue a la metalúrgica a **buscar la estructura del escáner** una vez terminada.
* Se probo el motor de la pi 4 en protoboard
* Se enntro y emepzo a adaptar una version comptible de marlin con la skr

**Resultados obtenidos:**
* Se obtuvo la estructura final, lista para el ensamblaje.
* Los motores no arrancaron.

**Dificultades encontradas:**

**Próximos pasos:**
* En la siguiente etapa, se procederá al **montaje de los componentes electrónicos** (placa, motores, LiDAR) en la estructura.
