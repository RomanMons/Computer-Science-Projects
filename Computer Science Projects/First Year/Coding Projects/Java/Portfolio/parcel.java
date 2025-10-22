import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    double w, h, l, s;
    Scanner kb = new Scanner(System.in);
    System.out.print("Enter the width of the parcel: ");
    w = kb.nextDouble();
    System.out.print("Enter the height of the parcel: ");
    h = kb.nextDouble();
    System.out.print("Enter the length of the parcel: ");
    l = kb.nextDouble();
    s = w+h+l;
    if (s>90 || w>60 || h>60 || l>60) {
      System.out.print("parcel cannot be sent\n");
    }
    else {
      System.out.print("parcel can be sent\n");
    }
  }
}
