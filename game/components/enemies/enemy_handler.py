from game.components.enemies.ship import Ship

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.timer = 0
        self.delay = 200
    
    def update(self):
        self.timer += 1
        if self.timer >= self.delay:
            self.enemies.append(Ship())
            self.timer = 0
        for enemy in self.enemies:
            enemy.update()

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)