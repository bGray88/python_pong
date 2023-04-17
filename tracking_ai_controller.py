"""Module tracking_ai_controller"""

import sdl2
import sdl2.ext
from velocity import *
from player_data import *

class TrackingAIController(sdl2.ext.Applicator):
  """Class TrackingAIController"""

  def __init__(self, miny, maxy):
    super(TrackingAIController, self).__init__()
    self.componenttypes = PlayerData, Velocity, sdl2.ext.Sprite
    self.miny = miny
    self.maxy = maxy
    self.ball = None

  def process(self, world, componentsets):
      for pdata, vel, sprite in componentsets:
        if not pdata.ai:
          continue

        centery = sprite.y + sprite.size[1] // 2
        if self.ball.velocity.vx < 0:
          if centery < self.maxy // 2:
            vel.vy = 3
          elif centery > self.maxy // 2:
            vel.vy = -3
          else:
            vel.vy = 0
        else:
          bcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
          if bcentery < centery:
            vel.vy = -3
          elif bcentery > centery:
            vel.vy = 3
          else:
            vel.vy = 0
