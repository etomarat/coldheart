#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, time

import Adafruit_DHT

DHT_TYPE = Adafruit_DHT.DHT11
DHT_PIN  = 4

class ColdHeart():
  humidity, temp = [0, 0]
  
  while True:
    newHumidity, newTemp = readSensor()
    if temp != newTemp:
      temp = newTemp
      humidity = newHumidity
      postToSlack()
      
    time.sleep(10)
  
  def readSensor():
    return Adafruit_DHT.read(self.DHT_TYPE, self.DHT_PIN)
    
  def postToSlack():
    print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temp, humidity)
    print temp
    print humidity
  
  def __init__(self, DHT_TYPE, DHT_PIN):
    self.DHT_TYPE = DHT_TYPE
    self.DHT_PIN = DHT_PIN


if __name__ == '__main__':
  ColdHeart(DHT_TYPE, DHT_PIN)