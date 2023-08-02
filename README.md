
# Cifrado Cesar

El cifrado César es un algoritmo de cifrado simple  funciona desplazando cada letra del mensaje un número fijo de posiciones hacia la derecha en el alfabeto. El nombre del cifrado proviene de Julio César, quien lo utilizaba para proteger comunicaciones militares.

Para entender como funciona el cifrado podemos seguir los siguientes pasos:

1.- Necesitamos determinar el numero de posiciones que se desplazara cada letra. 

2.- Convertir el mensaje original a minúsculas para simplificar el proceso de cifrado.

3.- Recorrer cada letra del mensaje original:

Si la letra es una letra del alfabeto, se desplaza hacia la derecha en el alfabeto el número de posiciones indicado por el desplazamiento. Si se llega al final del alfabeto, se vuelve al principio.
Si la letra no es una letra del alfabeto (por ejemplo, espacios, dígitos o caracteres especiales), se mantiene sin cambios.
El mensaje cifrado se forma al juntar las letras resultantes después del proceso de desplazamiento.

Para descifrar el mensaje cifrado, se realiza el proceso inverso. Se toma el mensaje cifrado y se desplaza cada letra hacia la izquierda en el alfabeto, utilizando el mismo desplazamiento utilizado en el cifrado.

El cifrado César es un algoritmo de sustitución monoalfabética simple, cada letra se reemplaza por otra letra del alfabeto, y siempre se aplica el mismo desplazamiento. Aunque es fácil de entender y aplicar, el cifrado César es muy vulnerable a ataques de fuerza bruta y no se considera seguro para proteger información confidencial en la actualidad.






