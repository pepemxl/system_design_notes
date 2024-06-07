# FAQ

## Question 1

Quién usara la plataforma o los sistemas?

R. Esta data será utilizada por distintos equipos en analisis critico.

## Question 2

Esta información puede conteneter schemas muy complejos, o muchos campos altamente anidados(nested) ~ 10K.
Pregunta después de terminar lo basico seria escalarlo a 1M.

## Question 3

Que cantidad de data debe soportar el sistema?
R.

- Menor que un billon de usuarios
- 20 eventos por usuario al día
- 10kBs por evento

## Question 4

Rate de refresh?

R. Desde 1hora a un 1 día de retraso es aceptable.

## Question 5 

Qué latencia debería manajar?

- Menor a 5 minutos(usualmente para dashboards)
- Que podemos hacer para reducirlo a segundos?
