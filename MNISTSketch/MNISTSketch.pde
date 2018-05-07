import processing.net.*;

int port = 10001;

Server server;
int field[] = new int[784];
void setup() {
  noStroke();
  size(560, 560);
  server = new Server(this, port);
  println("server address: "+server.ip()); // 192.168.1.237
  for (int i=0; i<field.length; i++) {
    field[i] = 0;
  }
}

void draw() {
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
void keyPressed() {
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

void send() {
  String str = "";
  for (int i=0; i<784; i++) {
    str += str(field[i])+",";
  }
  str = str.substring(0, str.length()-1);
  server.write(str);
}
