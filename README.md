# IOT-project-Temperature-Dependent-Auto-Cooling-System-
Read data from the sensor and Control the actuator according to the reading from the sensor

### IOT
  Creating an interactive environment
  
  Network of devices connected together
     
     
### Sensor


  Electronic element
  
  Converts physical quantity into electrical signals 
  
  Can be analog or digital
  
        #### DHT Sensor
   
         Digital Humidity and Temperature Sensor (DHT)
         PIN1,2,3,4(fromleftto right)
         PIN1-3.3V-5VPower supply
         PIN2-Data
         PIN3-Null
         PIN4-Ground
        


###  Actuator
  Mechanical/Electro-mechanical device
  
  Converts energy into motion
  
  Mainly used to provide controlled motion to other components

        #### Relay
         Mechanical/electromechanical switch
         3 output terminals (left to right)  NO (normal open):
         Common
         NC (normal close)
        
        
        
  ## Requirements

    DHT Sensor
    4.7K ohm resistor  Relay
    Jumper wires
    Raspberry Pi
    Mini fan
 
 
 ![REquirements](/REquirements.jpg)
   
 
   ## Adafruit DHT Library
   
    Adafruit provides a library to work with the DHT22 sensor
     Install the library in your Pi-  Get the clone from GIT
    git clone https://github.com/adafruit/Adafruit_CircuitPython_DHT
     Go to folder Adafruit_CircuitPython_DHT     cd Adafruit_CircuitPython_DHT
     Install the library
    sudo python setup.py install

                    
