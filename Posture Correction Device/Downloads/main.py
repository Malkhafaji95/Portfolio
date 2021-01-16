import socket
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy_garden.graph import MeshLinePlot
from kivy.clock import Clock



# absulote pathing
postxt = os.path.dirname(os.path.abspath(__file__))

#network connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((('***.***.*.***'), (1239))) #phone
s.bind((('***.***.*.**'), (1239))) #pc
s.listen(5)

#link to kv file
Builder.load_file('design.kv') # loads the design.kv file

class MainPage(Screen):
    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_screen"

    def start10(self):
        self.manager.current = "scanning_page10"

    def start15(self):
        self.manager.current = "scanning_page15"

    def start20(self):
        self.manager.current = "scanning_page20"


class PostSeshPage10(Screen):
    def exit(self):
        self.manager.current = "main_page"
        Clock.unschedule(self.plot_value)

    def __init__(self,**kwargs):
        super(PostSeshPage10, self).__init__()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        global post_sesh_timer10
        post_sesh_timer10=Clock.create_trigger(self.post_graphh)
        

    def post_graphh(self,dt):
        self.ids.post_obs_text10.text = "Session results"
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.post_graph10.add_plot(self.plot)
        Clock.schedule_interval(self.plot_value, 0.1)
        Clock.schedule_once(self.get_average, 3)
        Clock.schedule_once(self.get_lowest_value, 5)

        global file_counter
        file_counter = 1
        while True:
            if os.path.isfile(os.path.join(postxt, 'data/datafile{0}.txt'.format(file_counter))):
                file_counter += 1
            else:
                file_counter -= 1
                open(os.path.join(postxt,('data/datafile{0}.txt'.format(file_counter))),"r")
                break

    def plot_value(self, dt):
        print(3)
        print("before plot")
        self.plot.points = [(x, float(y)) for x, y in enumerate(open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))).readlines(4000))]
        print("after plot")

    def get_average(self, dt):
        with open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))) as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter
            for line in fh:
                count += 1 # increment the counter
                sum += float(line.split()[0]) # add here, not in a nested loop
            average = round((sum / count),2)
            print("before average")
            self.ids.post_ave_text10.text = ('Average: {0}'.format(average))
            print("after average")
    
    def get_lowest_value(self, dt):
        postureData = open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter)), "r")
        smallest_value = 90

        for numbers in postureData:
            numbers = float(numbers.rstrip())
            # ... your other logic
            if smallest_value > numbers:
                smallest_value = numbers

        # for value in postureData:
        #     if smallest_value >= float(value.strip()):
        #       smallest_value = float(value.strip())
        
        self.ids.post_lowest_value_text10.text = ('Lowest Posture Angle : {0}'.format(smallest_value))

class PostSeshPage15(Screen):
    def exit(self):
        self.manager.current = "main_page"
        Clock.unschedule(self.plot_value)

    def __init__(self,**kwargs):
        super(PostSeshPage15, self).__init__()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        global post_sesh_timer15
        post_sesh_timer15=Clock.create_trigger(self.post_graphh)
        

    def post_graphh(self,dt):
        self.ids.post_obs_text15.text = "Session results"
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.post_graph15.add_plot(self.plot)
        Clock.schedule_interval(self.plot_value, 0.1)
        Clock.schedule_once(self.get_average, 3)
        Clock.schedule_once(self.get_lowest_value, 5)

        global file_counter
        file_counter = 1
        while True:
            if os.path.isfile(os.path.join(postxt, 'data/datafile{0}.txt'.format(file_counter))):
                file_counter += 1
            else:
                file_counter -= 1
                open(os.path.join(postxt,('data/datafile{0}.txt'.format(file_counter))),"r")
                break

    def plot_value(self, dt):
        print(3)
        print("before plot")
        self.plot.points = [(x, float(y)) for x, y in enumerate(open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))).readlines(6000))]
        print("after plot")

    def get_average(self, dt):
        with open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))) as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter
            for line in fh:
                count += 1 # increment the counter
                sum += float(line.split()[0]) # add here, not in a nested loop
            average = round((sum / count),2)
            print("before average")
            self.ids.post_ave_text15.text = ('Average: {0}'.format(average))
            print("after average")
    
    def get_lowest_value(self, dt):
        postureData = open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter)), "r")
        smallest_value = 90

        for numbers in postureData:
            numbers = float(numbers.rstrip())
            # ... your other logic
            if smallest_value > numbers:
                smallest_value = numbers

        # for value in postureData:
        #     if smallest_value >= float(value.strip()):
        #       smallest_value = float(value.strip())
        
        self.ids.post_lowest_value_text15.text = ('Lowest Posture Angle : {0}'.format(smallest_value))

class PostSeshPage20(Screen):
    def exit(self):
        self.manager.current = "main_page"
        Clock.unschedule(self.plot_value)

    def __init__(self,**kwargs):
        super(PostSeshPage20, self).__init__()
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        global post_sesh_timer20
        post_sesh_timer20=Clock.create_trigger(self.post_graphh)
        

    def post_graphh(self,dt):
        self.ids.post_obs_text20.text = "Session results"
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.post_graph20.add_plot(self.plot)
        Clock.schedule_interval(self.plot_value, 0.1)
        Clock.schedule_once(self.get_average, 3)
        Clock.schedule_once(self.get_lowest_value, 5)

        global file_counter
        file_counter = 1
        while True:
            if os.path.isfile(os.path.join(postxt, 'data/datafile{0}.txt'.format(file_counter))):
                file_counter += 1
            else:
                file_counter -= 1
                open(os.path.join(postxt,('data/datafile{0}.txt'.format(file_counter))),"r")
                break

    def plot_value(self, dt):
        print(3)
        print("before plot")
        self.plot.points = [(x, float(y)) for x, y in enumerate(open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))).readlines(8000))]
        print("after plot")

    def get_average(self, dt):
        with open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))) as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter
            for line in fh:
                count += 1 # increment the counter
                sum += float(line.split()[0]) # add here, not in a nested loop
            average = round((sum / count),2)
            print("before average")
            self.ids.post_ave_text20.text = ('Average: {0}'.format(average))
            print("after average")
    
    def get_lowest_value(self, dt):
        postureData = open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter)), "r")
        smallest_value = 90

        for numbers in postureData:
            numbers = float(numbers.rstrip())
            # ... your other logic
            if smallest_value > numbers:
                smallest_value = numbers

        # for value in postureData:
        #     if smallest_value >= float(value.strip()):
        #       smallest_value = float(value.strip())
        
        self.ids.post_lowest_value_text20.text = ('Lowest Posture Angle : {0}'.format(smallest_value))


class ScanningPage10(Screen):
    
    a= PostSeshPage10()
    call_pp10 = a.post_graphh

    def exit(self):
        # self.manager.transition.direction= 'right'
        self.manager.current = "main_page"
        Clock.unschedule(self.plot_value)
        Clock.unschedule(self.get_value)
        Clock.unschedule(self.get_average)

    def __init__(self, **kwargs):
        super(ScanningPage10, self).__init__(**kwargs)
        # self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def graphh(self):
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.graph10.add_plot(self.plot)
        Clock.schedule_interval(self.plot_value, 1)
        Clock.schedule_interval(self.get_value, 1)
        Clock.schedule_interval(self.get_average, 5)
        Clock.schedule_once(self.sesh_end, 610)
        self.ids.obs_text10.text = "Observing Posture"

        global file_counter
        file_counter = 1
        while True:
            if os.path.isfile(os.path.join(postxt, 'data/datafile{0}.txt'.format(file_counter))):
                file_counter += 1
            else:
                open(os.path.join(postxt,('data/datafile{0}.txt'.format(file_counter))),"w+")
                break
        

    def sesh_end (self,dt):
        self.manager.current = "post_sesh_page10"
        Clock.unschedule(self.plot_value, 0.5)
        Clock.unschedule(self.get_average, 1)
        Clock.unschedule(self.get_value, 0.5)
        post_sesh_timer10()

    def plot_value(self, dt):
        print(3)
        self.plot.points = [(x, float(y)) for x, y in enumerate(open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))).readlines(4000))]

    def get_value(self, dt):
        z_inclination = ''
        clientsocket, address = s.accept()

        while True:
            content = clientsocket.recv(8)
            if len(content) ==0:
                break
            z_inclination += content.decode("utf-8")
            print(1)
        clientsocket.close()
        posturedata = open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter)), "a")
        posturedata.write(z_inclination)
        posturedata.write("\n")

    def get_average(self, dt):
        with open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))) as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter
            for line in fh:
                count += 1 # increment the counter
                sum += float(line.split()[0]) # add here, not in a nested loop
            average = round((sum / count),2)
            self.ids.ave_text10.text = ('Average: {0}'.format(average))

class ScanningPage15(Screen):
    
    a= PostSeshPage15()
    call_pp15 = a.post_graphh

    def exit(self):
        # self.manager.transition.direction= 'right'
        self.manager.current = "main_page"
        Clock.unschedule(self.plot_value)
        Clock.unschedule(self.get_value)
        Clock.unschedule(self.get_average)

    def __init__(self, **kwargs):
        super(ScanningPage15, self).__init__(**kwargs)
        # self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def graphh(self):
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.graph15.add_plot(self.plot)
        Clock.schedule_interval(self.plot_value, 1)
        Clock.schedule_interval(self.get_value, 1)
        Clock.schedule_interval(self.get_average, 5)
        Clock.schedule_once(self.sesh_end, 910)
        self.ids.obs_text15.text = "Observing Posture"

        global file_counter
        file_counter = 1
        while True:
            if os.path.isfile(os.path.join(postxt, 'data/datafile{0}.txt'.format(file_counter))):
                file_counter += 1
            else:
                open(os.path.join(postxt,('data/datafile{0}.txt'.format(file_counter))),"w+")
                break
        

    def sesh_end (self,dt):
        self.manager.current = "post_sesh_page15"
        Clock.unschedule(self.plot_value, 0.5)
        Clock.unschedule(self.get_average, 1)
        Clock.unschedule(self.get_value, 0.5)
        post_sesh_timer15()

    def plot_value(self, dt):
        print(3)
        self.plot.points = [(x, float(y)) for x, y in enumerate(open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))).readlines(6000))]

    def get_value(self, dt):
        z_inclination = ''
        clientsocket, address = s.accept()

        while True:
            content = clientsocket.recv(8)
            if len(content) ==0:
                break
            z_inclination += content.decode("utf-8")
            print(1)
        clientsocket.close()
        posturedata = open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter)), "a")
        posturedata.write(z_inclination)
        posturedata.write("\n")

    def get_average(self, dt):
        with open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))) as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter
            for line in fh:
                count += 1 # increment the counter
                sum += float(line.split()[0]) # add here, not in a nested loop
            average = round((sum / count),2)
            self.ids.ave_text15.text = ('Average: {0}'.format(average))

class ScanningPage20(Screen):
    
    a= PostSeshPage20()
    call_pp20 = a.post_graphh

    def exit(self):
        # self.manager.transition.direction= 'right'
        self.manager.current = "main_page"
        Clock.unschedule(self.plot_value)
        Clock.unschedule(self.get_value)
        Clock.unschedule(self.get_average)

    def __init__(self, **kwargs):
        super(ScanningPage20, self).__init__(**kwargs)
        # self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def graphh(self):
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.ids.graph20.add_plot(self.plot)
        Clock.schedule_interval(self.plot_value, 1)
        Clock.schedule_interval(self.get_value, 1)
        Clock.schedule_interval(self.get_average, 5)
        Clock.schedule_once(self.sesh_end, 1210)
        self.ids.obs_text20.text = "Observing Posture"

        global file_counter
        file_counter = 1
        while True:
            if os.path.isfile(os.path.join(postxt, 'data/datafile{0}.txt'.format(file_counter))):
                file_counter += 1
            else:
                open(os.path.join(postxt,('data/datafile{0}.txt'.format(file_counter))),"w+")
                break
        

    def sesh_end (self,dt):
        self.manager.current = "post_sesh_page20"
        Clock.unschedule(self.plot_value, 0.5)
        Clock.unschedule(self.get_average, 1)
        Clock.unschedule(self.get_value, 0.5)
        post_sesh_timer20()

    def plot_value(self, dt):
        print(3)
        self.plot.points = [(x, float(y)) for x, y in enumerate(open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))).readlines(8000))]

    def get_value(self, dt):
        z_inclination = ''
        clientsocket, address = s.accept()

        while True:
            content = clientsocket.recv(8)
            if len(content) ==0:
                break
            z_inclination += content.decode("utf-8")
            print(1)
        clientsocket.close()
        posturedata = open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter)), "a")
        posturedata.write(z_inclination)
        posturedata.write("\n")

    def get_average(self, dt):
        with open(os.path.join(postxt,'data/datafile{0}.txt'.format(file_counter))) as fh:
            sum = 0 # initialize here, outside the loop
            count = 0 # and a line counter
            for line in fh:
                count += 1 # increment the counter
                sum += float(line.split()[0]) # add here, not in a nested loop
            average = round((sum / count),2)
            self.ids.ave_text20.text = ('Average: {0}'.format(average))



class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__=="__main__":
    MainApp().run()
