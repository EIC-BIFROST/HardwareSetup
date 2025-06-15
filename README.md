# HardwareSetup

### Camera Gimbal Calibration
1. Install Gimbal [Driver and Application](http://www.tarotrc.com/Download/Detail.aspx?Lang=en&Id=f742d38f-ee46-4321-b1b3-145c0d0a92d1)
2. Currently the camera should be facing down. Remove the orange camera bracket. (Be careful to not break the IMU sensor wires)
3. Re-attach the orange camera bracket so that the camera faces the front like the image below:

![camera gimbal](https://github.com/EIC-BIFROST/HardwareSetup/raw/main/images/gimbal_position.png)

4. Power on the gimbal
5. Connect the gimbal to your computer via USB hub
6. Open the **ZYX_T2_2D** application, select the right PORT and connect the gimbal
7. Ensure that the camera faces the front or else calibration will fail quietly
8. Once camera is in position, click the calibration in the program and hold the camera still
9. Click FLash Memory in the application and Disconnect
10. Re-attach the camera to be facing down
11. Test the stabilization