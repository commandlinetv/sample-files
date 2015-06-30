class DoubleEquals {
    public static void main(String[] args) {
        int x = 5;
        if(x = 6) {
            System.out.println("Oops!");
        }
        boolean y = false;
        if(true = y) {
            System.out.println("Crud");
        }
    }
}
