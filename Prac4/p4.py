# Import libraries
import RPi.GPIO as GPIO
import random
import ES2EEPROMUtils
import os
import time

# some global variables that need to change as we run the program
end_of_game = None  # set if the user wins or ends the game

# DEFINE THE PINS USED HERE
LED_value = [11, 13, 15]
LED_accuracy = 32
btn_submit = 16
btn_increase = 18
buzzer = 33
eeprom = ES2EEPROMUtils.ES2EEPROM()


# Print the game banner
def welcome():
    os.system('clear')
    print("  _   _                 _                  _____ _            __  __ _")
    print("| \ | |               | |                / ____| |          / _|/ _| |")
    print("|  \| |_   _ _ __ ___ | |__   ___ _ __  | (___ | |__  _   _| |_| |_| | ___ ")
    print("| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  \___ \| '_ \| | | |  _|  _| |/ _ \\")
    print("| |\  | |_| | | | | | | |_) |  __/ |     ____) | | | | |_| | | | | | |  __/")
    print("|_| \_|\__,_|_| |_| |_|_.__/ \___|_|    |_____/|_| |_|\__,_|_| |_| |_|\___|")
    print("")
    print("Guess the number and immortalise your name in the High Score Hall of Fame!")


# Print the game menu
def menu():
    global end_of_game
    option = input("Select an option:   H - View High Scores     P - Play Game       Q - Quit\n")
    option = option.upper()
    if option == "H":
        os.system('clear')
        print("HIGH SCORES!!")
        s_count, ss = fetch_scores()
        display_scores(s_count, ss)
    elif option == "P":
        os.system('clear')
        print("Starting a new round!")
        print("Use the buttons on the Pi to make and submit your guess!")
        print("Press and hold the guess button to cancel your game")
        value = generate_number()
        while not end_of_game:
            pass
    elif option == "Q":
        print("Come back soon!")
        exit()
    else:
        print("Invalid option. Please select a valid one!")


def display_scores(count, raw_data):
    # print the scores to the screen in the expected format
    print("There are {} scores. Here are the top 3!".format(count)) 
    # print out the scores in the required format
    pass


# Setup Pins
def setup():
    # Setup board mode
    GPIO.setmode(GPIO.BOARD)

    # Set LED's and Buzzer pins to output mode 
    GPIO.setup(LED_value, GPIO.OUT, initial=GPIO.LOW)    #LED 0 pin 11, LED 1 pin 13, LED 2 pin 15
    GPIO.setup(LED_accuracy, GPIO.OUT, initial=GPIO.LOW) #set LED on pin 32 
    GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)       #set buzzer as output pin 33
    #all outputs set with LOW initial state

    # Set submit and increase button pins to output mode   
    GPIO.setup(btn_submit, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button submit set as input pin 16  
    GPIO.setup(btn_increase, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button increase set as input pin 18 
    #all inputs use Pull_Up resistors becuase they are externally connected to ground.

    LED_brightness = GPIO.PWM(LED_accuracy, 100)
    buzzer_pwm = GPIO.PWM(buzzer, 1)
    
    # Setup debouncing and callbacks
    GPIO.add_event_detect(btn_increase, GPIO.FALLING, callback=btn_increase_pressed, bouncetime=200) #for increasing guess value
    GPIO.add_event_detect(btn_submit, GPIO.FALLING, callback=btn_guess_pressed, bouncetime=200) # for submiting guess
    
    
    
    
    
    pass


# Load high scores
def fetch_scores():
    # get however many scores there are
    score_count = None
    # Get the scores
    
    # convert the codes back to ascii
    
    # return back the results
    return score_count, scores


# Save high scores
def save_scores():
    # fetch scores
    # include new score
    # sort
    # update total amount of scores
    # write new scores
    pass


# Generate guess number
def generate_number():
    return random.randint(0, pow(2, 3)-1)


# Increase button pressed
def btn_increase_pressed(channel):
    # Increase the value shown on the LEDs
    guess = [0,0,0]
    for i in guess: #populate guess with pinstates of 
    	guess[i] = GPIO.input(LED_value[i])
    	
    guess_int = int("".join([str(j) for j in guess]),2)
    guess_int++
    if guess_int > 7: #wraps aroud for values above 7
    	guess_int = 1
    
    new_val = [int(x) for x in bin(guess_int)[2:]]
    
    for l in new_val:
    	GPIO.output(LED_value[l], new_val[l]) #writes out to leds
    
    
    	
    
    #GPIO.output(LED_value, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(LED_value, GPIO.LOW) #test to flash all lights for a second on increase
    # You can choose to have a global variable store the user's current guess, 
    # or just pull the value off the LEDs when a user makes a guess
    pass


# Guess button
def btn_guess_pressed(channel):
    # If they've pressed and held the button, clear up the GPIO and take them back to the menu screen
    time.sleep(0.3)
    if GPIO.input(channel) == 0:
    	welcome()
    
    guess = [0,0,0]
    for i in guess: #populate guess with pinstates of 
    	guess[i] = GPIO.input(LED_value[i])
    	
    guess_int = int("".join([str(j) for j in guess]),2)
    
    diff = abs(value - guess_int)
    switch diff{
    	case 1: 
    
    
    }
    	
    # Compare the actual value with the user value displayed on the LEDs
    # Change the PWM LED
    # if it's close enough, adjust the buzzer
    # if it's an exact guess:
    buzzer.stop()
    
    # - Disable LEDs and Buzzer
    # - tell the user and prompt them for a name
    # - fetch all the scores
    # - add the new score
    # - sort the scores
    # - Store the scores back to the EEPROM, being sure to update the score count
    pass


# LED Brightness
def accuracy_leds(difference):
    # Set the brightness of the LED based on how close the guess is to the answer
    # - The % brightness should be directly proportional to the % "closeness"
    # - For example if the answer is 6 and a user guesses 4, the brightness should be at 4/6*100 = 66%
    # - If they guessed 7, the brightness would be at ((8-7)/(8-6)*100 = 50%
    pass

# Sound Buzzer
def trigger_buzzer(difference):
    # The buzzer operates differently from the LED
    # While we want the brightness of the LED to change(duty cycle), we want the frequency of the buzzer to change
    # The buzzer duty cycle should be left at 50%
    
    buzzer_pwm.start(0.5)
    
    # If the user is off by an absolute value of 3, the buzzer should sound once every second
    # If the user is off by an absolute value of 2, the buzzer should sound twice every second
    # If the user is off by an absolute value of 1, the buzzer should sound 4 times a second
    pass


if __name__ == "__main__":
    try:
        # Call setup function
        setup()
        welcome()
        while True:
            menu()
            pass
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()
