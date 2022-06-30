from controller import Robot

robot=Robot()

timestep=320

flag= 0

leg1=robot.getDevice("front_left")
leg2=robot.getDevice("front_right")
leg3=robot.getDevice("back_left")
leg4=robot.getDevice("back_right")

while (robot.step(timestep) !=-1):    

    if(flag%10==0):
        leg1.setPosition(-0.3)
    elif(flag%10==2):
        leg2.setPosition(-0.3)
    elif(flag%10==4):
        leg4.setPosition(-0.3)
    elif(flag%10==6):
        leg3.setPosition(-0.3)
        

    elif(flag%10==7):
        leg1.setPosition(0.2)
        leg2.setPosition(0.2)
        leg4.setPosition(0.2)
        leg3.setPosition(0.2)
    
    flag=flag+1