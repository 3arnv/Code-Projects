import chess

import chess.engine

def play_chess():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")  # Adjust the path to your Stockfish engine

    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Enter your move: ")
            try:
                board.push_san(move)
            except (ValueError, chess.IllegalMoveError):
                print("Invalid move. Try again.")
                continue
        else:
            result = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(result.move)
            print(f"Bot move: {result.move}")

    print("Game over")
    print(board.result())
    engine.quit()

if __name__ == "__main__":
    play_chess()