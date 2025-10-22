import java.util.Scanner;
public class Main {
public static void main(String[] args) {
int ca, cb, va, vb, t, tf;
Scanner kb = new Scanner(System.in);
ca = 5;
cb = 3;
va = 0;
vb = 0;
t = 4;
while ((va != t) && (va+vb != t)) {
if (va == 0) {
va = ca;
System.out.println("Fill jug A with " + va + " litres");
}
if (vb == cb) {
vb = 0;
System.out.println("Empty jug B");
}
else {
if (va < cb-vb) {
tf = va;
}
else {
tf = cb-vb;
}
va -= tf;
vb += tf;
System.out.println("Transfer " + tf + " litres from jug A to jug
B");
System.out.println("There are now " + va + " litres in jug and " + vb
+ " litres in jug B");
}
}
if (va == t) {
System.out.println("Jug A contains the desired quantity of water");
}
else {
System.out.println("Transfer " + vb + "to jug A");
va += vb;
vb = 0;
System.out.println("Jug A contains the desired quantity of water " +
va);
}
}
}
