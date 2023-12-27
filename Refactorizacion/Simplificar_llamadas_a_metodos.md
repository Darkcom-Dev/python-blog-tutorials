# Simplificando Llamadas a Métodos
Estas técnicas hacen que las llamadas a métodos sean más simples y fáciles de entender. 
Esto, a su vez, simplifica las interfaces para la interacción entre clases.

## Renombrar Método
Problema: El nombre de un método no explica lo que hace el método.

Solución: Renombrar el método.

## Agregar Parámetro
Problema: Un método no tiene suficientes datos para realizar ciertas acciones.

Solución: Crear un nuevo parámetro para pasar los datos necesarios.

## Eliminar Parámetro
Problema: Un parámetro no se utiliza en el cuerpo de un método.

Solución: Eliminar el parámetro no utilizado.

## Separar Consulta de Modificador
Problema: ¿Tiene un método que devuelve un valor pero también cambia algo 
dentro de un objeto?

Solución: Dividir el método en dos métodos separados. Como era de esperar, 
uno de ellos debería devolver el valor y el otro modificar el objeto.

## Parametrizar Método
Problema: Varios métodos realizan acciones similares que son diferentes solo 
en sus valores internos, números u operaciones.

Solución: Combine estos métodos utilizando un parámetro que pase el valor 
especial necesario.

## Reemplazar Parámetro con Métodos Explícitos
Problema: Un método se divide en partes, cada una de las cuales se ejecuta 
según el valor de un parámetro.

Solución: Extraiga las partes individuales del método en sus propios métodos 
y llámelos en lugar del método original.

## Preservar Objeto Completo
Problema: Obtienes varios valores de un objeto y luego los pasas como 
parámetros a un método.

Solución: En su lugar, intente pasar el objeto completo.

## Reemplazar Parámetro con Llamada a Método
Problema: Llamando a un método de consulta y pasando sus resultados como 
parámetros de otro método, mientras ese método podría llamar a la consulta directamente.

Solución: En lugar de pasar el valor a través de un parámetro, intente colocar 
una llamada de consulta dentro del cuerpo del método.

## Introducir Objeto de Parámetros
Problema: Sus métodos contienen un grupo repetido de parámetros.

Solución: Reemplace estos parámetros con un objeto.

## Eliminar Método de Establecimiento
Problema: El valor de un campo debe establecerse solo cuando se crea, 
y no cambiar en ningún momento después de eso.

Solución: Eliminar los métodos que establecen el valor del campo.

## Ocultar Método
Problema: Un método no es utilizado por otras clases o se utiliza solo dentro 
de su propia jerarquía de clases.

Solución: Hacer que el método sea privado o protegido.

## Reemplazar Constructor con Método de Fábrica
Problema: Tiene un constructor complejo que hace algo más que simplemente 
establecer valores de parámetros en campos de objeto.

Solución: Cree un método de fábrica y úselo para reemplazar las llamadas al constructor.

## Reemplazar Código de Error con Excepción
Problema: ¿Un método devuelve un valor especial que indica un error?

Solución: En su lugar, arroje una excepción.

## Reemplazar Excepción con Prueba
Problema: Lanza una excepción en un lugar donde una prueba simple haría el trabajo?

Solución: Reemplace la excepción con una prueba