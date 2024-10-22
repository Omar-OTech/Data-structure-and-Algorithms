from preloaded import *

health = 100
position = 0
coins = 0


log = []
def roll_dice():
    log.append('roll_dice')
def move():
    log.append("move")
def combat():
    log.append("combat")
def get_coins():
    log.append("get_coins")
def buy_health():
    log.append("buy_health")
def print_status():
    log.append("print_status")
    


def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

main()

# Test Suite
def test_syntax_bug_fixes():
    # Testing if initial values are correct
    assert health == 100
    assert position == 0
    assert coins == 0

    # Reset log and run main to ensure it doesn't crash
    log.clear()
    main()

def test_runtime_error_bug_fixes():
    # Clear the log before every test to avoid any contamination
    log.clear()

    # Call main function and check if the steps are executed in the correct order
    main()
    assert log[0] == 'roll_dice', f"Expected 'roll_dice' but got {log[0]}"
    assert log[1] == 'move', f"Expected 'move' but got {log[1]}"
    assert log[2] == 'combat', f"Expected 'combat' but got {log[2]}"
    assert log[3] == 'get_coins', f"Expected 'get_coins' but got {log[3]}"
    assert log[4] == 'buy_health', f"Expected 'buy_health' but got {log[4]}"
    assert log[5] == 'print_status', f"Expected 'print_status' but got {log[5]}"

# Running the tests
test_syntax_bug_fixes()
test_runtime_error_bug_fixes()

print("All tests passed successfully!")
