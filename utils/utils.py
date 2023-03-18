"""
This file contains information needed throughout the program.
"""


hangman_levels = {
    "1": {
        "level_type": "beginner",
        "lives": 9,
        "stages": [
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                |    ▭  ▭
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                |    ▭
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |      |
                |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |
                |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |
                |
                |
                |
                |
                ------------
            """
        ]
    },
    "2": {
        "level_type": "intermediate",
        "lives": 6,
        "stages": [
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |
                |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |
                |
                |
                |
                |
                ------------
            """
        ]
    },
    "3": {
        "level_type": "expert",
        "lives": 4,
        "stages": [
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |      O
                |
                |
                |
                |
                ------------
            """,
            """
                --------
                |      |
                |
                |
                |
                |
                |
                ------------
            """
        ]
    }
}






