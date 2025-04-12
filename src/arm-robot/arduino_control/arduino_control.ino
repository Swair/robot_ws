#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVOMIN  150 
#define SERVOMAX  600 
#define SERVO_FREQ 50 
#define SERVO_NUMS 7

ros::NodeHandle nh;

// 创建 Float32MultiArray 消息
std_msgs::Float32MultiArray joint_positions_msg;

// 回调函数，处理接收到的关节位置消息
void joint_positions_callback(const std_msgs::Float32MultiArray& msg) {
    Serial1.print("Received joint positions: ");
    for (int i = 0; i < msg.data_length; i++) {
      Serial1.print(i);
      Serial1.print(", ");
        Serial1.print(msg.data[i]);
        if (i < msg.data_length - 1) {
            Serial1.print(", "); // 添加逗号分隔
        }
    }
    Serial1.println(); // 换行
}

void servo_set(const std_msgs::Float32MultiArray& msg){
    for(int i=0;i<msg.data_length;i++){
        pwm.setPWM(i,0,msg.data[i]);
    }
}

// 创建订阅者
//ros::Subscriber<std_msgs::Float32MultiArray> sub("/joint_positions", joint_positions_callback);
ros::Subscriber<std_msgs::Float32MultiArray> sub("/joint_positions", servo_set);

void setup() {
    Serial1.begin(57600); // 初始化串口
    Serial1.println("Arduino ROS Node Started");
    pwm.begin();
    pwm.setPWMFreq(SERVO_FREQ);
    delay(10);

    nh.initNode();
    nh.subscribe(sub); // 订阅 joint_positions 话题
}

void loop() {
    nh.spinOnce(); // 处理 ROS 消息
    delay(100); // 设置一个适当的延时
}
