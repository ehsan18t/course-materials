package fcfs;

import java.util.PriorityQueue;

public class FCFS {
    static PriorityQueue<Process> processQueue = new PriorityQueue<>(10, (o1, o2) -> {
        // Always based on arrival time
        return (int) (o1.getArrivalTime() - o2.getArrivalTime());
    });
    static PriorityQueue<Process> readyQueue = new PriorityQueue<>(10, (o1, o2) -> {
        // depends on scheduling algorithm
        return (int) (o1.getArrivalTime() - o2.getArrivalTime());
    });

    static GlobalTimer globalTimer = new GlobalTimer(0);

    public static void main(String[] args) {
        processQueue.add(new Process(1, 3, 2, globalTimer));
        processQueue.add(new Process(2, 6, 2, globalTimer));
        processQueue.add(new Process(3, 1, 2, globalTimer));
        processQueue.add(new Process(4, 3, 5, globalTimer));

        while (true) {
            while (!processQueue.isEmpty() && !readyQueue.isEmpty()) {
                readyQueue.add(processQueue.poll());
            }

            if (!readyQueue.isEmpty())
                runProcessInCPU();
            else {
                System.out.println("No process in Ready Queue");
                System.out.println("Global Time: " + globalTimer.time);
                globalTimer.time++;
            }
        }
    }

    public static boolean checkIfNewProcessArrived() {
        if (!processQueue.isEmpty()) {
            if (processQueue.element().getArrivalTime() < globalTimer.time)
                return true;
        }
        return false;
    }

    public static void runProcessInCPU() {
        Process process = readyQueue.poll();
        process.runProcess();
    }
}
