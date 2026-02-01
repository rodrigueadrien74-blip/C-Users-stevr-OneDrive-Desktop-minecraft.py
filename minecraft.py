from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(icon='ICON.PNG', title='Minecraft')

Sky(color=color.black)
player = FirstPersonController()
music = Audio(
    'Dash.mp3',
    loop=True,
    autoplay=True
)
player.gravity = 0.5
player.cursor.visible = True
window.fullscreen = True

# Blocs programmés avec couleur seulement
block_types = [
    {'name':'gason', 'color': color.green},
    {'name':'piere', 'color': color.gray},
    {'name':'bois', 'color': color.brown},
    {'name':'vitre', 'color': color.white},
]

selected_block = 0

class Block(Button):
    def __init__(self, position=(0,0,0), color_block=color.green):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color_block,
            scale=1,
            collider='box'
        )

    def input(self, key):
        global selected_block
        if self.hovered:
            # casser le bloc
            if key == 'left mouse down' and self.position.y > 0:
                destroy(self)
            # poser un bloc
            if key == 'right mouse down':
                Block(
                    position=self.position + mouse.normal,
                    color_block=block_types[selected_block]['color']
                )
            # quitter le jeu
            if key == 'escape':
                application.quit()

# Génération du sol
for x in range(-10, 10):
    for z in range(-10, 10):
        Block(position=(x, 0, z), color_block=color.green)

# Update : changer bloc + respawn
def update():
    global selected_block
    if held_keys['escape']:
        application.quit()
    if held_keys['1']:
        selected_block = 0
    if held_keys['2']:
        selected_block = 1
    if held_keys['3']:
        selected_block = 2
    if held_keys['4']:
        selected_block = 3
    if held_keys['r']:
        player.position = (0,1,0)

app.run()
