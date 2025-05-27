// input 1 -> payload 1 
// input 2 -> payload 2 
// input 3 -> payload 3 
// input 4 -> payload 4 
// input 7 -> all close 
// input 8 -> all half open 
// input 9 -> all opem

#include <Servo.h>
#include <Arduino_FreeRTOS.h>
#include <queue.h>

Servo servos[4];
int servoPins[4] = {4,5, 6, 7};

QueueHandle_t inputQueue;

//
void moveServo(int index, int angle) {
  if (index >= 0 && index < 4) {
    servos[index].write(angle);
    vTaskDelay(pdMS_TO_TICKS(500));
  }
}

void InputTask(void *pvParameters) {
  while (1) {
    if (Serial.available()) {
      char cmd = Serial.read();

      if ((cmd >= '1' && cmd <= '4') || cmd == '7' || cmd == '8' || cmd == '9') {
        xQueueSend(inputQueue, &cmd, portMAX_DELAY);
      }

      if (cmd == '\n') {
        while (Serial.available()) Serial.read();
      }
    }
    vTaskDelay(pdMS_TO_TICKS(50));
  }
}

void CommandTask(void *pvParameters) {
  char cmd;
  while (1) {
    if (xQueueReceive(inputQueue, &cmd, portMAX_DELAY) == pdPASS) {
      switch (cmd) {
        case '1': case '2': case '3': case '4': {
          int index = cmd - '1';
          moveServo(index, 90);
          vTaskDelay(pdMS_TO_TICKS(2000));
          moveServo(index, 135);
          break;
        }

        case '7':
          for (int i = 0; i < 4; i++) {
            moveServo(i, 45);
            vTaskDelay(pdMS_TO_TICKS(500));
          }
          break;

        case '8':
          for (int i = 0; i < 4; i++) {
            moveServo(i, 90);
            vTaskDelay(pdMS_TO_TICKS(500));
          }
          break;

        case '9':
          for (int i = 0; i < 4; i++) {
            moveServo(i, 135);
            vTaskDelay(pdMS_TO_TICKS(500));
          }
          break;
      }
    }
  }
}

void setup() {
  Serial.begin(9600);
  
  for (int i = 0; i < 4; i++) {
    servos[i].attach(servoPins[i]);
    servos[i].write(45);
  }

  inputQueue = xQueueCreate(10, sizeof(char));
  
  xTaskCreate(InputTask, "InputTask", 128, NULL, 1, NULL);
  xTaskCreate(CommandTask, "CommandTask", 256, NULL, 1, NULL);
}
void loop() {
}
