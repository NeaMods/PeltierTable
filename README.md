# NeaHeater   [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

Heater/Cooler stage control software and design files for neaSNOM/neaSCOPE microscopes

## Software installation

Launch the main application file: **heaterApp.py**

This software was designed to run on Windows 10. However, we used Python modules that should allow cross-platform 
operation.

⚠️⚠️⚠️COM port listing: when using other operation systems, please modify the COM port addressing part of the code accordingly⚠️⚠️⚠️

Requirements can be found in the `requirements.txt` file.

The Python module for the communication protocol of the Controller has to be installed from **(https://github.com/spomjaksilp/pyMeCom)**

## Parts list
- Custom-made microscope stage: aluminum frame (frame.stl file) + heatsink (https://hu.rs-online.com/web/p/hutobordak/5040772?gb=b)
- Peltier element (Thorlabs TECD2S and TECF2S)
- Peltier/TEC controller (Meerstetter TEC-1091 (±4 A / ±21 V))
- Plastic box with connectors (ElectronicsBox.stl and topCover.stl file)

### Device control

#### Thermoelectric controller
The Peltier elements are controlled with a Meerstetter TEC-1091 precision Peltier temperature controller. Product page: https://www.meerstetter.ch/products/tec-controllers/tec-1091

For easy customization and assembly, we use the screw terminal block version. For the temperature sensor, we use Pt1000 RTD (https://uk.rs-online.com/web/p/rtd-sensors/1699928). 

#### 3D printed box for the electronics
You will find the STL file to 3D print the box to house the electronic board and the connections. 

Our version looks like this:
![cad_design](/Images/cad_design.png)

#### Connectors

We used a D-Sub 9 pins connector for both terminals, thus all GPIO and sensor pins of the controller are available and accessible through the two D-Sub 9 pins ports on the box. The input and the output ports are DC power plugs.

#### Wiring

The wiring between the controller pins and the D-Sub 9 pins pins is arbitrary. Here is an example of the sensor pins/D-Sub layout.
![wiring](/Images/TECcontroller_wiring.png)

Our version looks like this (colors and pins do not correspond to the design figure above):
![final_box](/Images/final_box.png)

### Peltier elements

In v1.0 we can accommodate two Peltier elements that we purchased from Thorlabs.

- TECD2S: https://www.thorlabs.com/thorproduct.cfm?partnumber=TECD2S
- TECF2S: https://www.thorlabs.com/thorproduct.cfm?partnumber=TECF2S

### Custom-made NeaSCOPE sample stage

The CAD files to build the sample stage with two, replaceable Peltier elements are located in the CAD directory. 
In v1.0 we modified a commercial heatsink from RS (https://hu.rs-online.com/web/p/hutobordak/5040772?gb=b) to dissipate the heat when cooling. The heatsink is integrated with the sample stage as the image shows below.

Our version looks like this:
![stage](/Images/heaterStage_hardware.png)

## Performance

The image below shows the temperature response and stability of the heating stage.
![controllapp_new](/Images/controllapp_new.png)

### License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
