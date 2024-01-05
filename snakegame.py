#am importat libraria pygame, libraria pygame este folosita pentru development in multimedia, cel mai bun exemplu ar fi jocurile facute
# folosind limbajul de programare python
import pygame as pg
# am importat selectia de numere aleatorii , rand range este pentru a reda numerele incluse intr o lista
from random import randrange
# am creat marimea ferestrei ce vreau sa o utilez folosind libraria pygame
WINDOW = 600
# am selectat marimea tile de care am nevoie pentru joc
#Tile =tile este folosit pentru repetarea array ului dorit 
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)] #lambda este pentru a selecta o mica functie anonyma, poate fi folosita doar la o expresie
snake = pg.rect.Rect([0,0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position() #comanda folosita pentru a fi pozitionat random 
length = 1
segments = [snake.copy()] #am folosit segments pentru copiera desenului facut mai jos incat sarpele sa poate sa creasca
snake_dir =(0,0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock() #folosita pentru cadrele pe secunda
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d:1}
#am setat in asa fel incat daca se intampla un eveniment, in cazul aceasta fiind apasare de taste , A,W,S,D sarpele sa se poata misca
# if event type este folosita pentru a specifica ce fel de eveniment se va intampla in timpul rulari codului
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d:1}

            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                 snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE , 0)
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)            

    screen.fill('black')
    # marginele ecranului
    self_eating = pg.Rect.collidelist(snake, segments [:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or  snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0,0)
        segments = [snake.copy()]
       
    #verificarea pozitionari marului
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    # desenarea marului
    pg.draw.rect(screen,'red',food)
    #desenarea sarpelui
    [pg.draw.rect(screen,'pink' , segment )for segment in segments]
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments [-length:]
    pg.display.flip()
    clock.tick(60)        
