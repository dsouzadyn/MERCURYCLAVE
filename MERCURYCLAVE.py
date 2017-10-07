import argparse
import base64
from utils import *

def tool_decoder(file_name):
    prev_string = ''
    try:
        with open(file_name, 'rb') as encoded_file:
            content = encoded_file.read()
            if isinstance(content, bytes):
                # Python3 compatibility handing. Reading files without encoding returns butes, not a string
                # We need convert the bytes to a str
                content = content.decode('utf-8')
            decoded_string = "".join(content.split())
        if is_valid_b64(decoded_string):
            while is_valid_b64(decoded_string):
                try:
                    prev_string = decoded_string
                    decoded_string = base64.b64decode(decoded_string)
                except Exception as e:
                    break
            if is_valid_ascii(decoded_string):
                print_info(decoded_string)
            else:
                print_info(prev_string)
            # True for successful decoding
            return True

        else:
            print_error(
                "Hmm, seems like the file isn't base64 encoded or there's nothing in the file.")
    except Exception as e:
        print_error("Unable to open file named '{0}'".format(file_name))

    # Return False for failed decoding
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='File to be base64 decoded.')
    args = parser.parse_args()

    tool_decoder(args.file)

if __name__ == '__main__':
    main()
