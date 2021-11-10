from time import sleep,time
import RPi.GPIO as GPIO

pir_pin = (17,27,22)
lock_pin = (10,9,11)
buzz_pin = (25,8,7)

start = 0

def pin_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	for x in range(0,3):
		GPIO.setup(pir_pin[x],GPIO.IN)
		GPIO.setup(lock_pin[x],GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(buzz_pin[x],GPIO.OUT,initial=GPIO.LOW)
	
def read_pir(ind):
	return GPIO.input(ind)

def buzzing(num,delay):
	GPIO.output(buzz_pin[num],True)
	sleep(delay)
	GPIO.output(buzz_pin[num],False)

def locking():
	pass

def main():
	inp = read_pir(pir_pin[0])
	print(inp)
	if inp == 1:
		buzzing(0,0.1)
		sleep(2)
	# inp = read_pir(pir_pin[0])
	# print(inp)
	# if inp == 1:
		# start = time() 
		# while (read_pir(pir_pin[0]) != 0):print(read_pir(pir_pin[0]))
		# print(time()-start)
		# sleep(3)

if __name__ == "__main__":
	pin_setup()
	while True:
		main()
		
	
'''
<<if want to use gpiozero module>>
https://github.com/gpiozero/gpiozero

# from gpiozero import MotionSensor

# pir = MotionSensor(pin)

# while True:
	# print(pir.wait_for_motion())
	# print("moved")
	# print(pir.wait_for_no_motion())
'''
