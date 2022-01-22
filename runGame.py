import sof
import gameState

gs = gameState.GameState()

sof.printGame()

while(gs.checkQuit()):
    sof.game(gs)