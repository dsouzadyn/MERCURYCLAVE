import argparse
import base64
from utils import *


def tool_decoder(file_name):
    prev_string = ''
    try:
        with open(file_name, 'rb') as encoded_file:
            decoded_string = "".join(encoded_file.read().split())
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
        else:
            print_error(
                "Hmm, seems like the file isn't base64 encoded or there's nothing in the file.")
    except Exception as e:
        print_error("Unable to open file named '{0}'".format(file_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='File to be base64 decoded.')
    args = parser.parse_args()

    tool_decoder(args.file)

if __name__ == '__main__':
    main()
