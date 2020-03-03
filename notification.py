## Install
# pip install -I https://github.com/kivy/plyer/zipball/master

from plyer import notification

notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_name='Here is the application name',
    #app_icon='path/to/the/icon.png'
)