import argparse

import psutil

parser = argparse.ArgumentParser()

parser.add_argument('--filter', type=str, default='core', help='Item label must contain this keyword.')
parser.add_argument('--sensor', type=str, default='coretemp', help='Which sensor to check.')
parser.add_argument('--list_all', action='store_true', help='Display all.')


def main():
    args = parser.parse_args()
    if args.list_all:
        print(psutil.sensors_temperatures())
        return
    
    temps = psutil.sensors_temperatures()[args.sensor]

    for temp in temps:
        if args.filter in temp.label.lower():
            print(f'{temp.label}: {temp.current:.0f}°C')


if __name__ == '__main__':
    main()
