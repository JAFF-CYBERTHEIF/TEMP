import RPi.GPIO as GPIO
import time
import paramiko

# Set up the GPIO pin for the servo
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, 50) # 50Hz PWM frequency
servo_pwm.start(0) # Set the initial duty cycle to 0

# Connect to the SSH server on the computer
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('your_computer_ip_address', username='your_username', password='your_password')

# Define a function to map the joystick input to the servo duty cycle
def map_servo(value):
    # Map the joystick input range (0 to 255) to the servo duty cycle range (2 to 12)
    return (value / 255.0) * 10.0 + 2.0

# Loop to read the joystick inputs over SSH and control the servo
while True:
    # Read the joystick inputs over SSH
    stdin, stdout, stderr = ssh.exec_command('cat /dev/input/js0 | xxd -p -c 8')

    # Parse the joystick input values from the output of the SSH command
    data = stdout.readline().strip()
    if len(data) == 16:
        x = int(data[6:8] + data[4:6], 16) - 32768
        y = int(data[10:12] + data[8:10], 16) - 32768

        # Map the joystick inputs to the servo duty cycle
        duty_cycle = map_servo(x)

        # Set the servo duty cycle
        servo_pwm.ChangeDutyCycle(duty_cycle)

        # Wait for a short time to prevent jitter in the servo movement
        time.sleep(0.01)
