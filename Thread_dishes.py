import threading
import queue
import time

def washer(dishes, dish_queue):
    for dish in dishes:
        print('Washing', dish)
        time.sleep(2)  # Simulate time taken to wash each dish
        dish_queue.put(dish)  # Put the washed dish in the queue


def dryer(dish_queue):
    while True:
        dish = dish_queue.get()  # Wait until there is a dish in the queue
        print('Drying', dish)
        time.sleep(4)  # Simulate time taken to dry each dish
        dish_queue.task_done()  # Indicate that the dish is done drying


# Main function to set up the threads and process the dishes
def main():
    dish_queue = queue.Queue()  # Shared queue between washer and dryer

    # Create the dryer thread
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,), daemon=True)
    dryer_thread.start()

    # List of dishes to be washed
    dishes = ['salad', 'bread', 'entree', 'dessert']

    # Start the washer process
    washer(dishes, dish_queue)

    # Wait until all dishes are processed (i.e., dried)
    dish_queue.join()

    print("All dishes are washed and dried!")


if __name__ == "__main__":
    main()