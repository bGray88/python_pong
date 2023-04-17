"""Module pong"""

import sdl2
import sdl2.ext

class PlayerInput:
  """Class PlayerInput"""

  def controller(self, events, player):
    """Method controller"""

    for event in events:
      if event.type == sdl2.SDL_QUIT:
        return False
      if event.type == sdl2.SDL_KEYDOWN:
        if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
          return False
        if event.key.keysym.sym == sdl2.SDLK_UP:
          player.velocity.vy = -3
        elif event.key.keysym.sym == sdl2.SDLK_DOWN:
          player.velocity.vy = 3
      elif event.type == sdl2.SDL_KEYUP:
        if event.key.keysym.sym in (sdl2.SDLK_UP, sdl2.SDLK_DOWN):
          player.velocity.vy = 0
    return True