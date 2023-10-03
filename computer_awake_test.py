import pytest
import time
from unittest.mock import patch, MagicMock
from computer_awake import ComputerAwake


@pytest.fixture
def computer_awake():
    return ComputerAwake()


def test_start(computer_awake):
    # Start the key press interval
    computer_awake.start(interval=1, run_time=5)

    # Check that the thread is running
    assert computer_awake.thread.is_alive() is True

    # Wait for the interval to finish
    time.sleep(6)

    # Check that the thread is not running
    assert computer_awake.thread.is_alive() is False


def test_stop(computer_awake):
    # Start the key press interval
    computer_awake.start(interval=1, run_time=10)

    # Stop the key press interval
    computer_awake.stop()

    # Join the thread to ensure that it has stopped
    computer_awake.thread.join()

    # Check that the thread is not running
    assert computer_awake.thread.is_alive() is False


def test_pause_resume(computer_awake):
    # Start the key press interval
    computer_awake.start(interval=1, run_time=10)

    # Pause the key press interval
    computer_awake.pause()

    # Check that the interval is paused
    assert computer_awake.paused is True

    # Resume the key press interval
    computer_awake.resume()

    # Check that the interval is running
    assert computer_awake.paused is False


def test_reset_timer(computer_awake):
    # Start the key press interval with a short run time
    computer_awake.start(interval=1, run_time=5)

    # Wait for the interval to run for a short time
    time.sleep(1)

    # Pause the key press interval and reset the timer
    computer_awake.pause()
    computer_awake.reset_timer()

    # Resume the key press interval
    computer_awake.resume()

    # Wait for the interval to finish
    time.sleep(6)

    # Check that the total number of key presses is approximately equal to the original run time divided by the interval
    assert abs(computer_awake.press_count - 5) <= 1


def test_start_with_default_values(computer_awake):
    # Create a new instance of the ComputerAwake class without providing any arguments
    default_awake = ComputerAwake()

    # Check that the interval and run time attributes have their default values
    assert default_awake.interval == 210
    assert default_awake.run_time == float('inf')


def test_key_input():
    # Start the key press interval with a different key
    awake = ComputerAwake(key='ctrl', interval=1, run_time=5)
    awake.start()

    # Wait for the interval to finish
    time.sleep(6)

    # Check that the thread is not running
    assert awake.thread.is_alive() is False


def test_interval(computer_awake):
    # Start the key press interval with a shorter interval
    computer_awake.start(interval=0.5, run_time=5)

    # Wait for the key press interval to run
    time.sleep(1)

    # Check that the key was pressed multiple times
    assert computer_awake.press_count > 1

    # Wait for the key press interval to finish
    time.sleep(5)

    # Check that the key was pressed multiple times
    assert computer_awake.press_count > 4


def test_duration(computer_awake):
    # Start the key press interval with a shorter duration
    computer_awake.start(interval=1, run_time=3)

    # Wait for the key press interval to run
    time.sleep(4)

    # Check that the thread is not running
    assert computer_awake.thread.is_alive() is False

    # Check that the key was pressed multiple times
    assert computer_awake.press_count > 1


@patch('keyboard.press_and_release')
def test_key_press(mock_press_and_release, computer_awake):
    # Start the key press interval
    computer_awake.start(interval=1, run_time=5)

    # Wait for the key press interval to run
    time.sleep(1)

    # Check that the key was pressed at least once
    assert mock_press_and_release.call_count >= 1
