<header>
<h1>PROGRAMA &#10077;QPART&#10078; <sub>(Software de Termodinámica Estadística)</sub></h1>
Programa diseñado para el cálculo de funciones de partición de sistemas con uno o dos átomos.
</header>
		<h2>BIENVENIDA</h2>
		<p>Le damos la bienvenida al programa QPART, este programa ha sido desarrollado por Aarón Rodríguez e Ignacio
			Migliaro, alumnos del curso de termodinámica estadística del semestre Enero-Junio 2016, en la Universidad
			de Guanajuato.</p>
		<p>En este archivo usted encontrará la información básica del programa, así como los detalles correspondientes
			para su uso.</p>
		<h2>¿QUÉ ES QPART?</h2>
		<p>Es un programa desarrollado en Python&trade; que permite el cálculo numérico de las funciones de partición
			para un sistema químico de 1 o de 2 átomos. Fue desarrollado con el fin de encontrar las funciones de
			partición de forma rápida, ya que el cálculo manual es en ocasiones tedioso. </p>
		<h2>CARACTERISTICAS GENERALES:</h2>
		<p>Esta es la primer versión del programa (esperamos que si usted está interesado, pueda contribuir a mejorarlo),
			el programa está compuesto de 5 scripts (nosotros los llamamos calculadoras); cuatro que calculan las funciones
			de partición (electrónica, vibracional, rotacional y translacional) y uno que permite el cálculo de la función
			de partición total. Para que estos scripts puedan compilar adecuadamente es requesito tener Python&trade; instalado con
			el paquete 'math'. Cada script es llamado por otro llamado "QPART.sh", el cual corre en bash y basícamente consta
			de un menú interactivo con el que usted puede llamar a cualquiera de las calculadoras almacenadas en un directorio
			dado.</p>
		<p>Cuando usted hace selecciona la función de partición a calcular, el programa le pedirá los parámetros necesarios
			para el cálculo de esta, en este sentido usted debe de contar las propiedades de su sistema (p.ej. modos
			vibracionales, constantes de rotación, etc.) Una vez que el programa termina de pedirle los atributos necesarios
			arroja los valores calculados con estos parámetros.</p>
	<h2>USO:</h2>
	<p>El uso del programa es sencillo, pues por medio de opciones básicas usted puede decidir que funciones calcular y/o
		si desea salir del programa. Deje que el programa pregunte que hacer.</p>
	<p>Sin embargo debe tener bien en mente ciertos detalles para su uso adecuado:</p>
	<ul>
		<li>El programa solo puede calcular las funciones de partición de sistemas no degenerados (salvo en el estado basal
			electrónico). de modo que no es adecuado para el cálculo de, por ejemplo, la función de partición rotacional del
			CO<sub>2</sub> ya que está doblemente degenerado en uno de sus modos de rotación.</li>
		<li>La calculadora de funciones de partición translacionales puede calcular las funciones de partición de moléculas
			monoatómicas o de moléculas diatómicas, en ambos casos es necesario contar con la masa atómica de cada uno de los
			átomos en la molécula.</li>
		<li>Por el contrario, la calculadora de funciones de partición vibracionales solo puede calcular funciones de
			partición para sistemas de dos átomos. En este caso le pedirá que inserte el total de modos de vibración, el
			programa puede calcular hasta para cuatro modos de vibración (solo por si se le ocurre insertar más de dos modos
			vibracionales). Esta calculadora se encuentra implícita en el script para el cálculo de la función de partición
			total, de modo que si usted desea calcular la función de partición total de un sistema monoatómico, no se le
			recomienda usar esta opción.</li>
		<li>La calculadora de funciones de partición rotacional arroja el número de iteraciones que le tomó para hacer un
			cálculo confiable de la función de partición rotacional, esto lo consigue haciendo una diferencia de la función
			de partición calculada con la de la iteración anterior, de modo que cuando esta diferencia es menor o igual a
			1E-06 el cálculo termina y se indica el número de iteraciones seguidas para llegar a tal sensibilidad. Esta
			calculadora tambien presenta el cálculo a aproximación de altas temperaturas, lo compara con el cálculo normal
			e indica si la aproximación es buena o mala, esta funcionalidad no la presenta en la calculadora de función de
			partición total.</li>
		<li>La calculadora de funciones electrónicas es básicamente una trivia, le pregunta sobre el nivel de degeneración
			del estado basal de su molécula y le da una respuesta. En muchos casos no es necesario lanzar esta calculadora
			por la razón que ya ha de suponer.</li>
		<li>Considere que este programa fue desarrollado por estudiantes de química que apenas se introducen en el mundo
			de la programación, por lo que aún falta mucho por hacer.</li>
	</ul>
