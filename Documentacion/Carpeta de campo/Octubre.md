## Mes de Octubre

### Semana 1 de octubre: Depuración de la Placa de Cobre Prototipo

**Objetivo de la semana:**
* Finalizar el ensamblaje y la corrección de la primera versión de la placa de cobre de control de motores.
* Realizar las primeras pruebas funcionales de los motores y el sensor.

**Actividades realizadas:**
* Se realizó una intensa labor de **soldadura y desoldadura** de componentes para asegurar la continuidad de las pistas.
* Se encontraron y corrigieron múltiples **cortocircuitos** donde las patas tocaban la línea de tierra (GND) debido al diseño compacto de la placa.
* Se tuvieron que **desoldar borneras** para acceder y corregir las pistas.
* Se reubicó una **bornera en el lado opuesto** para facilitar las conexiones.
* Se corrigieron fallos donde las **patas de los componentes no hacían contacto** correcto con el estaño.
* Se iniciaron las pruebas de funcionamiento: probando **uno y dos motores más el sensor**. Los motores que giraban lo hacían con **muchísimo ruido y vibraciones**, y consumían más corriente de lo normal.
* El tercer motor no funcionó.

**Resultados obtenidos:**
* La placa de control fue ensamblada y corregida, lista para pruebas.
* Detección de problemas de **ruido/vibración** en los motores y **fallo** en el tercer motor.

**Dificultades encontradas:**
* Múltiples errores de soldadura y problemas de cortocircuitos por la complejidad del diseño.

**Próximos pasos:**
* Diagnosticar la causa del ruido y el fallo del tercer motor.

***

### Semana 2 de octubre: Diagnóstico Crítico y Fallo de Componentes

**Objetivo de la semana:**
* Resolver problemas de ruido/vibración y diagnosticar el fallo del tercer motor.
* Solucionar un fallo crítico en la Raspberry Pi 4 (Pi 4).

**Actividades realizadas:**
* Se descubrió que la causa del **ruido y las vibraciones** venía de los **cables conectores del motor**, que estaban **derretidos** y causaban un mal contacto. Una vez reemplazados, los dos motores funcionaron perfectamente.
* Se diagnosticó el fallo del tercer motor, sospechando del driver. Se **desoldó el driver** y se probó, confirmando que el **GND y VCC estaban en cortocircuito interno** (componente defectuoso de fábrica). Tuvimos que conseguir otro driver nuevo.
* Durante estas pruebas, la **Pi 4 tuvo un fallo**: no reconocía la Micro SD porque el **zócalo se había desprendido**.
* Se investigó la solución y se logró **instalar el sistema operativo en un USB** y configurar la Pi 4 para que **arrancara desde el USB**, reviviendo la placa.

**Resultados obtenidos:**
* **Ruido y vibración de motores resueltos**.
* **Pi 4 recuperada** con éxito mediante la configuración de arranque por USB.
* Detección de un **driver de motor defectuoso**.

**Dificultades encontradas:**
* Fallo físico del zócalo SD de la Pi 4.
* Componente defectuoso (driver) que impidió la operación completa.

**Próximos pasos:**
* Probar la placa con el driver nuevo.

***

### Semana 3 de octubre: Deterioro de la Placa y Rediseño Definitivo

**Objetivo de la semana:**
* Probar la funcionalidad completa con el nuevo driver.
* Diseñar y ensamblar una nueva placa de control (Versión Definitiva) debido al deterioro del prototipo.

**Actividades realizadas:**
* Una vez con el driver nuevo, al intentar probar la placa, **ninguno de los tres drivers y motores funcionó**. Los motores consumían corriente, pero no giraban.
* Se descubrió que la **placa de cobre prototipo estaba seriamente deteriorada**: el cobre estaba **levantado y quemado** cerca de los conectores de la Pi 4 debido a las pruebas y fallos de corriente, además de presentar oxidación.
* Se tomó la decisión de **desechar la placa prototipo** y construir una **nueva desde cero** para asegurar la fiabilidad.
* Se **desoldaron todos los componentes** y se compraron una nueva placa de cobre y conectores.
* Se procedió a **fabricar la placa de nuevo**, corrigiendo las pistas y **mejorando el diseño** para crear la **versión definitiva** del circuito de control.

**Resultados obtenidos:**
* Se constató el **fallo total y deterioro físico** de la placa prototipo.
* Se inició el proceso de **rediseño y fabricación de la placa de control definitiva**.

**Dificultades encontradas:**
* Fallo irreversible de la placa prototipo, obligando a un reinicio de la fase de ensamblaje.

**Próximos pasos:**
* Ensamblar y testear la nueva placa definitiva.

***

### Semana 4 de octubre: Nuevos Componentes y Avances en Impresora

**Objetivo de la semana:**
* Adquirir componentes mecánicos para el sistema de ejes en H.
* Integrar la nueva placa madre y poner en funcionamiento el extrusor de la impresora 3D.

**Actividades realizadas:**
* Se investigaron y compraron **tuercas anti-backlash** y los **acoples** necesarios para las varillas roscadas, avanzando en los componentes del **sistema de ejes en H** para el escáner.
* Con la nueva placa definitiva realizada, se testó nuevamente: solo **funcionó un driver de motor y el sensor LiDAR**.
* Se encontró que la **Pi 4 se desconectaba fácilmente** de los pines y el proceso de **arranque (bootear)** era **muy irregular**, lo que causaba grandes retrasos. Se inició la investigación de alternativas.
* Se implementó la solución para el control de la impresora: se instaló y se configuró el **pinout de la placa madre SKR 1.4**.
* Se comenzó a usar la **fuente de la impresora** para alimentar la nueva placa madre.
* Se tuvo que realizar un **cable DB25 casero** y comprar las fichas para realizar conexiones.
* Se realizaron ajustes en la configuración de *firmware* (`Klipper`): se cambió el **fin de carrera de X2 por Z2**.
* El **eje Z presentó problemas de falso contacto** en sus conexiones, lo que requirió diagnóstico.
* Finalmente, se **eliminó el cable DB25 casero** y se conectó el **extrusor directamente** a la placa mediante cables, simplificando la conexión.
* Se logró poner en **funcionamiento el extrusor con filamento**, demostrando que el subsistema de fabricación de la plantilla estaba operativo.

**Resultados obtenidos:**
* Adquisición de **componentes clave** para el sistema de ejes del escáner.
* **Extrusor de la impresora 3D operativo** y probado con filamento.
* Detección de una nueva dificultad: **inestabilidad en la conexión y el arranque de la Pi 4**.

**Dificultades encontradas:**
* Persistencia de fallos en el control de motores y el arranque irregular de la Pi 4.
* Dificultades de conectividad (falso contacto en eje Z) y necesidad de simplificar el cableado (eliminación del DB25).

**Próximos pasos:**
* Encontrar una solución definitiva para la inestabilidad de la Pi 4.
* Solucionar el fallo en el control de los tres motores.
