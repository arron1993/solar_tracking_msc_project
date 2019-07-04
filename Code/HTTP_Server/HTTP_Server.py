import socket
import sys
import time
import os
class HTTP_Server:
    def __init__(self):
        print("HTTP Server Created")
        
    def encodeData(self,data):
        data = str(data)
        return data.encode("utf-8")

    def decodeResponse(self,response):
        return response.decode("utf-8")
    
    def socket_init(self):
        host = ''
        size = 1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s

    def Generate_Response_Code(self, code):
        # determine response code
        response = ''
        if(code == 404):
            response = 'HTTP/1.1 404 Not Found \n'
        elif (code == 200):
            response = 'HTTP/1.1 200 Status OK \n'


        # write further headers
        current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) 
        response += 'Date: ' + current_date +'\n'
        response += 'Server: Arrons HTTP Server\n'
        response += 'Connection: close\n\n'     
        return response

    def index_html(self):
        html = '<html>'
        html += '<head>'
        html += '<!--jquerystuff-->'
        html += '<style>'
        html += 'td th {width:15%;text-align:center;}'
        html += '.title_button_bar_button'
        html += '{float:left;height:100%;width:25%;display:block;text-align:center;}'
        html += '.title_button_bar_button:hover'
        html += '{'
        html += '-webkit-box-shadow:0px0px10px0pxrgba(0,0,0,0.50);'
        html += '-moz-box-shadow:0px0px10px0pxrgba(0,0,0,0.50);'
        html += 'box-shadow:0px0px10px0pxrgba(0,0,0,0.50);'
        html += '}'
        html += 'h3 {padding:0;margin:0;}'
        html += '</style>'
        html += '</head>'
        html += '<body style="margin:0;padding:0">'
        html += '<div id="title_bar"style="width:100%;height:10%;text-align:center">'
        html += '<h1 style="margin:0;padding:0">Data</h1>'
        html += '</div>'
        html += '<div id="title_button_bar"style="float:left;height:5%;width:100%;">'
        html += '<div id="button_1"class="title_button_bar_button"style="">'
        html+= '<button onclick="get_live()"> Refresh </button>'
        html += '</div><!--button_1-->'
        html += '<div id="button_2"class="title_button_bar_button"style="b">'
        html+= '<button onclick="start_live_feed()"> Start Live Feed </button>'
        html += '<button onclick="stop_live_feed();">Stop Live Feed</button>'
        html += '</div><!--button_2-->'
        html += '<div id="button_3"class="title_button_bar_button"style="">'
        html += 'Button3'
        html += '</div><!--button_3-->'
        html += '<div id="button_4"class="title_button_bar_button"style="">'
        html += 'Button4'
        html += '</div><!--button_4-->'

        html += '</div>'
        
        html += '<div id="main_content"style="float:left;width:100%;height:75%;">'
        

        
        html += '<div id = "main_content_all_live" style="width:100%;float:left">'
        html +='<table id = "all_data" style="text-align:center;table-layout:fixed;margin-left:auto;margin-right:auto;width:75%"> <tr> <th>Time</th> <th> Channel </th> <th> GPIO Pin </th> <th> Angle Mode </th> <th>Angle  </th> <th> Voltage </th> </tr>'
        
        data = self.get_all_data(10)
        #print("\n\n",data_array,"\n\n")
       
        
        per_channel_reading = data.split("/")


        for channel in per_channel_reading:
            values = channel.split(",")
            if(len(values) >= 6):
                time = values[0]
                read_channel = values[1]
                gpio_pin = values[2]
                angle_mode = values[3]
                angle = values[4]
                voltage = values[5]

                html += "<tr> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> <td> {} </td> </tr>".format(time,read_channel,gpio_pin,angle_mode,angle,voltage)

                
        html +='</table>'
        
        html += '<script>'
        html += 'function get_live()'
        html += '{'
        html += '    var xhr = new XMLHttpRequest();'
        html += '    xhr.open("GET", "/data", true);'
        html += '    xhr.onload = function (e) {'
        html += '      if (xhr.readyState === 4) {'
        html += '        if (xhr.status === 200) {'
        html += 'response = xhr.responseText;'
        html += 'channel_values = response.split("/");'
        html+='for(var x = 0; x < channel_values.length; ++x) {'
        html += 'readings = channel_values[x].split(",");'
        html += 'if(readings.length >= 6){'
        html += 'var table = document.getElementById("all_data");'
        html += 'var row = table.insertRow(1);'
        html += 'var time = row.insertCell(0);'
        html += 'var channel = row.insertCell(1);'
        html += 'var gpio_pin = row.insertCell(2);'
        html += 'var angle_mode = row.insertCell(3);'
        html += 'var angle = row.insertCell(4);'
        html += 'var voltage = row.insertCell(5);'
        html += 'time.innerHTML = new Date(parseInt(readings[0]));'
        html += 'channel.innerHTML = readings[1];'
        html += 'gpio_pin.innerHTML = readings[2];'
        html +=  'angle_mode.innerHTML = readings[3];'
        html +=  'angle.innerHTML = readings[4];'
        html +=  'voltage.innerHTML = readings[5];'
        html +=  '}}'
        html += '          console.log(xhr.responseText);'
        html += '        } else {'
        html += '          console.error(xhr.statusText);'
        html += '        }'
        html += '      }'
        html += '    };'
        html += '    xhr.onerror = function (e) {'
        html += '      console.error(xhr.statusText);'
        html += '    };'
        html += '    xhr.send(null);'
        html += '}'
        html += 'function start_live_feed() '
        html += '{'
        html += '      live_feed_interval = setInterval(get_live, 1000);'
        html += '}'
        html+= 'function stop_live_feed() { clearInterval(live_feed_interval); }'
        html += '</script>'

        html += '</div> <!--main_content_all_live-->'
        html += '</div> <!--main_content-->'
        html += '<div id="main_footer"style="float:left;width:100%;height:10%;">'


        html += '</div> <!--main_footer-->'
        html += '</body>'
        html += '</html>'
        return html
        
    def get_all_data(self, quantity):
        response = "ERROR: Response Not Defined"
        try:
            host = "192.168.0.10" #location of data server
            port = 15000 # data server port
            request = "GET_DATA A " + str(quantity)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host,port))
            sock.send(self.encodeData(request))  
            response = sock.recv(1024)
            response = self.decodeResponse(response)
            sock.close()
        except OSError as os_error:
            print(os_error)
            response = "ERROR: Could Not Connect to Data Server at {}:{}".format(host,port)
        return response
        
    def data_html(self):  
        html_str = ""
        html_array = self.get_all_data(1)
        for data in html_array:
            html_str += data

        return html_str


    
    def start(self):
        if(len(sys.argv) > 1):
            port = sys.argv[1]
        else:
            port = 9000
            
        s = self.socket_init()
        s.bind(('0.0.0.0',int(port)))
        s.listen(5)
        print("HTTP Server Started on Port",port)
        while 1:
            HTTP_Response = self.Generate_Response_Code(404)
            conn, addr = s.accept()

            print("Got connection from:", addr)

            data = conn.recv(1024) 

            HTTP_Request = bytes.decode(data) 

            print(HTTP_Request)

            HTTP_line = HTTP_Request.split('\n')
            
            HTTP_Method = HTTP_line[0].split(' ')[0]

            print("Method =",HTTP_Method)

            if(HTTP_Method == "GET"):
                Content_Found = False
             
                HTTP_Method_GET_What = HTTP_line[0].split(' ')[1]
                print("GETTING: ", HTTP_Method_GET_What)
                if(HTTP_Method_GET_What == "/index.html" or HTTP_Method_GET_What == "/"):
                    html = self.index_html()
                    HTTP_Response = self.Generate_Response_Code(200) + html
                elif(HTTP_Method_GET_What == "/data"):
                    html = self.data_html()
                    HTTP_Response = self.Generate_Response_Code(200) + html
                #elif(HTTP_Method_GET_What == "/jquery-test"):
                    #file jq_test = open(
            elif(HTTP_Method == "HEAD"):
                print("HEAD")

                HTTP_Response = self.Generate_Response(200)

            print(HTTP_Response)
            conn.send(HTTP_Response.encode("utf-8"))

            conn.close()



    





