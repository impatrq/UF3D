## Mes de Noviembre

### Semana 1: Migración a Pi Pico y Fabricación de Nueva Placa de Control

**Objetivo de la semana:**
* Resolver la inestabilidad recurrente de la Raspberry Pi 4 (Pi 4) y migrar a un microcontrolador más fiable para la etapa de control.
* Diseñar y fabricar la nueva placa de control.

**Actividades realizadas:**
* Se realizaron pruebas para estabilizar la Pi 4 intentando el arranque a través de la salida **Micro HDMI** a monitores, pero la inestabilidad regresó después de poco tiempo.
* Se tomó la decisión de cambiar de microcontrolador, optando por la **Raspberry Pi Pico** debido a que se percibía como más simple y confiable para las tareas de control de motores.
* Se diseñó y se fabricó una **nueva placa de cobre** adaptada a la **Pi Pico**.
* En el nuevo diseño se tomaron medidas para mejorar la fiabilidad: se **agrandaron las pistas** y se hicieron las conexiones más cómodas.

**Resultados obtenidos:**
* Se decidió la **migración completa** del control de motores a la Pi Pico.
* Se completó el diseño y la fabricación de la **placa de control adaptada** al nuevo microcontrolador.

**Dificultades encontradas:**
* La persistente inestabilidad del *boot* y las conexiones de pines de la Raspberry Pi 4.

**Próximos pasos:**
* Probar la funcionalidad de los drivers y motores con la nueva placa.

***

### Semana 2: Control Estable de Motores, Integración LiDAR y Primeras Impresiones

**Objetivo de la semana:**
* Lograr el control total y estable de motores y sensor en la Pi Pico.
* Iniciar el testeo y la calibración de la impresora 3D.

**Actividades realizadas:**
* **Control de Motores:** Una vez fabricada la placa, se probaron los drivers y funcionaron perfectamente, **moviendo hasta dos motores paso a paso a la vez**. Se identificó que faltaba un driver operativo, se compró un reemplazo y, una vez instalado, **los tres motores funcionaron sin problemas**.
* **Integración LiDAR:** Se intentó testear el sensor LiDAR en la Pi Pico y **no funcionaba** (a pesar de funcionar en la Pi 4), un problema que resultó ser inusual. Tras diversas pruebas con códigos e invirtiendo el cableado, se descubrió que la única manera de que funcionara era **puentear el TX y RX del mismo LiDAR**. Esta corrección permitió seguir avanzando con el testeo del sensor.
* **Impresora 3D:** Se realizaron las primeras pruebas de impresión y **calibración** para el filamento **PETG**. Posteriormente, se realizó el **cambio de filamento a PLA**, con la calibración específica requerida para este material.

**Resultados obtenidos:**
* **Control de tres motores estable** y funcionando correctamente con la Pi Pico.
* Se implementó una **solución de *hardware*** (puenteo TX/RX) para el sensor LiDAR.
* Se **calibró la impresora** para los filamentos PETG y PLA.

**Dificultades encontradas:**
* Problema de comunicación inexplicable del LiDAR con la Pi Pico.

**Próximos pasos:**
* Fabricar los componentes mecánicos de acople.

***

### Semana 3: Solución Mecánica Ingeniosa y Montaje Final del Escáner

**Objetivo de la semana:**
* Resolver los problemas de acoplamiento mecánico y ensamblar el sistema de escaneo completo.

**Actividades realizadas:**
* **Diseño e Impresión 3D:** Se diseñaron **tres acoples en AutoCAD** para las varillas roscadas de los ejes X e Y, y se buscaron y modificaron **dos soportes** para las varillas del eje Y. Todas estas piezas fueron **impresas en 3D con filamento PLA**.
* **Problema Anti-Backlash:** La **tuerca *anti-backlash* comprada no encajaba** con las varillas roscadas.
* **Solución Ingeniosa:** Se compraron **arandelas con tuercas a rosca** que sí coincidían con la varilla. Se procedió a **soldar la tuerca a la arandela** con un soldador eléctrico.
* Esta solución casera funcionó perfectamente, permitiendo que la varilla realizara los **movimientos horizontales y verticales** para el sensor LiDAR sin juego.
* **Ensamblaje Final:** Finalmente, se procedió a **unir y montar todo el escáner**, integrando la Pi Pico, los motores, el LiDAR y la estructura de ejes en H.

**Resultados obtenidos:**
* Se creó una **solución mecánica funcional y económica** para el problema de la tuerca *anti-backlash*.
* El **escáner fue completamente ensamblado y montado** en su estructura final.

**Dificultades encontradas:**
* Incompatibilidad de la tuerca *anti-backlash* comprada.

**Próximos pasos:**
* Pruebas de funcionamiento del sistema ensamblado y desarrollo de *software* de alto nivel.
