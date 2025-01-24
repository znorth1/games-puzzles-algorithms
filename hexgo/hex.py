"""
  * simple set-based hex environment    rbh 2024
  * similar to go.py
  * they both use hexgo.py, stone_board.py
"""
#   ideas from ...
#     * Michi (by Petr Baudis)
#     * Morat (by Timo Ewalds)
#     * Miaowy (by rbh)
#     * Benzene (by 
#         Broderick Arneson, Philip Henderson, Jakub Pawlewicz,
#         Aja Huang, Yngvi Bjornsson, Michael Johanson, Morgan Kan,
#         Kenny Young, Noah Weninger, Chao Gao, rbh)
#     * hex (by Luke Schultz)
#     * hsearch (by Owen Randall)

from hexgo import Cell, Color, Game, IO, Pt, UF
from stone_board import Stone_board
from time import time

b,w = 0,1
m33demo  = ((b,1,1),(w,0,0),(b,2,1),(w,2,2),(b,0,1),(w,0,2),(b,3,1),(w,0,3),(b,4,1))
m33tdemo  = ((w,1,1),(b,0,0),(w,0,2),(b,2,2),(w,2,0))
hw1 = ((b,0,1),(w,0,2),
       (b,1,2),(w,1,3),
       (b,1,1),(w,0,0),
       (b,2,0))

start_time = time()
hb = Stone_board(Game.hex_game, 5, 5)

for move in m33demo:
  hb.make_move(move)
'''
for sort_nbrs in (True, False):
  hb.bfs_demo(0, sort_nbrs)
  hb.dfs_demo(0, sort_nbrs, True)
  hb.dfs_demo(0, sort_nbrs, False)
'''
print('\ntime ', time() - start_time)
