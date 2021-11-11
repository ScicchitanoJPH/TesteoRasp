# Testeo de HBL

El objetivo de este proyecto es testear las interfaces del HBL. Para esto hay 4 etapas de testeo:

## Testeo de Salidas
_Para testear las salidas se conectaron 4 LEDs directo a las salidas de los 4 contectores de salida del HBL. En esta etapa el usuario debe verificar que los 4 LEDs enciendan,de ser asi
debe presionar '1', de no ser asi debera presionar '0'_

## Testeo de Entradas
_Para testear las entradas se conectaron 2 pulsadores normales abiertos directo a las entradas de los 2 contectores de entrada del HBL. En esta etapa el usuario tendra 10 segundos
para presionar cada boton. Si la Raspberry recibe el pulso de entrada validara la etapa de entrada como "OK", sino dara un error_

## Testeo de Puerto Serie
_Para testear el puerto serie se cortocircuitaron los pines de Tx y Rx, entonces la Raspberry envia un mensaje por el Tx y si se recibe el mismo mensaje por el pin Rx quiere decir
que el puerto serie esta funcionando perfectamente, de no ser asi el sistema lanzara un error_

## Testeo de Wiegand
_Para testear el Wiegand se cortocircuitaron los pines de Data0 y Data1 del trasmisor con los pines Data0 y Data1 del receptor respectivamente. Entonces, al igual que en el puerto
serie, se envia un mensaje por el trasmisor y se verifica que el receptor reciba dicho mensaje_
