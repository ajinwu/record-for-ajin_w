import java.io.*;
import java.lang.reflect.Array;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class BinarySearch {

    public static int rank(int key,int[] a){
        int low = 0, high = a.length - 1;
        while (low <= high){
            int mid = low + (low + high) / 2;
            if(key < a[mid]){
                high = mid - 1;
            }
            if(key > a[mid]){
                low = mid + 1;
            }
            else
                return mid;
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = Files.newBufferedReader(Paths.get("/home/ajin_w/github/record-for-ajin_w/算法4/第一章基础/基础编程模型/src/1.txt"));

        String line = bf.readLine();
        String[] s = line.split(" ");
        int length = s.length - 1;
        int[] whitelist = new int[length + 1];
        for (String i:
             s) {
            whitelist[length] = Integer.parseInt(i);
            length--;
        }
        Arrays.sort(whitelist);
        System.out.println(rank(3,whitelist)+1);
    }
}
