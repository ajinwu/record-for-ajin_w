public class isPrime {
    public static void main(String[] args) {
        System.out.println(isPrime(6));
    }
    public static boolean isPrime(int N){
        if(N<2)
            return false;
        for (int i = 2; i < Math.sqrt(N); i++) {
            if(N % i == 0){
                return false;
            }
        }
        return true;
    }
}
