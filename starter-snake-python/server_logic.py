import random
from typing import List, Dict

def avoid_myself(data,my_head,my_body,possible_moves):
  for body in my_body:
    if my_head['x'] +1 == body['x'] and body['y'] == my_head['y']:
      possible_moves.remove('right')
    elif my_head['x'] -1 == body['x'] and body['y'] == my_head['y']:
      possible_moves.remove('left')
    elif my_head['y'] +1 == body['y'] and body['x'] == my_head['x']:
      possible_moves.remove('up')
    elif my_head['y'] -1 == body['y'] and body['x'] == my_head['x']:
      possible_moves.remove('down')
  return possible_moves

def avoid_walls(data,possible_moves):
  my_head = data['you']['head']
  my_body = data['you']['body']
  boardc = data['board']
  if my_head['x']+1 == boardc['width'] and my_head['y']+1 == boardc['height']:
    possible_moves.remove("right")
    possible_moves.remove('up')
  elif my_head['x'] == 0 and my_head['y']+1 == boardc['height']:
    possible_moves.remove("left")
    possible_moves.remove("up")
  elif my_head['x']== 0 and my_head['y'] == 0:
    possible_moves.remove("down")
    possible_moves.remove("left")
  elif my_head['x'] +1 == boardc['width'] and my_head['y'] == 0:
    possible_moves.remove('down')
    possible_moves.remove("right")
  elif my_head['x']+1 == boardc['width']:
    possible_moves.remove('right')
  elif my_head['x'] == 0:
    possible_moves.remove('left')
  elif my_head['y']+1 == boardc['height']:
    possible_moves.remove("up")
  elif my_head['y'] == 0:
    possible_moves.remove("down")
  else:
    return possible_moves
  return possible_moves

def avoid_snakes(data,my_head,my_body,possible_moves):

  for snake in data['board']['snakes']:
    for body in snake['body']:
      if my_head['x']+1 == body['x']:
        possible_moves.remove("right")
      elif my_head['x']-1 == body['x']:
        possible_moves.remove("left")
      elif my_head['y']+1 == body['y']:
        possible_moves.remove("up")
      elif my_head['y']-1 == body['y']:
        possible_moves.remove("down")
    return possible_moves

def avoid_others(data,my_head,possible_moves):
  for snake in data['board']['snakes']:
    for body in snake['body']:
      if my_head['x']-1==body['x'] and body['y']==my_head['y']:
        if "left" in possible_moves:
          possible_moves.remove("left")
      if my_head['x']+1==body['x'] and body['y']==my_head['y']:
        if "right" in possible_moves:
          possible_moves.remove("right")
      if my_head['y']-1==body['y'] and body['x']==my_head['x']:
        if "down" in possible_moves:
          possible_moves.remove("down")
      if my_head['y']+1 == body['y'] and body['x']==my_head['x']:
        if "up" in possible_moves:
          possible_moves.remove("up")
  return possible_moves

def eat_food(data,my_head,possible_moves):

    my_health = data['you']['health']
    direction = []

    if my_health < 70: 
      if my_head['x'] < data['board']['food'][0]['x'] and 'right' in possible_moves:
        direction.append("right")
      if my_head['x'] > data['board']['food'][0]['x'] and 'left' in possible_moves:
        direction.append("left")
      if my_head['y'] < data['board']['food'][0]['y'] and 'down' in possible_moves:
        direction.append("down")
      if my_head['y'] < data['board']['food'][0]['y'] and 'up' in possible_moves:
        direction.append("up")
      return direction
    return direction


    
def choose_move(data: dict) -> str:
    
  my_head = data["you"]["head"]  
  my_body = data["you"]["body"] 
  my_head_x = data['you']['head']['x']
  my_head_y = data['you']['head']['y']
  board_width = data['board']['width']
  board_height = data['board']['height']

  possible_moves= ["right","left","up","down"]

  possible_moves= avoid_myself(data,my_head,my_body,possible_moves)

  possible_moves = avoid_walls(data,possible_moves)

  possible_moves = avoid_others(data,my_head,possible_moves)

  hungry = eat_food(data,my_head,possible_moves)

  if hungry == []:
    move = random.choice(possible_moves)
  elif len(hungry) > 0:
    move = random.choice(hungry)

  return move
        
