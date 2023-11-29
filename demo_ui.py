# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1540, 1020)
        self.VGG19 = QtWidgets.QGroupBox(Dialog)
        self.VGG19.setGeometry(QtCore.QRect(780, 520, 741, 480))
        self.VGG19.setObjectName("VGG19")
        self.ACC_LOSS = QtWidgets.QPushButton(self.VGG19)
        self.ACC_LOSS.setGeometry(QtCore.QRect(80, 290, 200, 50))
        self.ACC_LOSS.setObjectName("ACC_LOSS")
        self.Augmented = QtWidgets.QPushButton(self.VGG19)
        self.Augmented.setGeometry(QtCore.QRect(80, 130, 200, 50))
        self.Augmented.setObjectName("Augmented")
        self.ModelStructure = QtWidgets.QPushButton(self.VGG19)
        self.ModelStructure.setGeometry(QtCore.QRect(80, 210, 200, 50))
        self.ModelStructure.setObjectName("ModelStructure")
        self.LoadImage_VGG = QtWidgets.QPushButton(self.VGG19)
        self.LoadImage_VGG.setGeometry(QtCore.QRect(80, 50, 200, 50))
        self.LoadImage_VGG.setObjectName("LoadImage_VGG")
        self.Inference = QtWidgets.QPushButton(self.VGG19)
        self.Inference.setGeometry(QtCore.QRect(80, 370, 200, 50))
        self.Inference.setObjectName("Inference")
        self.Predict = QtWidgets.QLabel(self.VGG19)
        self.Predict.setGeometry(QtCore.QRect(390, 50, 151, 16))
        self.Predict.setObjectName("Predict")
        self.INF = QtWidgets.QLabel(self.VGG19)
        self.INF.setGeometry(QtCore.QRect(390, 80, 128, 128))
        self.INF.setObjectName("INF")
        self.SIFT = QtWidgets.QGroupBox(Dialog)
        self.SIFT.setGeometry(QtCore.QRect(400, 520, 360, 480))
        self.SIFT.setObjectName("SIFT")
        self.LoadImage_1 = QtWidgets.QPushButton(self.SIFT)
        self.LoadImage_1.setGeometry(QtCore.QRect(70, 90, 200, 50))
        self.LoadImage_1.setObjectName("LoadImage_1")
        self.LoadImage_2 = QtWidgets.QPushButton(self.SIFT)
        self.LoadImage_2.setGeometry(QtCore.QRect(70, 170, 200, 50))
        self.LoadImage_2.setObjectName("LoadImage_2")
        self.Keypoints = QtWidgets.QPushButton(self.SIFT)
        self.Keypoints.setGeometry(QtCore.QRect(70, 250, 200, 50))
        self.Keypoints.setObjectName("Keypoints")
        self.MatchedKeypoints = QtWidgets.QPushButton(self.SIFT)
        self.MatchedKeypoints.setGeometry(QtCore.QRect(70, 330, 200, 50))
        self.MatchedKeypoints.setObjectName("MatchedKeypoints")
        self.LoadImage = QtWidgets.QGroupBox(Dialog)
        self.LoadImage.setGeometry(QtCore.QRect(20, 20, 360, 480))
        self.LoadImage.setObjectName("LoadImage")
        self.LoadImage_L = QtWidgets.QPushButton(self.LoadImage)
        self.LoadImage_L.setGeometry(QtCore.QRect(70, 200, 200, 50))
        self.LoadImage_L.setObjectName("LoadImage_L")
        self.LoadImage_R = QtWidgets.QPushButton(self.LoadImage)
        self.LoadImage_R.setGeometry(QtCore.QRect(70, 310, 200, 50))
        self.LoadImage_R.setObjectName("LoadImage_R")
        self.Load_folder = QtWidgets.QPushButton(self.LoadImage)
        self.Load_folder.setGeometry(QtCore.QRect(70, 90, 200, 50))
        self.Load_folder.setObjectName("Load_folder")
        self.Calibration = QtWidgets.QGroupBox(Dialog)
        self.Calibration.setGeometry(QtCore.QRect(400, 20, 360, 480))
        self.Calibration.setObjectName("Calibration")
        self.Findcorner = QtWidgets.QPushButton(self.Calibration)
        self.Findcorner.setGeometry(QtCore.QRect(70, 40, 200, 50))
        self.Findcorner.setObjectName("Findcorner")
        self.FindIntrinsic = QtWidgets.QPushButton(self.Calibration)
        self.FindIntrinsic.setGeometry(QtCore.QRect(70, 110, 200, 50))
        self.FindIntrinsic.setObjectName("FindIntrinsic")
        self.Finddistortion = QtWidgets.QPushButton(self.Calibration)
        self.Finddistortion.setGeometry(QtCore.QRect(70, 340, 200, 50))
        self.Finddistortion.setObjectName("Finddistortion")
        self.ShowResult = QtWidgets.QPushButton(self.Calibration)
        self.ShowResult.setGeometry(QtCore.QRect(70, 410, 200, 50))
        self.ShowResult.setObjectName("ShowResult")
        self.GFindextrinsic = QtWidgets.QGroupBox(self.Calibration)
        self.GFindextrinsic.setGeometry(QtCore.QRect(60, 180, 221, 141))
        self.GFindextrinsic.setObjectName("GFindextrinsic")
        self.spinBox = QtWidgets.QSpinBox(self.GFindextrinsic)
        self.spinBox.setGeometry(QtCore.QRect(90, 30, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.Findextrinsic = QtWidgets.QPushButton(self.GFindextrinsic)
        self.Findextrinsic.setGeometry(QtCore.QRect(10, 70, 200, 50))
        self.Findextrinsic.setObjectName("Findextrinsic")
        self.AugmentedReality = QtWidgets.QGroupBox(Dialog)
        self.AugmentedReality.setGeometry(QtCore.QRect(780, 20, 360, 480))
        self.AugmentedReality.setObjectName("AugmentedReality")
        self.textEdit_2 = QtWidgets.QTextEdit(self.AugmentedReality)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 70, 221, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.Showwordsonboard = QtWidgets.QPushButton(self.AugmentedReality)
        self.Showwordsonboard.setGeometry(QtCore.QRect(80, 200, 200, 50))
        self.Showwordsonboard.setObjectName("Showwordsonboard")
        self.Showwordsvertically = QtWidgets.QPushButton(self.AugmentedReality)
        self.Showwordsvertically.setGeometry(QtCore.QRect(80, 340, 200, 50))
        self.Showwordsvertically.setObjectName("Showwordsvertically")
        self.GStereoDisparityMap = QtWidgets.QGroupBox(Dialog)
        self.GStereoDisparityMap.setGeometry(QtCore.QRect(1160, 20, 360, 480))
        self.GStereoDisparityMap.setObjectName("GStereoDisparityMap")
        self.StereoDisparityMap = QtWidgets.QPushButton(self.GStereoDisparityMap)
        self.StereoDisparityMap.setGeometry(QtCore.QRect(80, 200, 200, 50))
        self.StereoDisparityMap.setObjectName("StereoDisparityMap")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.VGG19.setTitle(_translate("Dialog", "5. VGG19"))
        self.ACC_LOSS.setText(_translate("Dialog", "5.3 Show Acc and Loss"))
        self.Augmented.setText(_translate("Dialog", "5.1 Show Augmented Images"))
        self.ModelStructure.setText(_translate("Dialog", "5.2 Show Model Structure"))
        self.LoadImage_VGG.setText(_translate("Dialog", "LoadImage"))
        self.Inference.setText(_translate("Dialog", "5.4 Inference"))
        self.Predict.setText(_translate("Dialog", "Predict = "))
        self.INF.setText(_translate("Dialog", ""))
        self.SIFT.setTitle(_translate("Dialog", "4. SIFT"))
        self.LoadImage_1.setText(_translate("Dialog", "LoadImage_1"))
        self.LoadImage_2.setText(_translate("Dialog", "LoadImage_2"))
        self.Keypoints.setText(_translate("Dialog", "4.1 Keypoints"))
        self.MatchedKeypoints.setText(_translate("Dialog", "4.2 Matched Keypoints"))
        self.LoadImage.setTitle(_translate("Dialog", "Load Image"))
        self.LoadImage_L.setText(_translate("Dialog", "LoadImage_L"))
        self.LoadImage_R.setText(_translate("Dialog", "LoadImage_R"))
        self.Load_folder.setText(_translate("Dialog", "Load folder"))
        self.Calibration.setTitle(_translate("Dialog", "1. Calibration"))
        self.Findcorner.setText(_translate("Dialog", "1.1 Find Corner"))
        self.FindIntrinsic.setText(_translate("Dialog", "1.2 Find Intrinsic"))
        self.Finddistortion.setText(_translate("Dialog", "1.4 Find distortion"))
        self.ShowResult.setText(_translate("Dialog", "1.5 Show Result"))
        self.GFindextrinsic.setTitle(_translate("Dialog", "1.3 Final extrinsic"))
        self.Findextrinsic.setText(_translate("Dialog", "1.3 Find extrinsic"))
        self.AugmentedReality.setTitle(_translate("Dialog", "2. Augmented Reality"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">CAMERA</span></p></body></html>"))
        self.Showwordsonboard.setText(_translate("Dialog", "2.1 Show words on board"))
        self.Showwordsvertically.setText(_translate("Dialog", "2.2 Show words vertically"))
        self.GStereoDisparityMap.setTitle(_translate("Dialog", "3. Stereo Disparity Map"))
        self.StereoDisparityMap.setText(_translate("Dialog", "3.1 Stereo Disparity Map"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())