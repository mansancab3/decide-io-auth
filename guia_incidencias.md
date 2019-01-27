Sistema de incidencias
======================
Guía para la creación de incidencias en el fork de Decide-Ío-Visualización.

***Nota: Si usted no pertenece al equipo de desarrollo, unicamente debe mirar el apartado de Plantillas y el apartado de "tipos de incidencia" de Etiquetas.***

Plantillas
----------
Existen 2 plantillas que pueden ser usada para la creación de incidencias:

* **Bug report**. Esta plantilla se puede usar cuando se quiere reportar algún bug.

* **Feature request**. Plantilla ideal para la creación de incidencias relativa a peticiones de nuevas características.

Si no se desea usar plantillas o el tipo de incidencia no se ajusta a ninguna de estas dos plantillas, puede crearse una incidencia sin plantilla, pero asegurese de explicar claramente el motivo de la incidencia y de aportar todos los datos posibles.

Puede ver las plantillas en esta [sección del repositorio](https://github.com/EGC-DECIDE-IO-Visualizacion/decide-io/tree/master/.github/ISSUE_TEMPLATE).

Etiquetas
---------
Existen varios tipos de etiquetas que nos sirven para identificar y catalogar rapidamente una incidencia:

* **Tipo de incidencia**. *Color morado*.

  Estas etiquetas sirven para identificar el tipo de incidencia. Puede ser:
  - `Duda`: No esta seguro de si el comportamiento actual es el correcto o no y necesita información del equipo de desarrollo.
  - `Mejora`: Aunque todo funciona correctamente, propone una posible mejora en el funcionamiento actual.
  - `Rediseño`: Aunque todo funciona correctamente, un cambio en la implementación podría mejorar el sistema.
  - `Mal comportamiento`: Aunque no se producen fallos, el comportamiento no es el esperado.
  - `Bug menor`: Se producen fallos pero la acción termina de ejecutarse.
  - `Bug`: Se producen fallos que no permiten realizar alguna/s acción/es.
  
* **Tipo de incidencia**. *Color naranja*.

  Estas etiquetas serán usadas únicamente por el equipo de desarrollo.
  - `Duplicada`: La incidencia ya ha sido creada con anterioridad y no es necesario volver a abordarla.
  - `Inválida`: La incidencia no es válida. Los motivos pueden ser variados (falta de información, sin sentido, incidencia creada por error, etc).
  - `No factible`: La incidencia es correcta pero para abordarla se necesitarían más recursos de los necesarios o significaría abandonar el resto de los desarrollos.
  
  **Si usted no pertenece al equipo de desarrollo, no use ninguna de las etiquetas de incidencia de color naranja.**
  
* **Estado de incidencia**. *Color verde*.

  Estas etiquetas sirven para establecer el estado en el que se encuentra la incidencia. Estos estados, ordenados son:
  `Nueva` - `Asignada` - `En proceso` - `Pendiente de prueba` - `cerrada`
  
  **Si usted no pertenece al equipo de desarrollo y esta creando la incidencia por primera vez, use siempre la etiqueta `Nueva`.**
  
* **Prioridad de incidencia**. *Color azul*.

  Estas etiquetas sirven para establecer una prioridad en la incidencia. Ordenadas de menor a mayor prioridad, las etiquetas son:
  `Baja` - `Media` - `Alta` - `Muy alta` - `Crítica`
  
  **Si usted no pertenece al equipo de desarrollo, no use ninguna de las etiquetas de prioridad.**
  
* **Roles**. *Color rosa*.

  Estas etiquetas serán usadas únicamente por el equipo de desarrollo y sirven para determinar el rol que mejor se ajusta al tipo de incidencia.
  - `Desarrollador`: La incidencia puede ser resuelta mediante un nuevo desarrollo o esta relacionada con un bug menor.
  - `Tester`: La incidencia puede ser resuelta mediante una serie de pruebas o bien esta relacionada con un bug de alta prioridad.
  - `Integrador`: La incidencia esta relacionada con la integración de código.
  
   **Si usted no pertenece al equipo de desarrollo, no use ninguna de las etiquetas de roles.**
