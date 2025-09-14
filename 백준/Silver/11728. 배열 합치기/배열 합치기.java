import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        List<Integer> listA = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            listA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        List<Integer> listB = new ArrayList<>();
        for(int i = 0; i < m; i++) {
            listB.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> listC = new ArrayList<>(listA);
        listC.addAll(listB);
        Collections.sort(listC);

        StringBuilder sb = new StringBuilder();
        for (int x: listC) {
            sb.append(x).append(' ');
        }
        System.out.println(sb.toString().trim());

    }
}