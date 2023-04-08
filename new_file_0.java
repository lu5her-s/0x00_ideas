import java.util.*;
import java.text.*;

public class DigitalClock {
    public static void main(String[] args) {
        while (true) {
            DateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
            Date date = new Date();
            System.out.println(dateFormat.format(date));
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
