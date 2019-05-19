interface Eatable{
    void taste();
}
interface Flyable{
    void fly(String weather);
}
interface Addable{
    int add(int a, int b);
}
public class Lambda {
    public void eat (Eatable e){
        System.out.println(e);
        e.taste();
    }
    public void drive(Flyable f){
        System.out.println(f);
        f.fly("【碧空如洗的晴日】");
    }
    public void test(Addable add){
        System.out.println(add.add(5, 3));
    }
    public static void main(String[] args){
        Lambda l = new Lambda();
        l.eat(()->System.out.println("苹果味道不错"));
        l.drive(weather -> {
            System.out.println("今天天气是："+weather);
            System.out.println("直升机飞行平稳");
        });
        l.test(((a, b) -> a+b));
    }
}
