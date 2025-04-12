package PRACTICA1.INTRODUCCIONPOO.EJERCICIO3;

public class Ejercicio3 {
    public static class Coche {
        private String marca;
        private String modelo;
        private int velocidad;
    
        public Coche(String marca, String modelo, int velocidad) {
            this.marca = marca;
            this.modelo = modelo;
            this.velocidad = velocidad;
        }
    
        public void acelerar() {
            velocidad += 10;
            System.out.println(marca + " " + modelo + " acelera. Nueva velocidad: " + velocidad + " km/h");
        }
    
        public void frenar() {
            velocidad -= 5;
            if (velocidad < 0) {
                velocidad = 0;
            }
            System.out.println(marca + " " + modelo + " frena. Nueva velocidad: " + velocidad + " km/h");
        }
    
        public void mostrarVelocidad() {
            System.out.println("El coche " + marca + " " + modelo + " va a " + velocidad + " km/h");
        }
    
        public static void main(String[] args) {
            Coche coche1 = new Coche("Toyota", "Corolla", 50);
            Coche coche2 = new Coche("Ford", "Focus", 30);
    
            coche1.acelerar();
            coche1.frenar();
            coche1.mostrarVelocidad();
    
            coche2.acelerar();
            coche2.frenar();
            coche2.mostrarVelocidad();
        }
    }    
}
