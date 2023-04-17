"""Module pong"""

import sys
import sdl2
import sdl2.ext
from software_renderer import *
from player import *
from ball import *
from movement_system import *
from collision_system import *
from player_input import *

WHITE = sdl2.ext.Color(255, 255, 255)

def run():
  """Method run"""

  sdl2.ext.init()

  window = sdl2.ext.Window("The Pong Game", size=(800, 600))
  window.show()

  factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
  sp_ball = factory.from_color(WHITE, size=(20, 20))
  sp_paddle1 = factory.from_color(WHITE, size=(20, 100))
  sp_paddle2 = factory.from_color(WHITE, size=(20, 100))

  world = sdl2.ext.World()

  ball = Ball(world, sp_ball, 390, 290)
  ball.velocity.vx = -3

  movement = MovementSystem(0, 0, 800, 600)
  collision = CollisionSystem(0, 0, 800, 600)
  spriterenderer = SoftwareRenderer(window)
  aicontroller = TrackingAIController(0, 600)

  world.add_system(aicontroller)
  world.add_system(movement)
  world.add_system(collision)
  world.add_system(spriterenderer)

  player1 = Player(world, sp_paddle1, 0, 250)
  player2 = Player(world, sp_paddle2, 780, 250, True)

  aicontroller.ball = ball
  collision.ball = ball
  player_input = PlayerInput()
  
  running = True
  while running:
    events = sdl2.ext.get_events()
    running = player_input.controller(events, player1)
    
    sdl2.SDL_Delay(10)
    world.process()

if __name__ == "__main__":
  sys.exit(run())
