# This program is used to calculates the voltage, resistance, current, and power in a circuit (needs 2 values) 
def main() -> None:
    print('---------------------------------------------------')
    print('Leave empty if value is not known (must know 2 values)')
    voltage = input('What is your voltage?: ')
    resistance = input('What is your resistance?: ')
    current = input('What is your current?: ')
    if voltage == '':
        voltage = float(current) * float(resistance)
    if current == '':
        current = float(voltage) / float(resistance)
    if resistance == '':
        resistance = float(voltage) / float(current)
    power = float(voltage) * float(current)
    print('---------------------------------------------------')
    print(f'Voltage: {voltage}V')
    print(f'Resistance: {resistance} Ohms')
    print(f'Current: {current} Amps')
    print(f'Power: {power} Watts')

if __name__ == '__main__':
    main()
