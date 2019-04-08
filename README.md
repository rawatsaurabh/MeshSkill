# MeshSkill - Draft Version
Sample Skill to interact with the BlueNRG Mesh

The binaries are provided in .bin format and can be flashed into the SoC/micro-controller flash memory using one of the procedures described below. 

- Procedure 1 (.bin only) -

 1 - Plug the Eval Board to the host PC using a micro-USB cable. The board will be recognized as an external memory device called "BlUENRG-1" or "BLUENRG-2".
 2 - Drag and drop or copy the binary file into the "BlUENRG-1(IDB007VX)/BLUENRG-2(IDB008VX)" device you see in Computer.
 3 - Wait until flashing is complete.

- Procedure 2 (.hex and .bin) -

 1 - Install BlueNRG-1 ST-Link Utility http://www.st.com/en/embedded-software/stsw-bnrg1stlink.html
 2 - Plug the Eval Board to the host PC using a micro USB cable.
 3 - Open the BlueNRG-1 ST-Link utility.
 4 - Connect to the board selecting "Target -> Connect" from the menu or pressing the corresponding button.
 5 - Open the binary file selecting "File -> Open File..." and choose the one you want to flash.
 6 - From the menu choose: "Target -> Program"
 7 - Click Start.
 8 - Wait until flashing is complete.


