# VIA INFORMATION

## Via Overview

### What Are Vias? 
Vias are metallic lined holes connected to the metal circuitry of a PCB that conduct an electrical signal between the different layers of the board.

### Why Do We Use Vias?
Using vias in a PCB design allows the designer to shorten the distance that a trace must be routed in order to complete its connection. Just as with the laundry chute, the via will drop the trace down onto another layer where there is a clear path, instead of wandering the long way around. 

## Types of Vias 

**Thru-Hole Via**: This is the type of via that is used most often in a circuit board. The holes are drilled all the way through the board with a mechanical drill bit and can get down to 6 mils in size.

**Buried Via:** This via only connects internal layers of the board and is useful for PCBs with very dense routing.

**Blind Via:** This via starts on either the top or bottom of the board but doesn’t go all the way through it.

## Using Vias In Our Design

**Signal Routing:** Most circuit boards will use a thru-hole via for signal routing placed on a grid. Denser boards, however, may also use blind or buried vias, while very dense boards will need microvias.

**Escape Routing:** Larger surface mount (SMT) components can usually have their escape, or fanout, routing done with thru-hole vias. In some cases, blind vias or microvias will be used. 

**Power Routing:** Since the vias used for power and ground nets will conduct more current, they are usually restricted to larger thru-hole vias, although blind vias may be used as well.

**Stitching Vias:** These vias are used to provide multiple connections to a plane and are, therefore, thru-hole or blind vias. For example, a sensitive area of circuitry may be surrounded by a strip of metal with vias stitched in it to connect to a ground plane for EMI protection.

**Thermal Vias:** In this case, a via is used to conduct heat from a component out through the internal plane layer that it is connected to. This usually requires a larger thru-hole or blind via and these vias are often in the pads of these devices as well.

## Sizing

- There aren’t necessarily any standard PCB via sizes in PCB manufacturing because PCB standard via sizes tend to vary between manufacturers and PCB fabricators. 
- However, there are commonly used drill sizes that many PCB manufacturers prefer to use, and they may refer to them as standard PCB drill sizes. 
- One of the most common sizes is 0.6 mm, but 0.2 mm and 0.3 mm are also commonly used. 

### JCLPCB Capabilities
- **Min. Via Hole Size:** For Single & Double Layer PCB, the minimum via hole size is 0.3mm; For Multi-Layer PCB, the minimum via hole size is 0.2mm.
- **Min. Via Diameter:** For Single & Double Layer PCB, the minimum Via diameter is 0.6mm; For Multi-Layer PCB, the minimum via diameter is 0.4mm.
- **Drill Hole Size:** Supports a minimum of 0.20 mm drill hole size, and a maximum of 6.30 mm dril hole size.



Space School - Level 2 Ideas
- build a 1U cubesat 
- 1-axis reaction wheel
- half duplex communications using nRF24 radios (send and wait for user-acknowledge)
- PCB design and assemply for all components (standardized sizing, via, traces, only to mate with headers and swappable parts)
- Ground Station CLI to control radio
- pi-camera and raspberry pi OBS
- obc 
