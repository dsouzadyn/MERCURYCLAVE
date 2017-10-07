import unittest
import shutil, tempfile
from os import path
import MERCURYCLAVE as m

class TestMercuryClave(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_decoding(self):
        # Create a file in the temporary directory
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        # double encoded text "hello this is a test"
        f.write('YUdWc2JHOGdkR2hwY3lCcGN5QmhJSFJsYzNRPQ==')
        f.close()

        decoding_succeeded = m.tool_decoder(path.join(self.test_dir, 'test.txt'))
        self.assertTrue(decoding_succeeded)

if __name__ == '__main__':
    unittest.main()
