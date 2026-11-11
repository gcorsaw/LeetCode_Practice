import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (input.hasNextInt()) {
            int numberOfDays = input.nextInt();
            int runningGain = 0;
            int bestGain = 0;

            for (int day = 0; day < numberOfDays; day++) {
                int gain = input.nextInt();

                runningGain += gain;

                if (runningGain < 0) {
                    runningGain = 0;
                }

                if (runningGain > bestGain) {
                    bestGain = runningGain;
                }
            }

            System.out.println(bestGain);
        }

        input.close();
    }
}