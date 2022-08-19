# Connect4

Argument interactive specifies that the program runs in interactive mode.

Argument [input_file] specifies an input file that contains an initial board state. This way we can start the program from a non-empty board state. If the input file does not exist, the program should just create an empty board state and start again from there.

Argument [computer-first/human-first] specifies whether the computer should make the next move or the human.

Argument [depth] specifies the number of moves in advance that the computer should consider while searching for its next move. In other words, this argument specifies the depth of the search tree. Essentially, this argument will control the time takes for the computer to make a move

The purpose of the one-move mode is to make it easy for programs to compete against each other, and communicate their moves to each other using text files.

Programming language: Python 3.9, tested on a linux-based OS running Python 3.8.5 and on Windows 10 Python 3.9.2

How to run: 
open terminal on a linux based OS, navigate to where 
maxconnect4.py, MaxConnect4Game.py, input_file and output_file are in the same directory, than run

(Linux)
python3 maxconnect4.py interative [input_file] [computer-next/human-next] [depth]

python3 maxconnect4.py one-move [input_file] [output_file] [depth]

or

(Windows 10)
open command prompt on Windows 10, navigate to where
maxconnect4.py, MaxConnect4Game.py, input_file and output_file are in the same directory, run

python maxconnect4.py interative [input_file] [computer-next/human-next] [depth]

python maxconnect4.py one-move [input_file] [output_file] [depth]
