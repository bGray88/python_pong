"""Module player"""

import sdl2
import sdl2.ext
from velocity import *
from player_data import *
from tracking_ai_controller import *

class Player(sdl2.ext.Entity):
  """Class Player"""

  def __init__(self, world, sprite, posx=0, posy=0, ai=False):
    self.sprite = sprite
    self.sprite.position = posx, posy
    self.velocity = Velocity()
    self.playerdata = PlayerData()
    self.playerdata.ai = ai
