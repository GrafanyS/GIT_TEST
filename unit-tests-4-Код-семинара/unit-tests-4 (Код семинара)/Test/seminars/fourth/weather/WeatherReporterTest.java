package seminars.fourth.weather;


import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

/**
 * 4.3 Предположим, у вас есть класс WeatherService, который имеет метод getCurrentTemperature(),
 * обращающийся к внешнему API для получения информации о текущей температуре.
 * Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService.
 * Создайте мок-объект для WeatherService с использованием Mockito.
 */
class WeatherReporterTest {

    @Test
    void generateReportTest(){
        WeatherService mockWeatherService = mock(WeatherService.class);
        //WeatherService mockWeatherService = new WeatherService();
        when(mockWeatherService.getCurrentTemperature()).thenReturn(25);
        WeatherReporter weatherReporter = new WeatherReporter(mockWeatherService);

        String reply = weatherReporter.generateReport();

        assertThat(reply).isEqualTo("Текущая температура: " + 25 + " градусов.");
    }


}