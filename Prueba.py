

from pymodbus.client import ModbusTcpClient

# Configuración del inversor (cambia la IP y el puerto según tu configuración)
INVERTER_IP = "192.168.1.100"  # Cambia esto por la IP real del inversor
PORT = 502  # Puerto por defecto de Modbus TCP

# Crear cliente Modbus TCP
client = ModbusTcpClient(INVERTER_IP, port=PORT)

# Conectar al inversor
if client.connect():
    print("Conectado al inversor")

    # Leer registros Modbus (ajustar dirección y cantidad según la documentación del inversor)
    response = client.read_holding_registers(0x100, 10, unit=1)

    if not response.isError():
        print("Datos del inversor:", response.registers)
    else:
        print("Error en la lectura:", response)

    client.close()
else:
    print("No se pudo conectar al inversor")
