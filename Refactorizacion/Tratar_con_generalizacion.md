# Tratar con generalización

La abstracción tiene su propio grupo de técnicas de refactorización, 
principalmente asociadas con mover la funcionalidad a lo largo de la jerarquía 
de herencia de clases, crear nuevas clases e interfaces, 
y reemplazar la herencia con delegación y viceversa.

## Subir Campo
Problema: Dos clases tienen el mismo campo.

Solución: Elimina el campo de las subclases y muévelo a la superclase.

## Subir Método
Problema: Tus subclases tienen métodos que realizan trabajos similares.

Solución: Haz que los métodos sean idénticos y luego muévelos a la superclase relevante.

## Subir el cuerpo del constructor
Problema: Tus subclases tienen constructores con código que es mayormente idéntico.

Solución: Crea un constructor en la superclase y mueve el código que 
es igual en las subclases a él. 
Llama al constructor de la superclase en los constructores de las subclases.

## Empujar Método hacia Abajo
Problema: ¿El comportamiento implementado en una superclase es utilizado 
por solo una (o unas pocas) subclases?

Solución: Mueve este comportamiento a las subclases.

## Empujar Campo hacia Abajo
Problema: ¿Se utiliza un campo solo en algunas subclases?

Solución: Mueve el campo a esas subclases.

## Extraer Subclase
Problema: Una clase tiene características que se utilizan solo en ciertos casos.

Solución: Crea una subclase y úsala en esos casos.

## Extraer Superclase
Problema: Tienes dos clases con campos y métodos comunes.

Solución: Crea una superclase compartida para ellas y mueve todos los campos 
y métodos idénticos a ella.

## Extraer Interfaz
Problema: Varios clientes están utilizando la misma parte de una interfaz de clase. 
Otro caso: parte de la interfaz en dos clases es la misma.

Solución: Mueve esta porción idéntica a su propia interfaz.

## Colapsar Jerarquía
Problema: Tienes una jerarquía de clases en la que una subclase es prácticamente 
igual que su superclase.

Solución: Fusiona la subclase y la superclase.

## Formar Método de Plantilla
Problema: Tus subclases implementan algoritmos que contienen pasos similares 
en el mismo orden.

Solución: Mueve la estructura del algoritmo y los pasos idénticos a una superclase, 
y deja la implementación de los pasos diferentes en las subclases.

## Reemplazar Herencia con Delegación
Problema: Tienes una subclase que utiliza solo una porción de los métodos 
de su superclase (o no es posible heredar datos de la superclase).

Solución: Crea un campo y pon un objeto de superclase en él, delega métodos 
al objeto de la superclase, y deshazte de la herencia.

## Reemplazar Delegación con Herencia
Problema: Una clase contiene muchos métodos simples que delegan a todos los 
métodos de otra clase.

Solución: Haz que la clase sea una heredera delegada, lo que hace que los 
métodos de delegación sean innecesarios.

