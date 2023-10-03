import logging
import time
import threading
import keyboard
import argparse


class ComputerAwake:
    """
    This class holds functions to keep the computer awake.
    It expects a key as a string and an interval & run time, in seconds, as an int.
    Example: ComputerAwake('space', 2, 10) hits space every 2 seconds for 10 seconds.
    """

    def __init__(self, key='shift', interval=210, run_time=float('inf')):
        self.key = key
        self.interval = interval
        self.run_time = run_time
        self.current_run_time = run_time
        self.press_count = 0
        self.run = False
        self.paused = False
        self.thread = threading.Thread(target=self._run)

    def _run(self):
        """
        This function starts the key press interval. It will run until the current run time reaches 0 or the `run` attribute is set to False.
        """
        start_time = time.time()
        end_time = start_time + self.run_time
        self.press_count = 0
        while self.current_run_time > 0 and self.run is True:
            if self.paused:
                time.sleep(self.interval)
                continue
            if not self.run:  # Check if the run attribute is False
                break
            # Increment press_count only when the interval is not paused
            self.press_count += 1
            try:
                keyboard.press_and_release(self.key)
                # Log the key press to the CLI
                logging.info(
                    f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Key press: {self.key}")
            except Exception as e:
                # Log the error message to a file
                logging.error(f"An error occurred while pressing the key: {e}")
                # Exit the program
                raise SystemExit
            time.sleep(self.interval)
            self.current_run_time -= self.interval
            time_remaining = max(end_time - time.time(), 0)
            logging.info(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Time remaining: {time_remaining:.2f}s")

        self._stop_key_press_interval()

    def _stop_key_press_interval(self):
        """
        This function stops the key press interval.
        """
        self.current_run_time = 0
        self.run = False

    def start(self, interval=None, run_time=None):
        """
        This function starts the key pressing interval.
        The interval and run time can be set as optional arguments. If not provided, the default values set in the constructor will be used.
        """
        start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        logging.info(
            f"Starting key press interval at {start_time} for {self.run_time} seconds")
        if interval:
            self.interval = interval
        if run_time:
            self.current_run_time = run_time
            self.run_time = run_time
        self.run = True
        self.thread.start()

    def stop(self):
        """
        This function stops the key pressing interval.
        """
        self._stop_key_press_interval()

    def reset_timer(self):
        """
        This function resets the key pressing interval.
        """
        self.current_run_time = self.run_time

    def pause(self):
        """
        This function pauses the key press interval.
        """
        self.paused = True

    def resume(self):
        """
        This function resumes the key press interval.
        """
        self.paused = False
        self.current_run_time = self.run_time - \
            (self.press_count * self.interval)

    def join(self):
        """
        This function joins the thread created by the class.
        """
        self.thread.join()


if __name__ == '__main__':
    # Set up logging to print to the CLI
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser(
        description='Keep computer awake by simulating key press.')
    parser.add_argument('key', type=str, nargs='?',
                        default='shift', help='Key to simulate press')
    parser.add_argument('--interval', '-i', type=int, default=210,
                        help='Interval between key press (in seconds)')
    parser.add_argument('--runtime', '-r', type=int, default=float('inf'),
                        help='Total duration of key press simulation (in seconds)')
    args = parser.parse_args()

    awake = ComputerAwake(args.key, args.interval, args.runtime)
    awake.start()

    # Wait for the thread to finish
    awake.join()
