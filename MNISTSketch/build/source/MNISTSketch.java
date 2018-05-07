import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import processing.net.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class MNISTSketch extends PApplet {



int port = 10001;

Server server;
int field[] = new int[784];
public void setup() {
  noStroke();
  
  server = new Server(this, port);
  println("server address: "+server.ip()); // 192.168.1.237
  for (int i=0; i<field.length; i++) {
    field[i] = 0;
  }
}

public void draw() {
  Client client = server.available();
  if (client != null) {
    String msg = client.readString();
    if (msg != null) {
      println(msg);
    }
  }
  if (mousePressed) {
    if (0 <= mouseX && mouseX < 560 && 0 <= mouseY && mouseY < 560) {
      field[mouseY/20 * 28 + mouseX/20] = 255;
    }
  }
  for (int i=0; i<784; i++) {
    fill(field[i]);
    rect((i%28)*20, 20*(i/28), 20, 20);
  }
}
public void keyPressed() {
  switch (keyCode) {
  case 10:
    send();
    break;
  case 82:
    for (int i=0; i<784; i++) field[i]=0;
    break;
  default:
    break;
  }
}

public void send() {
  String str = "";
  for (int i=0; i<784; i++) {
    str += str(field[i])+",";
  }
  str = str.substring(0, str.length()-1);
  server.write(str);
}
  public void settings() {  size(560, 560); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "MNISTSketch" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
