import argparse
import tiktoken
from dataclasses import dataclass


@dataclass
class Args:
    file: str
    model: str


def num_tokens_from_string(string: str, encoding) -> int:
    """Returns the number of tokens in a text string."""
    num_tokens = len(encoding.encode(string))
    return num_tokens


def main(args: Args):
    print(f"File: {args.file}, Model: {args.model}")
    filepath = args.file
    model = args.model

    try:
        file = open(filepath, "r")
        file_text = file.read()
        file.close()
    except FileNotFoundError:
        print("File not found")
        exit(1)

    encoding = tiktoken.encoding_for_model(model)
    print(num_tokens_from_string(file_text, encoding))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="TokenChecker",
        description="Get amount of tokens in a specific file")
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-m', '--model', required=False,
                        default="gpt-4")
    args = Args(**vars(parser.parse_args()))

    main(args)
