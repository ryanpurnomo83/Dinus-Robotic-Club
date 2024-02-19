import RPi.GPIO as GPIO
import time

# Tentukan pin PWM
PWM_PIN = 13

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Buat objek PWM
pwm = GPIO.PWM(PWM_PIN, 50)  # Frekuensi PWM 50 Hz

# Atur PWM ke duty cycle 0 (motor berhenti)
pwm.start(0)

# Fungsi untuk mengatur kecepatan motor
def set_speed(speed):
    # Pastikan speed berada dalam rentang 0 hingga 100
    speed = max(0, min(100, speed))
    duty_cycle = speed  # Tidak perlu mengalikan dengan 10 karena nilai sudah dalam rentang 0-100
    pwm.ChangeDutyCycle(duty_cycle)

# Main loop
try:
    while True:
        # Putar motor ke arah searah jarum jam (misalnya, kecepatan maksimum)
        set_speed(100)
        time.sleep(5)  # Tunda selama 5 detik
        
        # Putar motor ke arah berlawanan jarum jam (misalnya, kecepatan setengah)
        set_speed(50)
        time.sleep(5)  # Tunda selama 5 detik

finally:
    # Matikan PWM
    pwm.stop()

    # Bersihkan GPIO
    GPIO.cleanup()