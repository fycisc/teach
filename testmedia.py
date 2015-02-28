__author__ = 'feiyicheng'
import pyglet

def playCelebrate():
	media = pyglet.resource.media('believe_in_yourself.mp3')
	media.play()

	pyglet.app.run()

def playNotify():
	media = pyglet.resource.media( 'hhh.mp4' )
	media.play( )

	pyglet.app.run( )


