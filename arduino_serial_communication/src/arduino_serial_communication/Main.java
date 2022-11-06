package arduino_serial_communication;

//Using the jSerialComm external library to do serial data reading/transmission
import com.fazecast.jSerialComm.*;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		//Gets all ports as listed under Device Manager. Arduino is usually port 0
		SerialPort[] ports = SerialPort.getCommPorts();
		SerialPort port = null;
		for (SerialPort p: ports) {
			if (p.getDescriptivePortName().equals("Arduino Uno (COM3)")) {
				port = p;
			}
		}
		assert(port != null);
		System.out.println(port.getDescriptivePortName());
		
		int bytesRead = 0;
		int readLimit = 200;
		//Default 1 stop bit per word
		port.setBaudRate(9600);
		port.openPort();
		//Timeout of 0 means 
		//comPort.setComPortTimeouts(SerialPort.TIMEOUT_NONBLOCKING, 0, 0);	//Default behaviour. readBytes() will make 1 instant attempt to read the requested number of bytes. Make sure they are available in the buffer. 
		//comPort.setComPortTimeouts(SerialPort.TIMEOUT_READ_SEMI_BLOCKING, 100, 0);	//readBytes() won't return until timeout reached or at least 1 byte read. You may want to handle input in a separate thread.
		//comPort.setComPortTimeouts(SerialPort.TIMEOUT_READ_BLOCKING, 100, 0);	//readBytes() won't return until timeout reached or all bytes requested are read. You may want to handle input in a separate thread.
		try {
			while(bytesRead < readLimit) {
				while (port.bytesAvailable() <= 0) Thread.sleep(20);
				byte[] readBuffer = new byte[port.bytesAvailable()];
				int numRead = port.readBytes(readBuffer, readBuffer.length);
				System.out.println("Successfully read " + numRead + " bytes: ");
				
				for (byte b : readBuffer) {
					System.out.print((char)b);
				}
				System.out.println();
				bytesRead += numRead;
			}
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		port.closePort();
		
	}

}
