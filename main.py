class Obstacle: #in this i defiend three important functions for the obstacles:
    def __init__(self, image, type): #function 1: this function is a constructor will bring the img and the type
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self): #finction 2: this function will make the obstacle disapear after the player pass it
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN): #finction 3: this function will make the obstacle displayed on the screan
        SCREEN.blit(self.image[self.type], self.rect)

        
#Here i created three classes (large and small cactus and bird)
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
