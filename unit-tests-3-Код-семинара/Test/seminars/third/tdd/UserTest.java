package seminars.third.tdd;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class UserTest {
    void testUserAccess() {
        User user = new User("User", "Password", false);
        assertTrue(user.authenticate("User", "Password"));
    }

    @Test
    void testUserDenied() {
        User user = new User("User1", "Password1", false);
        assertFalse(user.authenticate("User", "Password"));
    }
}