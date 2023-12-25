package seminars.second.simple_shopping_cart;

import java.util.List;

/**
 * @param productsShop Список продуктов в магазине
 */
public record Shop(List<Product> productsShop) {
    // При создании магазина нужно передать ему список продуктов
}