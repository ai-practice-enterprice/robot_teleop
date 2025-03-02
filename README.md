# robot_teleop
control robot white keyboard and joystick

## use
```bash
ros2 launch robot_teleop joystick.launch.py topic:=<control topic from the controller> use_sim_time:=<True if in sim>
```

### example:
- control jetracer in sim:
    ```bash
    ros2 launch robot_teleop joystick.launch.py topic:=/ackermann_steering_controller/reference use_sim_time:=True
    ```

- control jetank in sim:
    ```bash
    ros2 launch robot_teleop joystick.launch.py topic:=/diff_drive_controller/cmd_vel use_sim_time:=True
    ```