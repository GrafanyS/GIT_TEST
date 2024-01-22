package seminars.fourth.hotel;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.anyInt;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

class BookingServiceTest {
    /**
     * Вам необходимо проверить правильность работы класса BookingService, который
     * использует HotelService для бронирования номера, если он доступен.
     */
    @Test
    void bookingServiceTest(){
        HotelService hotelService = mock(HotelService.class);
        BookingService bookingService = new BookingService(hotelService);
        when(hotelService.isRoomAvailable(3)).thenReturn(false);

        boolean result = bookingService.bookRoom(3);

        assertFalse(result);
    }

    @Test
    void test(){
        HotelService hotelService = mock(HotelService.class);
        BookingService bookingService = new BookingService(hotelService);
        when(hotelService.isRoomAvailable(anyInt()))
                .thenAnswer(inv->{
                    int roomNumber= inv.getArgument(0);
                    return roomNumber%2==0;
                });

        assertTrue(bookingService.bookRoom(2));
        assertFalse(bookingService.bookRoom(1));
    }

}