"""
My first, self-made app.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from datetime import datetime
import pygame
import asyncio


class _37stretchtimer(toga.App):

    url = 'C:/Users/EB/Downloads/race-start-beeps-125125.mp3'
    stretch_time = 37

    def startup(self):
        main_box = toga.Box()

        # Initialize the button with the label "Start Timer"
        self.button = toga.Button(
            "Start Timer",
            on_press=self.toggle_timer,
        )

        self.second_button = toga.Button(
            "Reset",
            on_press=self.reset_timer,
        )
        self.second_button.style.visibility = 'hidden'
        self.text_input = toga.TextInput(value=f"00:{self.stretch_time}")


        main_box.add(self.button)
        main_box.add(self.text_input)
        main_box.add(self.second_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box

        self.main_window.show()

        # Initialize the timer state
        self.timer_running = False

        self.time_format = "%M:%S"
        self.time_object = datetime.strptime(self.text_input.value, self.time_format)

    async def update_input(self, timeformat):
        self.text_input.value = timeformat

    async def countdown_timer(self, seconds):
        while seconds >= 0 and self.timer_running:
            mins, secs = divmod(seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)

            await asyncio.sleep(1)
            await self.update_input(timeformat)

            print(timeformat)
            seconds -= 1
            if seconds == 3:
                self.play_sound()


        if self.timer_running:
            self.reset_timer(None)

            # await asyncio.sleep(1)

            asyncio.create_task(self.countdown_timer(self.stretch_time))
            self.timer_running = True
            # self.toggle_timer(None)

        # self.button.text = "Start Timer"
        # print("\nTimer complete!")
        # self.timer_running = False



    # "widget" is necessary. "button" creates it in background
    def toggle_timer(self, widget):
        try:
            if self.timer_running:
                # Stop the timer
                self.pause_timer()
                self.timer_running = False
                self.button.text = "Start Timer"
            else:
                # Update self.time_object with the current value of the text input
                self.time_object = datetime.strptime(self.text_input.value, self.time_format)

                # Start the timer
                total_seconds = self.time_object.minute * 60 + self.time_object.second
                asyncio.create_task(self.countdown_timer(total_seconds))
                self.timer_running = True
                self.button.text = "Pause"

        except ValueError:
            # Handle the ValueError, e.g., show a warning
            self.show_warning("Invalid Input", "Please enter a valid time in the format MM:SS")

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.url)
        pygame.mixer.music.play()

    def pause_timer(self):
        self.timer_running = False
        self.second_button.style.visibility = 'visible'

    def reset_timer(self, widget):
        # Reset the timer to its initial state
        self.text_input.value = f"00:{self.stretch_time}"
        self.second_button.style.visibility = 'hidden'

    def show_warning(self, title, message):
        # Create a warning dialog
        warning = toga.Window(title=title, size=(250, 50))

        # Add a label with the warning message
        warning_label = toga.Label(message, style=Pack(padding=10))
        warning.content = warning_label

        # Show the warning dialog
        warning.show()


def main():
    return _37stretchtimer()
