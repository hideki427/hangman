def hangman(word):
  wrong = 0
  stages =["",
           "________          ",
           "|                 ",
           "|       |         ",
           "|       O         ",
           "|     / | \       ",
           "|       |         ",
           "|     /   \       ",
           "|                 "
           ]
  retters = list(word)
  board = ["_"] * len(word)
  win = False
  print("ハングマンへようこそ！")
  while wrong < len(stages) -1 :
    print("\n")
    msg = "１文字を予想してね"
    chr = input(msg)
    if chr in retters :
      cind = retters.index(chr)
      board[cind] = chr
      retters[cind] = "$"
    else:
      wrong += 1
    print(" ".join(board))
    e = wrong + 1
    print("\n".join(stages[0:e]))
    if "_" not in board:
      print("あなたの勝ち！")
      print(" ".join(board))
      win = False
      break
  if not win:
    print("\n".join(stages[0:wrong + 1]))
    print("あなたの負け！正解は {}。".format(word))
    
hangman("cat")
