# Snake

<div style="text-align:center;">
  <image src="https://github.com/JavierAM01/Machine-Learnig-in-Games/blob/main/images/snake.gif" style="width:100%; height:12cm;">
</div>
  
## Explicación
  
Creación del juego snake. Para ello necesitamos 3 objetos principales: la serpiente, la comida y el tablero.

### Serpiente.
  
Guardamos el cuerpo de la serpiente en una lista y por otro lado la posición de la cabeza.
  
```python
snake_pos = [10*DIM, 5*DIM]
snake_body = [[10*DIM, 5*DIM]]
```
  
y comenzamos el bucle de juego. Cada X segundos actualizamos la serpiente en la siguiente posición (acorde con su dirección), y posteriormente 
vemos si eliminar la anterior dependiendo de si ha comido o no.
  
```python
snake_body.insert(0, list(snake_pos))

if snake_pos == food_pos:
    food_pos = food()
    score += 1
else:
    snake_body.pop()
```

### Comida.
  
Se genera una nueva cada vez que la serpiente se come una. Para elegir el lugar buscamos una posición aleatoria en el tablero. Además 
comprobaremos que no colisione con la serpiente.
  
```python
def food():
    x_pos = random.randint(0,NX-1)*DIM
    y_pos = random.randint(0,NY-1)*DIM
    food_pos = [x_pos, y_pos]
    return food_pos  
```
  
### Tablero
  
Para la creación del tablero solamente dibujamos en el fondo líneas verticales y horizontales.
  
```python
for i in range(NY+1):
    pygame.draw.rect(play_surface, GRIS, pygame.Rect(0, i*DIM-1, ANCHURA, 2))
for i in range(NY+1):
    pygame.draw.rect(play_surface, GRIS, pygame.Rect(i*DIM-1, 0, 2, ALTURA))
```
