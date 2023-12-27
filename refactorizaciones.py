#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
# Técnicas de Refactorización

## Composición de Métodos
Gran parte de la refactorización se dedica a componer correctamente los métodos. 
En la mayoría de los casos, los métodos excesivamente largos son la raíz de 
todos los males. 
Las vaguedades del código dentro de estos métodos ocultan la lógica de ejecución 
y hacen que el método sea extremadamente difícil de entender, 
e incluso más difícil de cambiar.

Las técnicas de refactorización de este grupo simplifican los métodos, 
eliminan la duplicación de código y allanan el camino para futuras mejoras.

- Extraer Método
- Método en línea
- Extraer Variable
- Variable temporal en línea
- Reemplazar Variable temporal con consulta
- Dividir variable temporal
- Eliminar asignaciones a parámetros
- Reemplazar Método con Objeto Método
- Sustituir Algoritmo

# Mover Características entre Objetos
Incluso si ha distribuido la funcionalidad entre diferentes clases de 
manera imperfecta, todavía hay esperanza.

Estas técnicas de refactorización muestran cómo mover la funcionalidad 
entre clases de forma segura, crear nuevas clases y ocultar detalles de 
implementación del acceso público.

- Mover Método
- Mover Campo
- Extraer Clase
- Clase en línea
- Ocultar Delegado
- Eliminar intermediario
- Introducir Método Externo
- Introducir Extensión Local

## Organización de Datos
Estas técnicas de refactorización ayudan con el manejo de datos, 
reemplazando primitivas con funcionalidades de clase ricas. 

Otro resultado importante es el desenredo de las asociaciones de clase, 
lo que hace que las clases sean más portátiles y reutilizables.

- Cambiar Valor a Referencia
- Cambiar Referencia a Valor
- Duplicar Datos Observados
- Autoencapsular Campo
- Reemplazar Valor de Datos con Objeto
- Reemplazar Matriz con Objeto
- Cambiar Asociación Unidireccional a Bidireccional
- Cambiar Asociación Bidireccional a Unidireccional
- Encapsular Campo
- Encapsular Colección
- Reemplazar Número Mágico con Constante Simbólica
- Reemplazar Código de Tipo con Clase
- Reemplazar Código de Tipo con Subclases
- Reemplazar Código de Tipo con Estado/Estrategia
- Reemplazar Subclase con Campos

## Simplificación de Expresiones Condicionales
Las condicionales tienden a volverse cada vez más complicadas en su 
lógica con el tiempo, y aún hay más técnicas para combatir esto también.

- Consolidar Expresión Condicional
- Consolidar Fragmentos Condicionales Duplicados
- Descomponer Condición
- Reemplazar Condicional con Polimorfismo
- Eliminar Bandera de Control
- Reemplazar Condicional Anidado con Cláusulas de Guarda
- Introducir Objeto Nulo
- Introducir Aserto

## Simplificación de Llamadas a Métodos
Estas técnicas hacen que las llamadas a métodos sean más simples 
y fáciles de entender. Esto, a su vez, simplifica las interfaces 
de interacción entre clases.

- Agregar Parámetro
- Eliminar Parámetro
- Cambiar Nombre de Método
- Separar Consulta de Modificador
- Parametrizar Método
- Introducir Objeto como Parámetro
- Preservar Objeto Completo
- Eliminar Método de Configuración
- Reemplazar Parámetro con Métodos Expl
"""
"""
===========================================================================================
# Componiendo Métodos
Gran parte de la refactorización se dedica a componer métodos correctamente. 
En la mayoría de los casos, los métodos excesivamente largos son la raíz de 
todos los males. 

Las vaguedades del código dentro de estos métodos ocultan la lógica de 
ejecución y hacen que el método sea extremadamente difícil de entender, 
e incluso más difícil de cambiar.

Las técnicas de refactorización en este grupo simplifican los métodos, 
eliminan la duplicación de código y allanan el camino para futuras mejoras.

## Extraer Método
Problema: tiene un fragmento de código que se puede agrupar.

Solución: mueva este código a un nuevo método (o función) separado y 
reemplace el código antiguo con una llamada al método.

## Método en Línea
Problema: cuando el cuerpo del método es más obvio que el propio método, 
use esta técnica.

Solución: reemplace las llamadas al método con el contenido del método 
y elimine el método en sí.

## Extraer Variable
Problema: tiene una expresión difícil de entender.

Solución: coloque el resultado de la expresión o sus partes en variables 
separadas que sean autoexplicativas.

## Temporizador en Línea
Problema: tiene una variable temporal a la que se le asigna el resultado 
de una expresión simple y nada más.

Solución: reemplace las referencias a la variable con la expresión misma.

## Reemplace el Temporizador con la Consulta
Problema: coloca el resultado de una expresión en una variable local para 
su uso posterior en su código.

Solución: mueva toda la expresión a un método separado y devuelva el resultado de ella. 
Consulte el método en lugar de usar una variable. 
Incorpore el nuevo método en otros métodos si es necesario.

## Dividir Variable Temporal
Problema: tiene una variable local que se utiliza para almacenar varios 
valores intermedios dentro de un método (excepto para variables de ciclo).

Solución: use diferentes variables para diferentes valores. 
Cada variable debe ser responsable de una sola cosa en particular.

## Eliminar Asignaciones a Parámetros
Problema: se asigna algún valor a un parámetro dentro del cuerpo del método.

Solución: use una variable local en lugar de un parámetro.

Reemplace el Método con el Objeto del Método
Problema: tiene un método largo en el que las variables locales están tan 
entrelazadas que no se puede aplicar Extraer Método.

Solución: transforme el método en una clase separada para que las variables 
locales se conviertan en campos de la clase. 

Luego, puede dividir el método en varios métodos dentro de la misma clase.

## Sustituya el Algoritmo
Problema: ¿Quiere reemplazar un algoritmo existente por uno nuevo?

Solución: reemplace el cuerpo del método que implementa el algoritmo con un 
nuevo algoritmo.
"""
"""
=========================================================================================
# Mover funcionalidades entre objetos
Incluso si ha distribuido la funcionalidad entre diferentes clases de una manera 
menos que perfecta, todavía hay esperanza.

Estas técnicas de refactorización muestran cómo mover funcionalidad entre 
clases de manera segura, crear nuevas clases y ocultar detalles de implementación 
del acceso público.

## Mover Método
Problema: un método se utiliza más en otra clase que en su propia clase.

Solución: cree un nuevo método en la clase que más use el método, luego mueva el 
código del antiguo método allí. 
Convierta el código del método original en una referencia al nuevo 
método en la otra clase o elimínelo por completo.

## Mover Campo
Problema: un campo se utiliza más en otra clase que en su propia clase.

Solución: cree un campo en una nueva clase y redirija a todos los usuarios del 
campo antiguo hacia él.

## Extraer Clase
Problema: cuando una clase hace el trabajo de dos, se producen dificultades.

Solución: en su lugar, cree una nueva clase y coloque los campos y métodos 
responsables de la funcionalidad relevante en ella.

## Clase en Línea
Problema: una clase hace casi nada y no es responsable de nada, y no se planean 
responsabilidades adicionales para ella.

Solución: mueva todas las características de la clase a otra.

## Ocultar Delegado
Problema: el cliente obtiene el objeto B de un campo o método del objeto A. 
Luego, el cliente llama a un método del objeto B.

Solución: cree un nuevo método en la clase A que delegue la llamada al objeto B. 
Ahora el cliente no sabe sobre la clase B o depende de ella.

## Eliminar Intermediario
Problema: una clase tiene demasiados métodos que simplemente delegan a otros objetos.

Solución: elimine estos métodos y obligue al cliente a llamar directamente a 
los métodos finales.

## Introducir Método Externo
Problema: una clase de utilidad no contiene el método que necesita y no puede agregar 
el método a la clase.

Solución: agregue el método a una clase cliente y pase un objeto de la clase 
de utilidad como argumento.

## Introducir Extensión Local
Problema: una clase de utilidad no contiene algunos métodos que necesita. 
Pero no puede agregar estos métodos a la clase.

Solución: cree una nueva clase que contenga los métodos y haga que sea hija 
o envoltorio de la clase de utilidad.
"""
"""
========================================================================================
## Organizando datos

Estas técnicas de refactorización ayudan con el manejo de datos, 
reemplazando los tipos primitivos con funcionalidad de clase rica.

Otro resultado importante es el desenredo de las asociaciones de clases, 
lo que hace que las clases sean más portátiles y reutilizables.

## Autocapsular campo
Problema: Accede directamente a campos privados dentro de una clase.

Solución: Cree un getter y un setter para el campo, y úselos solo para acceder al campo.

## Reemplazar valor de datos con objeto
Problema: Una clase (o grupo de clases) contiene un campo de datos. 
El campo tiene su propio comportamiento y datos asociados.

Solución: Cree una nueva clase, coloque el campo antiguo y su comportamiento 
en la clase y almacene el objeto de la clase en la clase original.

## Cambiar valor a referencia
Problema: Tiene muchas instancias idénticas de una sola clase que necesita 
reemplazar con un solo objeto.

Solución: Convierta los objetos idénticos en un objeto de referencia único.

## Cambiar referencia a valor
Problema: Tiene un objeto de referencia que es demasiado pequeño y cambia con 
poca frecuencia para justificar la gestión de su ciclo de vida.

Solución: Conviértalo en un objeto de valor.

## Reemplazar matriz con objeto
Problema: Tiene una matriz que contiene varios tipos de datos.

Solución: Reemplace la matriz con un objeto que tendrá campos separados para 
cada elemento.

## Datos observados duplicados
Problema: ¿Los datos de dominio se almacenan en clases responsables de la GUI?

Solución: Entonces es una buena idea separar los datos en clases separadas, 
asegurando la conexión y sincronización entre la clase de dominio y la GUI.

Cambiar asociación unidireccional a bidireccional
Problema: Tiene dos clases que necesitan usar las características de la otra, 
pero la asociación entre ellas es solo unidireccional.

Solución: Agregue la asociación faltante a la clase que la necesita.

Cambiar asociación bidireccional a unidireccional
Problema: Tiene una asociación bidireccional entre clases, pero una de las 
clases no usa las características de la otra.

Solución: Elimine la asociación no utilizada.

## Reemplazar número mágico con constante simbólica
Problema: Su código utiliza un número que tiene cierto significado.

Solución: Reemplace este número con una constante que tenga un nombre 
legible por humanos que explique el significado del número.

## Encapsular campo
Problema: Tiene un campo público.

Solución: Haga que el campo sea privado y cree métodos de acceso para él.

## Encapsular colección
Problema: Una clase contiene un campo de colección y un getter y setter 
simple para trabajar con la colección.

Solución: Haga que el valor devuelto por el getter sea de solo lectura 
y cree métodos para agregar / eliminar elementos de la colección.

## Reemplazar código de tipo con clase
Problema: Una clase tiene un campo que contiene código de tipo. 
Los valores de este tipo no se utilizan en condiciones de operador y 
no afectan el comportamiento del programa.

Solución: Cree una nueva clase y use sus objetos en lugar de los valores 
de código de tipo.

Reemplazar código de tipo con subclases

"""
"""
====================================================================================
# Simplificación de expresiones condicionales
Las expresiones condicionales tienden a volverse cada vez más complicadas 
en su lógica con el tiempo, y existen aún más técnicas para combatir esto también.

## Descomponer condicional
Problema: Tienes una condición compleja (if-then/else o switch).

Solución: Descompone las partes complicadas de la condición en métodos separados: 
la condición, el resultado de entonces y el resultado de lo contrario.

## Consolidar expresión condicional
Problema: Tienes múltiples condiciones que llevan al mismo resultado o acción.

Solución: Consolida todas estas condiciones en una sola expresión.

## Consolidar fragmentos condicionales duplicados
Problema: Se puede encontrar código idéntico en todas las ramas de una condición.

Solución: Mueve el código fuera de la condición.

## Eliminar bandera de control
Problema: Tienes una variable booleana que actúa como una bandera de control 
para múltiples expresiones booleanas.

Solución: En lugar de la variable, utiliza break, continue y return.

## Reemplazar condicional anidado con cláusulas de guardia
Problema: Tienes un grupo de condicionales anidados y es difícil determinar 
el flujo normal de ejecución de código.

Solución: Aisla todas las comprobaciones especiales y casos extremos en cláusulas 
separadas y colócalas antes de las comprobaciones principales. Idealmente, 
deberías tener una lista "plana" de condicionales, uno tras otro.

## Reemplazar condicional con polimorfismo
Problema: Tienes una condición que realiza varias acciones según el tipo o 
las propiedades del objeto.

Solución: Crea subclases que coincidan con las ramas del condicional. En ellas, 
crea un método compartido y mueve el código de la rama 
correspondiente del condicional a él. 

Luego, reemplaza el condicional con la llamada al método relevante. 
El resultado es que se obtendrá la implementación adecuada mediante 
el polimorfismo según la clase del objeto.

## Introducir objeto nulo
Problema: Dado que algunos métodos devuelven null en lugar de objetos reales, 
tienes muchas comprobaciones de null en tu código.

Solución: En lugar de null, devuelve un objeto nulo que exhibe el comportamiento 
predeterminado.

## Introducir afirmación
Problema: Para que una porción de código funcione correctamente, 
ciertas condiciones o valores deben ser verdaderos.

Solución: Reemplaza estas suposiciones con comprobaciones de afirmación específicas.
"""
"""
===================================================================================

"""
"""
================================================================================
"""