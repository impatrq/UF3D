## Día 10

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez
-  Victoria Viva
-  Valentin Zaccari

**Objetivo del día:**  
-  Verificar el funcionamiento de las salidas de la skr
-  Hacer funcionar un motor con la raspberry pi 4

**Actividades realizadas:**  
-  Se probo un motor con la pi 4 con la supervision del profesor Garabato
-  Se probo la alimentacion de la skr
-  Se probaron las salidas de los cooler de la skr
-  Se probaron las salidas de los motores de la skr
-  Se realizaron pruebas y medidas individuales para intentar encontrar el problema dentro del circuito del motor de la pi 4

**Resultados obtenidos:**  
-  El motor funciono parcialmente
-  No se encontro el problema
-  Se comprobo el correcto funcionamiento de las salidas de la skr

**Dificultades encontradas:**  
-  No conocemos el motivo del fallo en el circuito de la impresora

**Próximos pasos:**  
-  Encontrar el problema del circuito de la pi 4
-  Probar los Ejes de la impresora

---
## Día 11

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez
-  Victoria Viva
-  Valentin Zaccari

**Objetivo del día:**  
-  Probar Eje Y de la impresora
-  Probar Eje X de la impresora
-  Probar Eje Z de la impresora
-  Nivelar Eje Z de la impresora
-  Hacer funcionar un motor con la raspberry pi 4

**Actividades realizadas:**  
-  Se probo un motor con la pi 4 con la supervision del profesor Gabriel Arguello
-  Se probo la alimentacion de la skr
-  Se probaron las salidas de los cooler de la skr
-  Se probaron las salidas de los motores de la skr
-  Se realizaron pruebas y medidas indivuduales para intentar encontar el problema dentro del circuito del motor de la pi 4

**Resultados obtenidos:**  
-  El motor no arranco
-  Se comprobo el correcto funcionamiento de las salidas de la skr

**Dificultades encontradas:**  
-  Las medidas dieron como resultado que en la enrda dl step estaban llegando 1.6V y no 3.3V como se esperaba

**Próximos pasos:**  
-  Encontrar una forma de amplificarel voltajedado por la pi 4 en la entada del STEP
-  Probar los Ejes de la impresora

---
## Día 12

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez
-  Victoria Viva
-  Valentin Zaccari

**Objetivo del día:**  
-  Hacer funcionar un motor con la raspberry pi 4 

**Actividades realizadas:**  
-  Nuevo cableado d los ejes Z e Y de la impresora
-  Se realizo un diagrama para agregar un comparador al circuito de la pi 4
-  Se intento arrancar el motor con este nuevo circuito
-  Se realizaron pruebas y medidas individuales para intentar encontar el problema dentro del circuito del motor de la pi 4

**Resultados obtenidos:**  
-  El motor no arranco
-  No se encontro el problema
-  Se comprobo el funcionaminto del nuevo cableado

**Dificultades encontradas:**  
-  El motor de la pi 4 no arranco

**Próximos pasos:**  
-  Encontar el problema del circuito de la pi 4

---
## Día 15

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez
-  Victoria Viva
-  Valentin Zaccari

**Objetivo del día:**  
-  Verificar el funcionamiento d las salidas de la skr
-  Haver funcionar un motor con la raspberry pi 4

**Actividades realizadas:**  
-  Homing Eje Y y Eje X
-  Comprobar fines de carrera del Eje X
-  Se probo el nuevo circuito para el motor del escaner con el comparador bajo la supervision de Gabriel Arguello
-  Se realizaron pruebas y medidas indiviudales para intentar encontar el problema dentro del circuito del motor de la pi 4
-  Se realizo el esquematico y el pcb para este nuevo circuito

**Resultados obtenidos:**  
-  El motor arranco parcialmente, se movia cuando se tocaba un cable en especifico
-  No se encontro el problema
-  Se comprobo correctamente los fines de carrera
-  Se completo con exito el homing de los Ejes X e Y

**Dificultades encontradas:**  
-  Se cree que el error puede ser culpa de los cables

**Próximos pasos:**  
-  Solucionar el problema del circuito de los motores del escaner o imprimir el pcb
-  Homing Eje Z

---
## Día 16

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez
-  Victoria Viva
-  Valentin Zaccari

**Objetivo del día:**  
-  Hacer funcionar un motor con la raspberry pi 4

**Actividades realizadas:**  
-  Conexion en paralelo de los sensores Z1 minimo y Z2 minimo
-  Se realizo un diagrama para un circuito con un rele y uno para un circuitocon un tansistor parael circuito del motor por las recomendaciones de un profesor
-  Se probaron ambos esquemas
-  Se probo el motor usando el compardor y asegurando una buena conexion
-  Se realizaron pruebas y medidas indiviudales para intentar encontar el problema dentro del circuito del motor de la pi 4

**Resultados obtenidos:**  
-  Ninguno de los esquemas funciono
-  No se encontro el problema
-  Las conexiones en paralelo resultaron exitosas

**Dificultades encontradas:**  
-  El motor de la pi 4 no arranco
-  Se sospecha que es por culpa de los cables

**Próximos pasos:**  
-  Encontar el problema del circuito de la pi 4
-  Probar los Ejes de la impresora

---
## Día 17

**Integrantes presentes:**  
-  Agustin Azorin 
-  Eugenio Herrera (Falto por enfermedad)
-  Tiago Lopez
-  Victoria Viva
-  Valentin Zaccari

**Objetivo del día:**  
-  Hacer funcionar un motor con la raspberry pi 4
-  Hacer el homing del Eje Z

-  
**Actividades realizadas:**  
-  Se probo un motor con la pi 4 con la supervision de Fabrizio Karlassara
-  

**Resultados obtenidos:**  
-  El motor finalmene funciono
-  Se encinto la tira de pines del motor para que no generen falso contacto
-  Se prescindio dl comparador

**Dificultades encontradas:**  
-  Se encontaron varios drivers disfuncionales

**Próximos pasos:**  
-  Realizar el esquematico y el pcb para el nuevo circuito

---
## Día 18

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez

**Objetivo del día:**  
-  Realizar el pcb y el esquematico del nuevo circuito para el escaner
-  Completar el Homing del Eje Z
**Actividades realizadas:**  
-  Se probo un motor con la pi 4 con la supervision de Arguello Gabriel
-  Se desmonto una impresora 3D vieja para intentar conseguir componentes necesarios
-  Se intento hacer el homing del Eje Z 

**Resultados obtenidos:**  
-  Se termino el pcb y el esquematico
-  Se consiguiron unos cuantos componentes de la impresora vieja
-  

**Dificultades encontradas:**  
-  No se conmsiguieon los acoples buscados

**Próximos pasos:**  
-  Imprimir el pcb.

---
## Día 22

**Integrantes presentes:**  
-  Melina Alfonso
-  Agustin Azorin 
-  Eugenio Herrera
-  Tiago Lopez
-  Valentin Zaccari

**Objetivo del día:**  
-  Probar dos motores a la vez
-  Imprimir el pcb para la placa
-  

**Actividades realizadas:**  
-  Se probaron dos motores a la vez
-  Homing del Eje Z

**Resultados obtenidos:**  
-  Se logro que ambos funcionen al mismo tiempo acorde al esquema realizado

**Dificultades encontradas:**  
-  Se encontro que uno de los drivers no funcionaban

**Próximos pasos:**  
-  Comprar una placa de cobre
-  Comprar borneras
-  Pegar el pcb a la palca y pasarla por acido
-  Agujerear la placa

**Actividades realizadas:**  
-  Se probaron dos motores a la vez
-  Homing del Eje Z

**Resultados obtenidos:**  
-  Se logro que ambos funcionen al mismo tiempo acorde al esquema realizado

**Dificultades encontradas:**  
-  Se encontro que uno de los drivers no funcionaban

**Próximos pasos:**  
-  Comprar una placa de cobre
-  Comprar borneras
-  Pegar el pcb a la palca y pasarla por acido
-  Agujerear la placa

