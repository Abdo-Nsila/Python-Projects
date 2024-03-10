# from win10toast import ToastNotifier
# notify1 = ToastNotifier()
# notify1.show_toast("Title" , "You are Cracked HHHH ! " , duration=5)


#* More customized
from winotify import Notification , audio
# customize (:
notify2 = Notification(app_id="Remember",
                       title="Important info",
                       msg="You have a Quiz now !",
                       duration="long",
                       icon="tanjiro.png")
notify2.set_audio(audio.Default,loop=False)
notify2.add_actions(label="Click me",launch="http://le3zawa.somee.com/")
notify2.show()
