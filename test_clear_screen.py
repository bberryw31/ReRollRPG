from unittest import TestCase

from unittest.mock import patch

import io

from game import clear_screen


class TestClearScreen(TestCase):

    @patch('random.choice', return_value=92)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_clear_screen_full_logo(self, mock_stdout, _):
        clear_screen(0)
        expected = """\x1b[2J\x1b[H\x1b[1m\x1b[92m 

         ___           ___           ___           ___           ___       ___ 
        /\  \         /\  \         /\  \         /\  \         /\__\     /\__\\
       /::\  \       /::\  \       /::\  \       /::\  \       /:/  /    /:/  /
      /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/  /    /:/  / 
     /::\~\:\  \   /::\~\:\  \   /::\~\:\  \   /:/  \:\  \   /:/  /    /:/  /  
    /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/__/    /:/__/   
    \/_|::\/:/  / \:\~\:\ \/__/ \/_|::\/:/  / \:\  \ /:/  / \:\  \    \:\  \   
       |:|::/  /   \:\ \:\__\      |:|::/  /   \:\  /:/  /   \:\  \    \:\  \  
       |:|\/__/     \:\ \/__/      |:|\/__/     \:\/:/  /     \:\  \    \:\  \ 
       |:|  |        \:\__\        |:|  |        \::/  /       \:\__\    \:\__\\
        \|__|         \/__/         \|__|         \/__/         \/__/     \/__/ \x1b[0m\x1b[91m 
                            ________ ________ _________
                            ___  __ \___  __ \__  ____/
                            __  /_/ /__  /_/ /_  / __
                            _  _, _/ _  ____/ / /_/ /
                            /_/ |_|  /_/      \____/

     \x1b[0m
"""
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('random.choice', return_value=92)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_clear_screen_mini_logo(self, mock_stdout, _):
        clear_screen(1)
        expected = '''\x1b[2J\x1b[H\x1b[1m\x1b[92m 
   ________ ________ ________ ________ _________
   ___  __ \___  __ \___  __ \___  __ \__  ____/
   __  /_/ /__  /_/ /__  /_/ /__  /_/ /_  / __
   _  _, _/ _  _, _/ _  _, _/ _  ____/ / /_/ /
   /_/ |_|  /_/ |_|  /_/ |_|  /_/      \____/



 \x1b[0m
'''
        self.assertEqual(expected, mock_stdout.getvalue())
