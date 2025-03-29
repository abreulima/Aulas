import serial
import time

def receive_apc220_messages(serial_port, baud_rate=9600):
    """
    Receive messages from an APC220 wireless module connected via serial port.
    
    Parameters:
        serial_port (str): The serial port where APC220 is connected (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
        baud_rate (int): Baud rate for serial communication (default: 9600)
    """
    try:
        # Establish serial connection
        ser = serial.Serial(
            port=serial_port,
            baudrate=baud_rate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        
        print(f"Connected to APC220 on {serial_port} at {baud_rate} baud")
        print("Waiting for messages... (Press CTRL+C to exit)")
        
        while True:
            # Check if data is available to read
            if ser.in_waiting > 0:
                # Read the data
                received_data = ser.readline().decode('utf-8').strip()
                print(f"Received: {received_data}")
            
            # Small delay to prevent CPU overuse
            time.sleep(0.1)
            
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    finally:
        # Close the serial connection if it was opened
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed")

if __name__ == "__main__":
    # Replace with your actual serial port where APC220 is connected
    # Windows example: 'COM3'
    # Linux example: '/dev/ttyUSB0'
    # Mac example: '/dev/tty.usbserial-1410'
    SERIAL_PORT = '/dev/ttyUSB0'
    
    # Make sure this matches the baud rate configured on your APC220 modules
    BAUD_RATE = 9600
    
    receive_apc220_messages(SERIAL_PORT, BAUD_RATE)
