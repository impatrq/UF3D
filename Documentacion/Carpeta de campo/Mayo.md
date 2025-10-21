
### Semana 1 de mayo

**Objetivo de la semana:**
* Definir los materiales clave para la plantilla ortopédica y buscar la colaboración de especialistas.
* Iniciar el diseño conceptual del proyecto, incluyendo el escáner y la adquisición del microcontrolador principal.

**Actividades realizadas:**
* Se investigaron y analizaron diversos **materiales de amortiguación** para la plantilla, decidiéndose finalmente por la **Goma Eva** debido a sus propiedades y viabilidad. También se investigaron métodos de sujeción.
* Se contactó y se reunió con un **médico especialista** que brindó asesoramiento crucial sobre **plantillas ortopédicas**, sus beneficios y las principales causas de su necesidad, enriqueciendo la base teórica del proyecto.
* Se comenzó a investigar la adquisición del microcontrolador principal, la **Raspberry Pi 4 (Pi 4)**. Inicialmente se buscó de segunda mano, pero el alto precio dificultó la compra. Finalmente, se gestionó un **préstamo de una Pi 4** por parte del colegio.
* Se contactó a un **potencial socio** para el proyecto, pero las negociaciones no llegaron a concretarse.

**Resultados obtenidos:**
* Se definió la **Goma Eva** como el material principal de amortiguación.
* Se obtuvo **información médica especializada** fundamental para el diseño.
* Se consiguió una **Raspberry Pi 4 prestada**, solucionando el problema del microcontrolador.

**Dificultades encontradas:**
* La dificultad para conseguir la Raspberry Pi 4 a un precio accesible.

**Próximos pasos:**
* Iniciar el trabajo con la Raspberry Pi 4.
* Enfocarse en la adquisición y diseño de la estructura del escáner.

---

### Semana 2 de mayo

**Objetivo de la semana:**
* Asegurar el hardware de la impresora 3D  mediante un patrocinio.
* Iniciar la programación y la simulación del prototipo.

**Actividades realizadas:**
* Se contactó a una **empresa** que ofreció colaborar, proporcionándonos una **impresora 3D en mal estado** para que la restableciéramos y usáramos.
* Se visitó la empresa para formalizar el **acuerdo de colaboración**, comprometiéndonos a **publicitar** su marca a cambio del uso de la impresora.
* Se **creó contenido para redes sociales** junto a la empresa y el médico, cumpliendo con los primeros compromisos de publicidad.
* Se investigaron los **lenguajes y tecnologías** necesarios para la programación de la plantilla y el procesamiento de datos.
* Se creó un **programa prototipo inicial** para la generación del modelo 3D de la plantilla.

**Resultados obtenidos:**
* Se aseguró una **impresora 3D** para el proyecto.
* Se **inició la fase de programación** con la creación del programa prototipo.

**Dificultades encontradas:**
* Coordinación inicial de la colaboración y el contenido publicitario.

**Próximos pasos:**
* Retirar la impresora dañada.
* Integrar la Raspberry Pi 4 y simular los datos de escaneo.

---

### Semana 3 de mayo

**Objetivo de la semana:**
* Integrar el microcontrolador y el software prototipo.
* Iniciar el diagnóstico de la estructura del escáner (Kinect) y los sensores de presión.

**Actividades realizadas:**
* Se logró **acceder a la terminal de la Raspberry Pi 4**, permitiendo empezar a trabajar en el entorno de desarrollo.
* Se **simularon datos** de los futuros **sensores de presión** y la **Kinect futura** en un algoritmo.
* Se probó el algoritmo de simulación con el programa prototipo creado anteriormente, buscando simular el proceso de creación de la plantilla de principio a fin.
* Se realizaron las primeras investigaciones para encontrar el sensor de escaneo, identificando a la **Kinect** como la opción inicial, y se buscaron **precios de segunda mano**.
* Se empezó a analizar el **diseño y la estructura de la impresora casera** prestada para determinar sus medidas, materiales y detalles para su reparación y uso.
* Se creó una **lista de componentes** de repuesto necesarios para la impresora.

**Resultados obtenidos:**
* La Raspberry Pi 4 quedó lista para el trabajo.
* Se consiguió la **simulación inicial de todo el proceso de la plantilla** (del escaneo a la generación del modelo 3D).

**Dificultades encontradas:**
* Surgieron **problemas con el algoritmo prototipo de prueba** y su integración con los datos simulados.

**Próximos pasos:**
* Definir la estructura general del proyecto.
* Enfocarse en el diagnóstico de la Kinect y el diseño del circuito de sensores.

---

### Semana 4 de mayo

**Objetivo de la semana:**
* Finalizar la adquisición del hardware inicial y resolver los problemas de diseño de sensores.
* Definir la estructura electrónica del escáner.

**Actividades realizadas:**
* Se fue a **retirar la impresora 3D dañada** que había proporcionado la empresa colaboradora.
* Se analizó y discutió la **estructura general del proyecto**, buscando soluciones a los problemas detectados y definiendo posibles caminos a seguir.
* Se investigó y analizó la **portabilidad** general que debía tener el producto final.
* Se realizaron investigaciones para el **esquemático** de la placa electrónica del escáner.
* Se encontraron serias **dificultades para encontrar una Kinect**, ya que estaban descontinuadas y escaseaban. Además, se identificó la necesidad de un **adaptador** específico, lo cual complicaba aún más la adquisición.
* Se investigó la **ubicación de los sensores de presión**, ya que se encontró que podían **tapar la visión de la Kinect** durante el escaneo. Se propuso una solución inicial: **dividir el escaneo del pie y la toma de datos de presión en dos etapas separadas**.
* Se investigó el posible uso de un **multiplexor**, dada la potencial gran cantidad de entradas de sensores de presión, para poder leerlos todos con una única salida.
* Se analizó el **diseño inicial de la caja donde se apoyaría el pie**, detallando materiales, componentes y cómo se ensamblaría como prototipo.

**Resultados obtenidos:**
* Se obtuvo el **hardware principal de fabricación** (impresora dañada).
* Se definió la solución de **separar las etapas de escaneo y presión**.
* Se identificaron los problemas de escasez de la **Kinect**.

**Dificultades encontradas:**
* La escasez de la Kinect y la necesidad del adaptador forzaron a considerar la viabilidad del escáner.

**Próximos pasos:**
* Reparación de la impresora 3D y búsqueda de un reemplazo para el Kinect.
