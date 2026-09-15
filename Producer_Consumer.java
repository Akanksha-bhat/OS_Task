package task1;

import java.util.LinkedList;

class SharedBuffer {

    // Queue used to store the produced numbers
    private final LinkedList<Integer> queue = new LinkedList<>();

    // Maximum number of items the buffer can contain
    private final int maxSize = 4;

    // Adds a number to the buffer
    public synchronized void put(int number) throws InterruptedException {

        // Producer waits when the buffer is full
        while (queue.size() == maxSize) {
            System.out.println("Buffer full - Producer waiting");
            wait();
        }

        queue.add(number);
        System.out.println("Produced: " + number);

        // Wake up the other thread
        notifyAll();
    }

    // Removes a number from the buffer
    public synchronized int get() throws InterruptedException {

        // Consumer waits when there is nothing to consume
        while (queue.isEmpty()) {
            System.out.println("Buffer empty - Consumer waiting");
            wait();
        }

        int number = queue.removeFirst();
        System.out.println("Consumed: " + number);

        // Notify the Producer that space is available
        notifyAll();

        return number;
    }
}

class Producer implements Runnable {

    // Buffer shared with the Consumer
    private SharedBuffer buffer;

    Producer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {

        // Produce 10 numbers from 10 to 100
        for (int i = 1; i <= 10; i++) {

            try {
                buffer.put(i * 10);

                // Slow down the Producer a little
                Thread.sleep(400);

            } catch (InterruptedException e) {

                // Stop if the thread is interrupted
                Thread.currentThread().interrupt();
                return;
            }
        }
    }
}

class Consumer implements Runnable {

    // Buffer shared with the Producer
    private SharedBuffer buffer;

    Consumer(SharedBuffer buffer) {
        this.buffer = buffer;
    }

    public void run() {

        // Consume 10 numbers
        for (int i = 1; i <= 10; i++) {

            try {
                buffer.get();

                // Slow down the Consumer a little
                Thread.sleep(700);

            } catch (InterruptedException e) {

                // Stop if the thread is interrupted
                Thread.currentThread().interrupt();
                return;
            }
        }
    }
}

public class ProducerConsumer {

    public static void main(String[] args) {

        // Create one buffer shared by both threads
        SharedBuffer buffer = new SharedBuffer();

        // Create Producer and Consumer threads
        Thread p = new Thread(new Producer(buffer));
        Thread c = new Thread(new Consumer(buffer));

        // Start both threads
        p.start();
        c.start();

        try {
            // Wait for both threads to finish
            p.join();
            c.join();

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println("Execution completed.");
    }
}
