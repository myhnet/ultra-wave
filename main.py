function 显示条件 (左数: number, 中数: number, 右数: number) {
    I2C_LCD1602.ShowNumber(中数, 0, 0)
    I2C_LCD1602.ShowNumber(左数, 0, 1)
    I2C_LCD1602.ShowNumber(右数, 11, 1)
}
function 取距离 (数字: number) {
    cbit_小车类.Servo_Car(cbit_小车类.enServo.S1, 数字)
    basic.pause(500)
    距离 = Math.floor(cbit_小车类.Ultrasonic_Car())
    while (距离 == 0) {
        距离 = Math.floor(cbit_小车类.Ultrasonic_Car())
    }
    return 距离
}
let 中 = 0
let 右 = 0
let 左 = 0
let 距离 = 0
cbit_小车类.Servo_Car(cbit_小车类.enServo.S1, 90)
cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Stop, 0)
I2C_LCD1602.LcdInit(39)
basic.pause(500)
basic.forever(function () {
    cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Stop, 0)
    basic.pause(500)
    cbit_小车类.Servo_Car(cbit_小车类.enServo.S1, 150)
    basic.pause(500)
    左 = 取距离(150)
    右 = 取距离(30)
    中 = 取距离(90)
    显示条件(左, 中, 右)
    if (中 <= 40) {
        cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Back, 200)
        I2C_LCD1602.ShowString("H1", 0, 0)
    } else if (中 > 100) {
        cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Run, 200)
    } else {
        if (左 < 100 && 右 < 100) {
            cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Back, 200)
            I2C_LCD1602.ShowString("H2", 0, 0)
        } else if (右 <= 左) {
            cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Left, 200)
        } else {
            cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Right, 200)
        }
    }
    basic.pause(1000)
})
