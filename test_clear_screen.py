from unittest import TestCase

from unittest.mock import patch

import io

from game import clear_screen


class TestClearScreen(TestCase):

    @patch('random.choice', return_value=92)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_clear_screen_full_logo(self, mock_stdout, _):
        clear_screen(0)
        expected = '\x1b[2J\x1b[H\x1b[1m\x1b[92m \n\n         ___           ___           ___           ___           ___       ___ \n        /\\  \\         /\\  \\         /\\  \\         /\\  \\         /\\__\\     /\\__\\\n       /::\\  \\       /::\\  \\       /::\\  \\       /::\\  \\       /:/  /    /:/  /\n      /:/\\:\\  \\     /:/\\:\\  \\     /:/\\:\\  \\     /:/\\:\\  \\     /:/  /    /:/  / \n     /::\\~\\:\\  \\   /::\\~\\:\\  \\   /::\\~\\:\\  \\   /:/  \\:\\  \\   /:/  /    /:/  /  \n    /:/\\:\\ \\:\\__\\ /:/\\:\\ \\:\\__\\ /:/\\:\\ \\:\\__\\ /:/__/ \\:\\__\\ /:/__/    /:/__/   \n    \\/_|::\\/:/  / \\:\\~\\:\\ \\/__/ \\/_|::\\/:/  / \\:\\  \\ /:/  / \\:\\  \\    \\:\\  \\   \n       |:|::/  /   \\:\\ \\:\\__\\      |:|::/  /   \\:\\  /:/  /   \\:\\  \\    \\:\\  \\  \n       |:|\\/__/     \\:\\ \\/__/      |:|\\/__/     \\:\\/:/  /     \\:\\  \\    \\:\\  \\ \n       |:|  |        \\:\\__\\        |:|  |        \\::/  /       \\:\\__\\    \\:\\__\\\n        \\|__|         \\/__/         \\|__|         \\/__/         \\/__/     \\/__/ \x1b[0m\x1b[91m \n                            ________ ________ _________\n                            ___  __ \\___  __ \\__  ____/\n                            __  /_/ /__  /_/ /_  / __\n                            _  _, _/ _  ____/ / /_/ /\n                            /_/ |_|  /_/      \\____/\n\n     \x1b[0m\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choice', return_value=92)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_clear_screen_mini_logo(self, mock_stdout, _):
        clear_screen(1)
        expected = '\x1b[2J\x1b[H\x1b[1m\x1b[92m \n   ________ ________ ________ ________ _________\n   ___  __ \\___  __ \\___  __ \\___  __ \\__  ____/\n   __  /_/ /__  /_/ /__  /_/ /__  /_/ /_  / __\n   _  _, _/ _  _, _/ _  _, _/ _  ____/ / /_/ /\n   /_/ |_|  /_/ |_|  /_/ |_|  /_/      \\____/\n\n\n\n \x1b[0m\n'
        self.assertEqual(expected, mock_stdout.getvalue())
