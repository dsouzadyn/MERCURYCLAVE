import argparse
import base64
import re
from utils import *


def tool_decoder(file_name):
    decoded_string = ''
    validator = re.compile(
        '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
    try:
        with open(file_name, 'rb') as encoded_file:
            decoded_string = "".join(encoded_file.read().split())
        if validator.match(decoded_string) != None:
            while True:
                try:
                    decoded_string = base64.b64decode(decoded_string)
                except Exception as e:
                    break
            print_info(decoded_string)
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
