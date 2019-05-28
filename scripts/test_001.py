import os

import allure
import pytest
import yaml


class Test_01:
    @allure.step("这是测试步骤01")
    def test_001(self):
        with open(os.getcwd()+os.sep+"image"+os.sep+"abc.png","rb") as f:

            allure.attach("截图",f.read(),allure.attach_type.PNG)