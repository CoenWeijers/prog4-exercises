import pygame

WIDTH = 800
HEIGHT = 600


class Bullet:
    def __init__(self, x, y):
        # De positie van de speler
        self.x = x
        self.y = y
        # De verplaatsing van een kogel op de Y-as
        self.y_change = -5

    def update(self):
        # We passen enkel de Y-positie aan, omdat de kogel enkel verticaal
        # beweegt
        self.y += self.y_change

    def blit(self, screen, img):
        screen.blit(img, (self.x, self.y))
class Enemy:
    def __init__(self, x, y):
        # De positie van de speler
        self.x = x   
        self.y = y
        # De verplaatsing van een kogel op de Y-as
        self.y_change = -5

    def update(self):
        # We passen enkel de Y-positie aan, omdat de kogel enkel verticaal
        # beweegt
        self.y += self.y_change

    def blit(self, screen, img):
        screen.blit(img, (self.x, self.y))


pygame.init()

# Maak een venster aan met de opgegeven resolutie
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Laad de "sprites" (afbeeldingen) in
player_img = pygame.image.load("ship.png").convert_alpha()
bullet_img = pygame.image.load("bullet.png").convert_alpha()
enemy_img = pygame.image.load("enemyship.png").convert_alpha()

# De positie van de speler
player_x = WIDTH / 2
player_y = 500

# De verplaatsing van de speler op de X-as
player_xchange = 0
PLAYER_SPEED = 5

# De posities van alle kogels als een lijst van X- en Y-coordinaten
bullets = []

# Positie van de vijand, en verplaatsing van de vijand
enemies = []
enemy_x_change = 0
enemy_y_change = 1

nieuwe_enemy = Enemy(x=player_x, y=player_y)

# Voeg een vijand toe op positie (100, 0)
enemies.append(nieuwe_enemy)
# Voeg een vijand toe op positie (400, 0)


# Een variabele die we op False kunnen zetten om uit de while-lus te geraken
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Als de speler op de spatiebalk drukt,
                # maak dan een nieuwe lijst aan met de X- en Y-coordinaat
                # van de nieuwe kogel
                nieuwe_kogel = Bullet(x=player_x, y=player_y)
                # Voeg deze lijst toe aan de lijst van kogels
                bullets.append(nieuwe_kogel)
            if event.key == pygame.K_LEFT:
                # Als de speler op het linkerpijltje drukt
                # stel dan de verplaatsing van de speler in naar links
                player_xchange -= PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                # Als de speler op het rechterpijltje drukt
                # stel dan de verplaatsing van de speler in naar rechts
                player_xchange += PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                # Als de speler het linkerpijltje loslaat
                # stel dan de verplaatsingsnelheid in op 0
                player_xchange = 0
            elif event.key == pygame.K_RIGHT:
                # Als de speler het rechterpijltje loslaat
                # stel dan de verplaatsingsnelheid in op 0
                player_xchange = 0

    # Verplaats de speler
    player_x += player_xchange
    for enemy in enemies:
        # Als de vijand nog leeft
        if enemy[2]:
            # Verplaats de vijand
            enemy[0] += enemy_x_change
            enemy[1] += enemy_y_change

            # Als de vijand buiten het scherm gaat,
            # plaats hem dan terug bovenaan het scherm
            if enemy[1] > HEIGHT:
                enemy[1] = 0

    # Verplaats de kogels door voor ieder element 
    # de update() functie uit te voeren.
    for bullet in bullets:
        bullet.update()

    # Veeg het scherm uit
    screen.fill("black")

    # Teken de speler
    screen.blit(player_img, (player_x, player_y))

    # Teken de vijand
    for enemy_x, enemy_y, enemy_alive in enemies:
        if enemy_alive:
            screen.blit(enemy_img, (enemy_x, enemy_y))

    # Teken alle kogels in de lijst
    for bullet in bullets:
        bullet.blit(screen, bullet_img)

    # Update het scherm
    pygame.display.flip()

    # Wacht zodanig dat we maximal 60 FPS halen
    clock.tick(60)  