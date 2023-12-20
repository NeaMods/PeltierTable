
# TEC sample stage   [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

Here, we provide software and hardware design to build a thermoelectric cooler/heater (TEC) sample stage with precision temperature control.
The design is flexible and can be modified to fit any instrument. Our implementation is compatible with [neaSNOM/neaSCOPE](https://www.neaspec.com/) microscopes.

## Software installation

Launch the main application file: **heaterApp.py**

This software was designed to run on Windows 10. However, we used Python modules that should allow cross-platform 
operation.

⚠️ COM port listing: when using other operation systems, please modify the COM port addressing part of the code accordingly

Requirements can be found in the [requirements.txt](Software/requirements.txt) file.

The Python module for the communication protocol of the Controller has to be installed from [pyMeCom](https://github.com/spomjaksilp/pyMeCom)

# Components

## Commercial parts

- Custom-made microscope stage: [aluminum frame](CAD/frame.stl) + heatsink (https://hu.rs-online.com/web/p/hutobordak/5040772?gb=b)
- Peltier element (Thorlabs TECD2S and TECF2S)
- Peltier/TEC controller (Meerstetter TEC-1091 (±4 A / ±21 V))
- Plastic box with connectors (ElectronicsBox.stl and topCover.stl file)


## Electronics

### Thermoelectric controller

The Peltier elements are controlled with a Meerstetter TEC-1091 precision Peltier temperature controller. Product page: https://www.meerstetter.ch/products/tec-controllers/tec-1091

For easy customization and assembly, we use the screw terminal block version. For the temperature sensor, we use Pt1000 RTD (https://uk.rs-online.com/web/p/rtd-sensors/1699928). 

### 3D printed box for the electronics
You will find the STL file to 3D print the box to house the electronic board and the connections. 

Our version looks like this:
![cad_design](/Images/cad_design.png)

### Connectors

We used a D-Sub 9 pins connector for both terminals, thus all GPIO and sensor pins of the controller are available and accessible through the two D-Sub 9 pins ports on the box. The input and the output ports are DC power plugs.

### Wiring

The wiring between the controller pins and the D-Sub 9 pins pins is arbitrary. Here is an example of the sensor pins/D-Sub layout.
![wiring](/Images/TECcontroller_wiring.png)

Our version looks like this (colors and pins do not correspond to the design figure above):
![final_box](/Images/final_box.png)

### Peltier elements

In v1.0 we can accommodate two Peltier elements that we purchased from Thorlabs.

- TECD2S: https://www.thorlabs.com/thorproduct.cfm?partnumber=TECD2S
- TECF2S: https://www.thorlabs.com/thorproduct.cfm?partnumber=TECF2S

⚠️ To properly drive the Peltier elements, you have to give their characteristics and electronic properties (such as maximum current, resistance, voltage) to the TEC controller.

Here we provide the configuration files for our stage/peltier combinations. The configuration files can be uploaded to the controller via the [TEC Service Software](https://www.meerstetter.ch/products/tec-controllers/tec-1091) from the related downloads/software panel.

We provide here the two config files in this repository /Software/tecd2s_parameters.ini and /Software/tecf2s_parameters.ini

⚠️ It is likely that you have to retune the PID parameters of the controller. You can do this by using the autotune option of the TEC Service Software. For more information see the controller manual.

The CAD files to build the sample stage with two, replaceable Peltier elements are in the CAD directory. 
In v1.0 we modified a [commercial heatsink](https://hu.rs-online.com/web/p/hutobordak/5040772?gb=b) to dissipate the heat when cooling, which is integrated with the sample stage as the image shows below.

![stage](/Images/heaterStage_hardware.png)

## Performance

Temperature response and stability of the heating stage.

![controllapp_new](/Images/controllapp_new.png)

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
