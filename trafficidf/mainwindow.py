# This Python file uses the following encoding: utf-8
import sys
import cv2
import math
import numpy as np
import datetime

from PySide6.QtCore import QTimer, QSize
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

from fifo import FIFO
from fuction import Sort_points,Splitarray,Crop_image
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.fifo = FIFO(14)

        # 定义目标图像大小
        self.target_width = 400
        self.target_height = 600

        self.contourroad = np.array([[[30.,  38.]],

                        [[600.,  45.]],

                        [[600., 418.]],

                        [[ 30., 427.]]], dtype=np.float32)
        
        self.isopencam = False
        self.isfindcar = False

        self.ischeckspeed = False
        self.ischeckedspeed =False
        self.ischeckedspeedcount = 0

        self.ischeckcorretroad = False
        self.ischeckcorretroadcount = 0

        self.ischeckedlight = False
        self.ischeckedlightcount = 0

        self.ui.connectcam.clicked.connect(self.Connectcam)
        self.ui.startcheck.clicked.connect(self.Starcheck)
        self.ui.speedtest.clicked.connect(self.Checkspeedenable)

    def Connectcam(self):
        if self.isopencam ==  False:
            self.camaddress = self.ui.cam_address.text()
            self.ui.camlabel.setText('链接中......')
            QApplication.processEvents()
            self.cap = cv2.VideoCapture(self.camaddress)

            # 创建一个 QTimer 定时器用于更新图像
            self.timer = QTimer(self)
            self.timer.setInterval(70)  # 每 100 毫秒更新一次图像
            self.timer.timeout.connect(self.Updataframe)

            self.ui.cam_address.setEnabled(False)
            # 启动定时器
            self.timer.start()
        else:
            self.isopencam =True
            self.ui.camlabel.setText('链接相机')
            QApplication.processEvents()
            self.cap.release()
            # 创建一个 QTimer 定时器用于更新图像
            self.timer.stop()
            self.ui.cam_address.setEnabled(True)


    def Updataframe(self):
        # 读取图像
        ret,image = self.cap.read()
        #处理
        if self.isfindcar == True:
            roadimage = self.Idftraffic(image)
            result = cv2.cvtColor(roadimage, cv2.COLOR_BGR2RGB)
        else:
            result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 将图像转换为 QImage 格式
        qimage = QImage(result.data, result.shape[1], result.shape[0], QImage.Format_RGB888).scaled(self.ui.camlabel.size())
        # 将 QImage 显示在 QLabel 上
        self.ui.camlabel.setPixmap(QPixmap.fromImage(qimage))

    def Starcheck(self):
        if self.isfindcar == False:
            self.isfindcar = True
            self.ui.startcheck.setText('停止检测')
        else:
            self.isfindcar = False
            self.ui.startcheck.setText('开始检测')
    
    def findcar(self,image):
        # 将图像转换为 HSV 颜色空间
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定义蓝色颜色的范围
        lower_blue = np.array([100, 100, 100])
        upper_blue = np.array([120, 255, 255])

        # 创建一个掩膜来提取蓝色区域
        mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

        # 寻找蓝色区域的轮廓
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 遍历轮廓并找到最大的轮廓
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour

        # 计算蓝色区域的外接框
        x, y, w, h = cv2.boundingRect(max_contour)

        return [[x,y],[x+w,y+h]]

    def perspective_transform(self,image, src_points):
        
        # 定义目标四个角点
        dst_points = np.array([[0, 0], [self.target_width - 1, 0], [self.target_width - 1, self.target_height - 1], [0, self.target_height - 1]], dtype=np.float32)

        # 计算透视变换矩阵
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # 应用透视变换
        warped_image = cv2.warpPerspective(image, matrix, (self.target_width, self.target_height))

        return warped_image
    
    def Checklight(self,image,st_car,end_car):
        if self.ischeckedlight == True:
            self.ischeckedlightcount += 1
            if self.ischeckedlightcount == 30:
                self.ischeckedlight = False
                self.ischeckedlightcount = 0
        else:
            light = self.ui.lighlimit.currentIndex()
            if light == 0:
                pass
            elif light == 1:
                if end_car[0]>self.roadline4[0] or st_car[0]>self.roadline4[0]:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    self.ui.warmingtext.append(f'闯红灯！时间{timestamp}')
                    cv2.imwrite(f'./image/redlight{timestamp}.png', image)
                    self.ischeckedlight = True
                else:
                    pass
            elif light ==2:
                if end_car[0]>self.roadline4[1] or st_car[0]>self.roadline4[1]:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    self.ui.warmingtext.append(f'闯黄灯！时间{timestamp}')
                    cv2.imwrite(f'./image/yellight{timestamp}.png', image)
                    self.ischeckedlight = True
            else:
                pass

    def Checkroad(self,image,st_car,end_car):
        if self.ischeckcorretroad == True:
            self.ischeckcorretroadcount += 1
            if self.ischeckcorretroadcount == 30:
                self.ischeckcorretroad = False
                self.ischeckcorretroadcount = 0
        else:
            roadcheck = self.ui.roadlimit.currentIndex()
            if roadcheck == 0:
                pass
            elif roadcheck == 1:
                if self.roadline0[1]<st_car[1] and self.roadline1[0]>end_car[1]:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
                    self.ui.warmingtext.append(f'上侧车道限制行驶！时间{timestamp}')
                    cv2.imwrite(f'./image/upperroad{timestamp}.png', image)
                    self.ischeckcorretroad = True
                else:
                    pass
            elif roadcheck ==2:
                if self.roadline1[1]<st_car[1] and self.roadline2[0]>end_car[1]:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    self.ui.warmingtext.append(f'下侧车道限制行驶！时间{timestamp}')
                    cv2.imwrite(f'./image/lowerroad{timestamp}.png', image)
                    self.ischeckcorretroad = True
            elif roadcheck ==3:
                if ((self.roadline0[1] > st_car[1]) or (self.roadline2[0] <end_car[1]) or 
                        (end_car[1]>self.roadline1[0] and st_car[1]<self.roadline1[0]) or
                        (end_car[1]>self.roadline1[1] and st_car[1]<self.roadline1[1])):
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    self.ui.warmingtext.append(f'实线禁止变道！时间{timestamp}')
                    cv2.imwrite(f'./image/changeroad{timestamp}.png', image)
                    self.ischeckcorretroad = True
            else:
                pass

    
    def Checkspeedenable(self):
        if self.ischeckspeed == False:
            self.ischeckspeed = True
            self.ui.speedtest.setText('停止检测')
        else:
            self.ischeckspeed = False
            self.ui.speedtest.setText('超速检测')


    def Checkspeed(self,image,speed_car):
        if self.ischeckspeed:
            if self.ischeckedspeed == True:
                self.ischeckedspeedcount += 1
                if self.ischeckedspeedcount == 15:
                    self.ischeckedspeed = False
                    self.ischeckedspeedcount = 0
            else:
                speedlimit = int(self.ui.speedtop.text())
                print(speedlimit)
                print(speed_car)
                if speed_car >speedlimit:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    self.ui.warmingtext.append(f'超速行驶！时间{timestamp}')
                    cv2.imwrite(f'./image/overspeed{timestamp}.png', image)
                    self.ischeckedspeed = True
                else:
                    pass
        else:
            pass

    def Idftraffic(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 高斯模糊
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Canny边缘检测
        edges = cv2.Canny(blurred, 50, 150)

        # 寻找轮廓
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # 计算轮廓的面积
            area = cv2.contourArea(contour)

            # 过滤掉面积小的轮廓
            if area < 10000:
                continue

            # 拟合四边形
            approx = cv2.approxPolyDP(contour, cv2.arcLength(contour, True) * 0.02, True)

            if len(approx) == 4:
            # 返回试卷的四个角的位置
                # 绘制拟合后的四边形
                # cv2.drawContours(frame, [approx], -1, (0, 255, 0),3)
                self.contourroad = approx

        sortpoints = Sort_points(self.contourroad)
        # print(sortpoints)
        roadimage = self.perspective_transform(frame,sortpoints)

        roadimage = Crop_image(roadimage,3)

        gray_roadimage = cv2.cvtColor(roadimage, cv2.COLOR_BGR2GRAY)

        car_st,car_end = self.findcar(roadimage)
        car_center = np.add(car_st,car_end)/2
        self.fifo.add(car_center)

        if self.fifo.is_full:
            car_move = car_center - self.fifo.get()
            speed_car = math.sqrt(car_move[0]**2 +car_move[1]**2)

            cv2.putText(roadimage,f'speed:{speed_car}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

        cv2.rectangle(roadimage, car_st, car_end, (0, 255, 0), 2)

        horizon_sum = np.sum(gray_roadimage, axis=1)
        # 计算竖向求和结果的中位数
        median_value_h = np.median(horizon_sum)-40000
        # 找到数值大于等于中位数的列的索引
        valid_indices_h = np.where(horizon_sum <= median_value_h)[0]

        if valid_indices_h is not None:
            split_array = Splitarray(valid_indices_h)
        if len(split_array) == 3:
            self.roadline0 = [split_array[0][0]+5,split_array[0][-1]-5]
            self.roadline1 = [split_array[1][0]+5,split_array[1][-1]-5]
            self.roadline2 = [split_array[2][0]+5,split_array[2][-1]-5]

            for line in [self.roadline0,self.roadline1,self.roadline2]:
                cv2.line(roadimage, (0, line[0]), (roadimage.shape[1], line[0]), (0,0,255), thickness=2)
                cv2.line(roadimage, (0, line[1]), (roadimage.shape[1], line[1]), (0,0,255), thickness=2)

        vertical_sum = np.sum(gray_roadimage, axis=0)
        # 计算竖向求和结果的中位数
        median_value_v = np.median(vertical_sum)-40000

        # 找到数值大于等于中位数的列的索引
        valid_indices_v = np.where(vertical_sum <= median_value_v)[0]
        if valid_indices_v is not None:
            self.roadline4 = [valid_indices_v[0],valid_indices_v[-1]]
            cv2.line(roadimage, (self.roadline4[0], 0), (self.roadline4[0], roadimage.shape[0]), (0,0,255), thickness=2)
            cv2.line(roadimage, (self.roadline4[1], 0), (self.roadline4[1], roadimage.shape[0]), (0,0,255), thickness=2)

        self.Checklight(roadimage,car_st,car_end)
        self.Checkroad(roadimage,car_st,car_end)
        self.Checkspeed(roadimage,speed_car)

        return roadimage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
