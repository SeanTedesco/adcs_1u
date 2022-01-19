# 1U Mock-Sat 
_Sean Tedesco | 2021-2022 | Queen’s University Student and Xiphos Systems Corporation Intern | Homo Sapien_

# Section 1.0: Introduction 

The Mock Sat is a 1U CubeSat capable of basic telemetry communications; power storage, distribution, and generation, attitude determination; and acquisition of temperature, pressure, and humidity measurements. In order to achieve these technical feats, the Mock Sat include the following subsystems: an electrical power system (EPS) for power storage, distribution, and charging; an attitude determination system (ADS) that produces 9-axis telemetry data; a data acquisition system (PAYLOAD) to collect temperature, pressure, and humidity data; communications system (COMMS) to transmit system health, telemetry and to receive user commands; an on-board computer (OBC) that acts as the central connection between the subsystems mentioned hitherto; a mechanical system (MECH) that encompasses the chassis housing all other subsystems. 

The Mock Sat is an education tool for the Queen’s Space Engineering Team in order to demonstrate a basic working implementation of each of the mentioned satellite subsystems. As such, it is beneficial to outline some learning objectives prior to any undertaking in order to align priorities. These learning objectives are described proceedingly. 

## 1.1 Simple PCB Design 
PCB designs shall be created using open source tools such as KiCad. 

## 1.2 OSI Network Model 
The 7-layer OSI model provides some pointers for code implementation. This is meant to be used as guiding principles to implement layers of abstraction for the microcontrollers as well as some of the sensors and devices, such as the COMMS radios, found on the cubesat. This is expanded on in Software Considerations. 

## 1.3 Advanced Hardware Features
 DMA, Interrupts, Resets, Watch Dogs are to be included in the scope of the cubesat project. 

## 1.4 Software Architecture 
(system managers, task routines)

First and foremost, decisions for this project are guided by the question: “Will this allow me to achieve the goal of an operating 1U cubesat the most efficiently?” 

#Hardware Considerations

Each subsystem is reduced in scope from a satellite that could be launched to space. This reduction in scope is made to reduce the time it takes to build this project, as well as reduce the cost of this project. This is to say that this 1U CubeSat will not be composed of flight hardware; assembled using cheap commercial, off-the-shelf (COTS) components. A complete BOM can be found in Appendix A - BOM. 

Some general considerations for hardware and mechanical design from a systems perspective include:
Have all areas of the cubesat that interact with the operator be located at the outside edges where at all possible. This includes LED indicator lights, charging ports, sd card slots, debugging ports. The motivation behind this is to eliminate the need to adjust and/or move the internal components of the cubesat. This prevents wear and tear, as well as some possible damage from 
The MECH subsystem has been typically left last in consideration in designing a cubesat on QSAT. This has resulted in over cramped designs, frustrations about fixing band aid solutions, providing a barrier to work on it intuitively, and performing the same adjustments over again. To mitigate this each of the subsystems in the cubesat will have a dedicated hardware section when the design is being undertaken. 
Software Considerations
The software architecture for this 1U cubesat is modelled after the 7-layer [OSI Network Model](https://en.wikipedia.org/wiki/OSI_model). The motivation for this is to provide layers of abstraction between the operator of the satellite and the individual hardware components, be able to have more than one person working on it at a time (people should be able to work on one layer without having to consider the layers above them), and have the software be contributed to with an aligned vision. I have interpreted and mapped the OSI model as a way to organize and structure the software, which is outlined below.  

| OSI MODEL LAYER | RELATION TO SOFTWARE ARCHITECTURE |
|PHY	| Have a controller be able to read / write to itself. |
|DATA	| Have a controller be able to read / write to other controllers. |
|NET  	| Have a controller be able to read / write to other controllers. |
|TRAN 	| Error checking, polling, request to send, clear to send. |
|SESS	| Implement a controller as a state machine. |
|PRES	| Format I/O data (from/to sensors, reaction wheels, camera, operator, ground station). |
|APP	| Receive / display raw I/O data (from/to sensors, reaction wheels, camera, operator, ground station).  |

Communications: Hardware
The objective of the communications (COMMS) system is, at the highest level, the ability to talk to the mock-sat from a distance. We are not going to quantitatively define the distance at which is sufficient for a successful design for the COMMS system. Since this project does not emphasize a scientific payload, thus mission performance does not drive design. We are concerned with getting something working. As such we are going to adopt a version of the [SWaP-C  strategy](https://www.baesystems.com/en-us/definition/what-is-swap-c#:~:text=SWaP%2DC%20is%20an%20acronym,device%2C%20system%2C%20or%20program.). Which is concerned with optimizing the size, weight, power, and cost of a system. With this strategy in mind, the requirements, and their corresponding justifications are given below. 

| # | Requirement		| Justification |
| 1 | Low Power 		| Power is limited for the entire satellite.  |
| 2 | Minimal Components 	| Reduces cost and complexity of the system.  |
| 3 | Minimal Volume 		| Space is limited for the entire satellite. |
| 4 | Minimal Cost 		| Project is more accessible if cheaper. |
| 5 | Swappable Components 	| Components break. |
| 6 | Visible System Status 	| Useful for debugging when no access to a serial monitor. |

The components used for the COMMS system include the following: 

| # | Component Name 	| Component Description | 
| 1 | Arduino Nano		| COMMS system controller |
| 2 | nRF24 Radio		| Implements wireless data transmissions |
| 3 | Capacitor 			| Required for nRF24 radio to regulate voltages |
Communications: Software
Requirements
Minimal manipulation of bytes between operator and satellite control logic. 
Does not interrupt operations of any other subsystem when performing system operations. 
Satellite communication remains reliable independent of the failure of other subsystems.
Handles commands from operator to satellite, 
Handles confirmations and data transfers from satellite to operator.

Steps 
RF24 Getting Started Example 
Groundstation and Satellite Code Split
Integrate Battery and Physical Indicators 
Mechanical
ADCS
Weighted rod for pointing? Saw this somewhere for a minimalist approach to ADCS. 
Python ADCS visualization
Figure out what quaternions are
Can you change orbit with an ADCS? If you change your center of gravity can that adjust your orbit? How does a satellite change its orbit? How does a satellite enter and stay into its orbit? 

MPU-650 -toast sat example code (lab4) has a Processing visualizer (check that out) 

For a build reference: 
https://charleslabs.fr/en/project-Reaction+Wheel+Attitude+Control 
https://github.com/CGrassin/reaction_wheel

Determine MOI for satellite: maybe use solid edge? 
On-Board Computer 
Electrical Power System 
Payload
Lab Overview 

Lab 1 - Communication Hardware
Lab 2 - Communication Software
Talk to something at a distance. 
Lab 3 - Power Hardware
Lab 4 - Power Software
Talk to something at a distance that is not tethered to anything. 
Lab 5 - OBC Hardware
Lab 6 - OBC Software
Talk to something at a distance that is not tethered to anything and does something simple. 
Lab 7 - Payload Hardware 
Lab 8 - Payload Software 
Talk to something at a distance that is not tethered to anything and does something cool. 
Lab 9 - Chassis Hardware 
Talk to something at a distance that is not tethered to anything and does something cool and can be easily held. 
Lab 10 - ADCS Hardware
Lab 11 - ADCS Software 
Talk to something at a distance that is not tethered to anything, does something cool, can be easily held, and can adjust its axis in 1 dimension. 

Nominal Layout 
Top - Reaction Wheel, Arduino Nano, MPU6050, Logic Shifter, Motor Driver 
Bottom - Arduino Nano, Radio, Antenna 
Front - Sensors 
Back - Raspberry PI
Left - Batteries, Arduino Nano, Charger, Booster 
Right - Cables and routing. 


Ideas
Mock-Sat Constellation 
Orbit Changing Satellite 
Appendix A - BOM
