package seminars.first.Shop;

import java.util.Arrays;

import static org.assertj.core.api.Assertions.assertThat;

public class ShopTest {

    /*
   1. Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов (правильное количество продуктов, верное содержимое корзины).
   2. Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
   3. Напишите тесты для проверки корректности работы метода sortProductsByPrice (проверьте правильность сортировки).
   */

    public static void main(String[] args) {
        // валидный экземпляр Магазина для проверки всех тестов
        Shop validShop = new Shop();
        validShop.setProducts(Arrays.asList(
                new Product(10, "Milk"),
                new Product(1, "matches"),
                new Product(20, "chicken")
        ));

        // Невалидный магазин с пустым списком продуктов (size = 0)
        Shop notValidShopProductsEmpty = new Shop();
        notValidShopProductsEmpty.setProducts(Arrays.asList());
        // Невалидный магазин с отсутствующим списком продуктов (null)
        Shop notValidShopProductsNull = new Shop();

        // Не знаю правильно ли я понял про тест на проверку верного списка продуктов
        // но других идей у меня нет
        assertThat(validShop.getProducts()).contains(
                new Product(1, "matches"),
                new Product(10, "Milk"),
                new Product(20, "chicken")
        );
        assertThat(notValidShopProductsEmpty.getProducts()).isEmpty();
        assertThat(notValidShopProductsNull.getProducts()).isNull();

        // тесты на проверку самого дорогого товара
        assertThat(validShop.getMostExpensiveProduct().getCost()).isEqualTo(20);
        assertThat(notValidShopProductsEmpty.getMostExpensiveProduct()).isNull();
        assertThat(notValidShopProductsNull.getMostExpensiveProduct()).isNull();

        // тесты на проверку сортировки продуктов
        assertThat(validShop.sortProductsByPrice()).isEqualTo(Arrays.asList(
                new Product(1, "matches"),
                new Product(10, "Milk"),
                new Product(20, "chicken")
        ));
        assertThat(notValidShopProductsEmpty.sortProductsByPrice()).isNull();
        assertThat(notValidShopProductsNull.sortProductsByPrice()).isNull();
    }
}

