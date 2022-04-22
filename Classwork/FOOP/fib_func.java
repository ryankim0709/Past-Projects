package Classwork.FOOP;

public class fib_func {
    public static int x1 = 0;
    public static int x2 = 1;

    public static void main(String[] args) {
        System.out.println(nextFib());
        System.out.println(nextFib());
        System.out.println(nextFib());
        System.out.println(nextFib());
        System.out.println(nextFib());
    }

    public static int nextFib() {
        int temp = x1;
        x1 = x2;
        x2 = temp + x2;
        return x1;
    }
}
