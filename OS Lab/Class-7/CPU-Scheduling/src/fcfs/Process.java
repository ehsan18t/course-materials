package fcfs;

public class Process {
    int id;
    int arrivalTime;
    int duration;
    GlobalTimer globalTimer;

    public Process(int id, int arrivalTime, int duration, GlobalTimer globalTimer) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.duration = duration;
        this.globalTimer = globalTimer;
    }

    public void runProcess() {
        for (int i = 0; i < duration; i++) {
            System.out.println("My process ID: " + this.id);
            System.out.println("Global time: " + this.globalTimer.time);
            globalTimer.time++;
        }

        System.out.println("*****Process ID:" + this.id + " completed it's job.*****");
    }

    public int getId() {
        return id;
    }

    public int getArrivalTime() {
        return arrivalTime;
    }

    public int getDuration() {
        return duration;
    }

    public GlobalTimer getGlobalTimer() {
        return globalTimer;
    }
}
