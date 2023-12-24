package seminars.first.Shop;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import static org.assertj.core.api.Assertions.assertThat;

public class Shop {
    private List<Product> products;

    // Геттеры, сеттеры:
    public List<Product> getProducts() {
        return products;
    }

    public void setProducts(List<Product> products) {
        this.products = products;
    }

    // Метод должен вернуть отсортированный по возрастанию по цене список продуктов
    public List<Product> sortProductsByPrice() {
        // Допишите реализацию метода самостоятельно
        if (products == null || products.size() == 0) return null;

        List<Product> sortedList = new ArrayList<>(products);
        sortedList.sort(Comparator.comparingInt(Product::getCost));
        return sortedList;
    }

    // Метод должен вернуть самый дорогой продукт
    public Product getMostExpensiveProduct() {
        // Допишите реализацию метода самостоятельно

        if (products == null || products.size() == 0) return null;

        Product mostExpensiveProduct = new Product(0, "");
        for (Product product : products) {
            if (product.getCost() > mostExpensiveProduct.getCost()) {
                mostExpensiveProduct = product;
            }

        }

        return mostExpensiveProduct;
    }
}
