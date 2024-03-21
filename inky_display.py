
import requests
from bs4 import BeautifulSoup
import inkyphat
import time
# No need for schedule module in this version

def update_image():
    url = "https://www.gov.uk/terrorism-national-emergency"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    sentence = soup.find(text="The threat to the UK (England, Wales, Scotland and Northern Ireland) from terrorism is ")
    
    if sentence:
        next_word = sentence.find_next("strong")
        if next_word:
            next_word = next_word.text.strip().lower()
            print(f"Retrieved sentence: {sentence}")  # Debugging print
            print(f"Next word (image indicator): {next_word}")  # Debugging print
            if next_word in image_paths:
                inkyphat.clear()  # Clear the display
                inkyphat.set_image(image_paths[next_word])
                inkyphat.show()

inkyphat.set_colour("red")  # Specify the color of your Inky pHAT
inkyphat.set_image("/home/pi/inky/images/connecting.png")
inkyphat.show()
time.sleep(15)  # Wait 5 seconds on boot

image_paths = {
    "low": "/home/pi/inky/images/1.png",
    "medium": "/home/pi/inky/images/2.png",
    "substantial": "/home/pi/inky/images/3.png",
    "severe": "/home/pi/inky/images/4.png",
    "critical": "/home/pi/inky/images/5.png"
}



# Continuous loop to check for updates (alternative to schedule)
while True:
  update_image()
  time.sleep(43200)  # Update every 12 hours (43200 seconds)
