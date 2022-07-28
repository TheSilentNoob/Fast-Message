#! /bin/env python3

import random
import requests
from core.internet import CheckInternet
from os import system as cmd
from core.color import *
import sys
from time import sleep
from pathlib import Path
import os

# Start -------------------------------------
cmd("clear")  
cmd("figlet Fast Message | lolcat -d 50")
# --------------------------------------------

# Animation ---------

def animate():
	print("Loading:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
	animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■] \n"]

	for i in range(len(animation)):
		sleep(0.05)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()

# Verify wi-fi ---------------------------------

print(info + white + "Checking for internet connection..." + end)
if CheckInternet():
    print(good + green + "You're connected!" + end)
else:
    print(bad + red + "You're not connected!" + end)
    exit()
sleep(2)
cmd("clear")
cmd("figlet Fast Message | lolcat -d 50")

#-----------------------------------------------
# Directory -----------------------------------------

def cont_annu():
	while True:
		cont = input(red + "Do you wanna add some contacts to the directory ? : [Y/N] ")
		if cont == "Y":
			contact_ask = input("What person would you add to this page ? (person name) --> : ")
			number_ask = input("What phone number does he got ? (num with country code ) --> : ")
			sure_cont = input("Add " + contact_ask + " With as num : "+ number_ask  + " To this page ? [Y/N]")
			if sure_cont == "Y" or "y":
				animate()
				cmd("echo " + contact_ask + " - " + number_ask + ">> contact/contact.txt ")
			elif sure_cont == "N" or "n":
				animate()
				cmd("clear")
				cmd("figlet Fast Message | lolcat -d 50")
				break
			else:
				print(red + "FATAL ERROR : This is not a proposed answer !")
		if cont == "N":
			animate()
			cmd("clear")
			cmd("figlet Fast Message | lolcat -d 50")
			break
def create_cont_annu():
	while True:
		annu = input(red + "Do you want make a Directory page to save phone numbers ? [Y/N] : ")
		if annu == "Y":
			cmd("mkdir contact && touch contact/contact.txt")
			contact_ask = input("What person would you add to this page ? (persone name) --> : ")
			number_ask = input("What phone number does he got ? (num with country code ) --> : ")
			sure_cont = input("Add " + contact_ask + " With as num : "+ number_ask  + " To this page ? [Y/N]")
			if sure_cont == "Y":
				animate()
				cmd("echo " + contact_ask + " - " + number_ask + ">> contact/contact.txt ")
				cmd("clear")
				cont_annu()
			if sure_cont == "N":
				animate()
				cmd("clear")
				cmd("figlet Fast Message | lolcat -d 50")
				break
		if annu == "N":
			cmd("clear")
			cmd("figlet Fast Message | lolcat -d 50")
			break

path_to_file = 'contact/contact.txt'
path = Path(path_to_file)

if path.is_file():
	cont_annu()
else:
	create_cont_annu()
#-----------------------------------------------------
#Asking Region --------------------------------------------------
while True:
	reg = input(blue + "To which region would you send message : ")
	if reg == "inter":
		print(green + "OK you choose : International")
		animate()
		max_len=12
		cmd("clear")
		break
	elif reg == "us":
		print(green + "OK you choose:  US")
		animate()
		max_len=12
		cmd("clear")
		break
	elif reg == "ls" :
		print(green + "Available regions : " + white + "United States = us , International = inter")
	else:
		print(red + "FATAL ERROR : " +  white + "Unknown region")

 #------------------------------------------------------------------

# Asking requirements -----------------------------------------
cmd("figlet Fast Message | lolcat -d 50")
while True:
	number = input(yellow + "Target phone number : ")
	if number == "contact":
		cmd("cat contact/contact.txt")
	elif len(number) > max_len:
		animate()
		print(red + "The phone number is too big ! Please verify if the number is correct !")
	elif len(number) < max_len:
		animate()
		print(red + "The number is too short ! Please verify if number is correct ! ")
	elif len(number) == max_len:
		animate()
		print(green + "Ok ")
		sleep(2)
		cmd("clear")
		break

cmd("figlet Fast Message | lolcat -d 50")
message = input("Message : ")
animate()
cmd("clear")
cmd("figlet Fast Message | lolcat -d 50")
y_or_n = input(yellow + "Do you want modify your message ?  [Y/N] \n" + "Actual Message : " +  message + "\n" + " > : ")
while True:
	if y_or_n == "Y":
		cmd("clear")
		cmd("figlet Fast Message | lolcat -d 50")
		message = input(yellow + "Messsage : ")
		animate()
		cmd("clear")
		cmd("figlet Fast Message | lolcat -d 50")
		key = input(yellow + "Which key do you want to use to send message \n(If you are having an API key for textbelt you can type in here by default textbelt  : ") or "textbelt"
		break
	else:
		cmd("clear")
		cmd("figlet Fast Message | lolcat -d 50")
		key = input(yellow + "Which key do you want to use to send message \n(If you are having an API key for textbelt you can type in here by default textbelt  : ") or "textbelt"
		break
# RECAP ------------------------------------------------------------

cmd("clear")
cmd("figlet Recap | lolcat -d 50")

print(blue + "To recap :\nMessage to : " + number +"\nRegion : " + reg + " \nMessage :" + message + "\nKey : " + key )
#------------------------------------------------------------------
# Executing ------------------------------------
resp = requests.post('https://textbelt.com/text', {
	'phone': number,
	'message' : message,
	'key': key,
})
animate()

if "true" in resp.json():
	print(green + respo.json())
print(resp.json())

