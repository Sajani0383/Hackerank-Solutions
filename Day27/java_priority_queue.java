import java.util.*;

class Student {
    int id;
    String name;
    double cgpa;

    Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.cgpa = cgpa;
    }
}

class Priorities {
    PriorityQueue<Student> pq = new PriorityQueue<Student>(
        new Comparator<Student>() {
            public int compare(Student a, Student b) {
                if (a.cgpa != b.cgpa)
                    return Double.compare(b.cgpa, a.cgpa);
                if (!a.name.equals(b.name))
                    return a.name.compareTo(b.name);
                return a.id - b.id;
            }
        }
    );

    List<Student> getStudents(List<String> events) {
        for (String e : events) {
            String[] s = e.split(" ");
            if (s[0].equals("ENTER")) {
                pq.add(new Student(
                    Integer.parseInt(s[3]),
                    s[1],
                    Double.parseDouble(s[2])
                ));
            } else {
                pq.poll();
            }
        }

        List<Student> result = new ArrayList<Student>();
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }
        return result;
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        List<String> events = new ArrayList<String>();

        for (int i = 0; i < n; i++) {
            events.add(sc.nextLine());
        }

        Priorities p = new Priorities();
        List<Student> students = p.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student s : students) {
                System.out.println(s.name);
            }
        }
    }
}