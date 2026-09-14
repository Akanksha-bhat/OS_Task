```java
package task1;

import java.util.LinkedList;

// Shared buffer used by both Producer and Consumer
class Buffer {

    // LinkedList stores the produced items
    private final LinkedList<Integer> items = new LinkedList<>();

    // Maximum number of items the buffer can hold
    private final int limit = 4;


    // Method used by the Producer to add an item
    // synchronized prevents Producer and Consumer from
    // accessing the buffer at the same time
    public synchronized void addItem(int value) throws InterruptedException {

        // If the buffer is full, Producer has to wait
        while (items.size() >= limit) {
            System.out.println("Buffer is full. Producer is waiting...");
            wait();
        }

        // Add the new item at the end of the list
        items.addLast(value);

        System.out.println("Produced: " + value);

        // Inform waiting threads that the buffer has changed
        notifyAll();
    }


    // Method used by the Consumer to remove an item
    public synchronized int removeItem() throws InterruptedException {

        // If there are no items, Consumer has to wait
        while (items.isEmpty()) {
            System.out.println("Buffer is empty. Consumer is waiting...");
            wait();
        }

        // Remove the first item from the buffer
        int value = items.removeFirst();

        System.out.println("Consumed: " + value);

        // Inform the waiting Producer that space is available
        notifyAll();

        // Return the consumed value
        return value;
    }
}


// Producer class
// Runnable is used to create the Producer task
class ProducerTask implements Runnable {

    // Reference to the shared buffer
    private final Buffer sharedBuffer;


    // Constructor receives the shared buffer
    ProducerTask(Buffer sharedBuffer) {
        this.sharedBuffer = sharedBuffer;
    }


    // run() contains the work performed by the Producer thread
    @Override
    public void run() {

        // Produce 10 numbers: 10, 20, 30, ..., 100
        for (int value = 10; value <= 100; value += 10) {

            try {

                // Add the value to the shared buffer
                sharedBuffer.addItem(value);

                // Pause the Producer for a short time
                Thread.sleep(400);

            } catch (InterruptedException e) {

                // Restore the interrupted status of the thread
                Thread.currentThread().interrupt();

                // Stop the Producer
                break;
            }
        }
    }
}


// Consumer class
// Runnable is used to create the Consumer task
class ConsumerTask implements Runnable {

    // Reference to the shared buffer
    private final Buffer sharedBuffer;


    // Constructor receives the shared buffer
    ConsumerTask(Buffer sharedBuffer) {
        this.sharedBuffer = sharedBuffer;
    }


    // run() contains the work performed by the Consumer thread
    @Override
    public void run() {

        // Consume 10 items
        for (int i = 0; i < 10; i++) {

            try {

                // Remove an item from the shared buffer
                sharedBuffer.removeItem();

                // Pause the Consumer for a short time
                Thread.sleep(700);

            } catch (InterruptedException e) {

                // Restore the interrupted status
                Thread.currentThread().interrupt();

                // Stop the Consumer
                break;
            }
        }
    }
}


// Main class
public class ProducerConsumer {

    public static void main(String[] args) {

        // Create one shared buffer
        // Both Producer and Consumer use this same buffer
        Buffer buffer = new Buffer();


        // Create Producer thread
        Thread producer = new Thread(new ProducerTask(buffer));


        // Create Consumer thread
        Thread consumer = new Thread(new ConsumerTask(buffer));


        // Start the Producer thread
        producer.start();


        // Start the Consumer thread
        consumer.start();


        try {

            // Wait for Producer to finish
            producer.join();

            // Wait for Consumer to finish
            consumer.join();

        } catch (InterruptedException e) {

            // Restore the interrupted status
            Thread.currentThread().interrupt();
        }


        // Display completion message
        System.out.println("Execution completed.");
    }
}
```
