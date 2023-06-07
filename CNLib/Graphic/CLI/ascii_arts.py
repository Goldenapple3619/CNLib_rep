HIDDEN_CARD: str = """┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘"""

EMPTY_CARD: str = """┌─────────┐
│         │
│         │
│         │
│         │
│         │
│         │
│         │
└─────────┘"""

TO_FILL_CARD: str = """┌─────────┐
│V        │
│         │
│         │
│    S    │
│         │
│         │
│        V│
└─────────┘"""

ASCII_CARD_SYMBOL: dict = {
    'spade':   '♠',
    'diamond': '♦',
    'heard':   '♥',
    'club':    '♣',
}

STYLIZED_ACE_DIAMOND: str = """.------.
|A.--. |
| :/\: |
| :\/: |
| '--'A|
`------'"""

STYLIZED_ACE_CLUBS: str = """.------.
|A.--. |
| :(): |
| ()() |
| '--'A|
`------'"""

STYLIZED_SPADE: str = """.------.
|A.--. |
| :/\: |
| (__) |
| '--'A|
`------'"""

STYLIZED_ACE_HEART: str = """.------.
|A.--. |
| (\/) |
| :\/: |
| '--'A|
`------'"""

WHITE_BOX: str = '■'

BLACK_BOX: str = '□'

ASCII_BOX_LIGHT: dict = {
    "horizontal": '─',
    "vertical": '│',
    "top_left": '┌',
    "top_right": '┐',
    "bottom_left": '└',
    "bottom_right": '┘',
    "intersect_right": '├',
    "intersect_left": '┤',
    "intersect_bottom": '┬',
    "intersect_top": '┴',
    "cross": '┼',

    "round_bottom_left": '╰',
    "round_bottom_right": '╯',
    "round_top_right": '╮',
    "round_top_left": '╭' ,

    "diagonal_right": '╱',
    "diagonal_left": '╲',
    "diagonal_cross": '╳',

    "semi_horizontal_left": '╴',
    "semi_horizontal_right": '╶',
    "semi_vertical_top": '╵',
    "semi_vertical_bottom": '╷',
}

ASCII_BOX_OTHER: dict = {

}

ASCII_BLOCKS: dict = {
    "full_100": '█',
    "full_75": '▓',
    "full_50": '▒',
    "full_25": '░',
    "full_0": ' ',

    "semi_down": '▄',
    "semi_top": '▀',

    "pixel": '■'
}

ASCII_CHESS_PIECES: dict = {
    "white_king": '♚',
    "white_queen": '♛',
    "white_rook": '♜',
    "white_pawn": '♟',
    "white_knight": '♞',
    "white_bishop": '♝',

    "black_king": '♔',
    "black_queen": '♕',
    "black_rook": '♖',
    "black_pawn": '♙',
    "black_knight": '♘',
    "black_bishop": '♗'
}
