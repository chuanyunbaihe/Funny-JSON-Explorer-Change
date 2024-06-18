import argparse
import json
from Strategy import *
from IconFamily import IconFamily


def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='display style')
    parser.add_argument('-i', '--icon', required=False, choices=['star', 'pocker'], help='icon family')
    args = parser.parse_args()
    with open(args.file, 'r') as file:
        data = json.load(file)

    context = Context()
    if args.style == 'tree':
        context.set_strategy(TreeStrategy())
    elif args.style == 'rectangle':
        context.set_strategy(RectangleStrategy())
    else:
        raise ValueError(f"Unknown style: {args.style}")

    icon = IconFamily(args.icon)  # 选择图标族

    # 构造并呈现JSON树
    root = context.execute_strategy()
    root.show(icon, data)


if __name__ == '__main__':
    main()
