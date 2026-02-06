import java.util.*;
import java.security.*;

interface Food {
    String getType();
}

class Pizza implements Food {
    public String getType() {
        return "Fast Food";
    }
}

class Cake implements Food {
    public String getType() {
        return "Dessert";
    }
}

class FoodFactory {
    public Food getFood(String order) {
        if (order.equalsIgnoreCase("cake")) {
            return new Cake();
        } else if (order.equalsIgnoreCase("pizza")) {
            return new Pizza();
        }
        return null;
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        FoodFactory foodFactory = new FoodFactory();

        Food food = foodFactory.getFood(sc.nextLine());

        System.out.println("The factory returned class " + food.getClass().getSimpleName());
        System.out.println("Someone ordered a " + food.getType() + "!");
    }
}