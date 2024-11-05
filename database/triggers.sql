-- Trigger: update product last_update
CREATE TRIGGER IF NOT EXISTS update_product_last_update
AFTER UPDATE ON products
BEGIN
    UPDATE products SET last_update = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- Trigger: update category last_update
CREATE TRIGGER IF NOT EXISTS update_category_last_update
AFTER UPDATE ON categories
BEGIN
    UPDATE categories SET last_update = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- Trigger: update manufacturer last_update
CREATE TRIGGER IF NOT EXISTS update_manufacturer_last_update
AFTER UPDATE ON manufacturer
BEGIN
    UPDATE manufacturer SET last_update = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- Trigger: update client last_update
CREATE TRIGGER IF NOT EXISTS update_client_last_update
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET last_update = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- Trigger: update order last_update
CREATE TRIGGER IF NOT EXISTS update_order_last_update
AFTER UPDATE ON orders
BEGIN
    UPDATE orders SET last_update = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
