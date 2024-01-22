package seminars.fourth.message;


import org.junit.jupiter.api.Test;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;

class NotificationServiceTest {

    @Test
    void test() {

        MessageService messageServiceMock = mock(MessageService.class);

        NotificationService notificationService = new NotificationService(messageServiceMock);

        notificationService.sendNotification("message", "recipient");
        verify(messageServiceMock).sendMessage("message", "recipient");
    }

}