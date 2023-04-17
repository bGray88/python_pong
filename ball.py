"""Module movement_system"""

import sdl2
import sdl2.ext
from velocity import *

class Ball(sdl2.ext.Entity):
  """Class Ball"""

  def __init__(self, world, sprite, posx=0, posy=0):
    self.sprite = sprite
    self.sprite.position = posx, posy
    self.velocity = Velocity()