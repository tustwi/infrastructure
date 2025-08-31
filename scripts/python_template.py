import argparse
import logging

def main():
    parser = argparse.ArgumentParser(description="Template python script with logging.")
    parser.add_argument('--name', type=str, required=True, help='Your name')
    parser.add_argument('--level', type=str, default='INFO', help='Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
    parser.add_argument('--logfile', type=str, default='/var/log/python_template.log', help='Logging file location')
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.level.upper(), logging.INFO),
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=args.logfile,
        filemode='a'
    )

    logging.info(f"Hello, {args.name}!")
    logging.debug("This is a debug message.")
    logging.warning("This is a warning message.")

if __name__ == "__main__":
    main()