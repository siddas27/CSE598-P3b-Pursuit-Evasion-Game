# CSE598-P3b-Pursuit-Evasion-Game

# Pre-requsites

1) Install all Tb3 packages
2) sudo apt install ros-melodic-slam-gmapping

# Gmapping with Turtlebot3

## Launch the world and gmapping package

1) roslaunch pursuit_evasion robot_mapping.launch

## To drive autonomously with Turtlebot3 to map(not suggested)

2) roslaunch turtlebot3_gazebo turtlebot3_simulation.launch

## Using teleop to move around and create map

2) roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

## Saving the created map

3) rosrun map_server map_saver -f ~/map
![](https://github.com/siddas27/CSE598-P3b-Pursuit-Evasion-Game/blob/master/packages/rviz_screenshot_2021_04_13-19_49_33.png)


![](https://github.com/siddas27/CSE598-P3b-Pursuit-Evasion-Game/blob/master/packages/rviz_screenshot_2021_04_13-20_20_50.png)

![](https://github.com/siddas27/CSE598-P3b-Pursuit-Evasion-Game/blob/master/packages/rviz_screenshot_2021_04_13-20_32_22.png)
