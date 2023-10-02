import pygame
import webbrowser
class TEXTBUTTON:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2] and mouse_y > self.position[1] and mouse_y < self.position[1] + self.text_box[3]:
			return True
		else:
			return False

	def draw(self):
		font = pygame.font.SysFont('sans',30)
		text_render = font.render(self.text, True, (0,0,255))
		self.text_box = text_render.get_rect()

		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, (0,0,255))
			pygame.draw.line(screen, (0,0,255), (self.position[0], self.position[1] + self.text_box[3]), (self.position[0]+self.text_box[2], self.position[1] + self.text_box[3]))
		else:
			text_render = font.render(self.text, True, (0,0,0))

		screen.blit(text_render,self.position)

class Playlist:
	def __init__(self,name,discription,rating,videos):
		self.name=name
		self.discription = discription
		self.rating = rating
		self.videos = videos
	
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False
	def open(self):
		webbrowser.open(self.link,new =2)
		self.seen = True

def read_playlist_from_txt(file):
		name = file.readline()
		discription = file.readline()
		rate = file.readline()
		videos = read_videos_from_txt(file)
		playlist = Playlist(name,discription,rate,videos)
		return playlist
def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		title = file.readline()
		link = file.readline()
		video = Video(title,link)
		videos.append(video)
	return videos	
def draw_and_check_mouse(random_button):
	random_button.draw()
	random_button.is_mouse_on_text()


def read_playlists_from_txt():
	playlists =[]
	with open("youtube.txt","r") as file:
		total = file.readline()
		for i in range(int(total)):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
		return playlists	
playlists =read_playlists_from_txt()
def playlists_name_button(playlists):
	playlists_name_button = []
	for i in range(len(playlists)):
		playlist_button = TEXTBUTTON("playlist number "+str(i+1)+": "+playlists[i].name.rstrip(),(200,150+50*i))
		playlists_name_button.append(playlist_button)
	return playlists_name_button
playlists_name_button = playlists_name_button(playlists)

def video_name_button(playlist):
	videos_name_button =[]
	for i in range(len(playlist.videos)):
		video_button = TEXTBUTTON("video number "+str(i+1)+": "+playlist.videos[i].title.rstrip(),(600,150+50*i))
		videos_name_button.append(video_button)
	return videos_name_button

pygame.init()
screen = pygame.display.set_mode((1500, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEn =(0,255,0)
BLACK =(0,0,0)
RED = (255,0,0)
WHiTE =(236, 240, 241)
back_ground = WHiTE
color_of_the_box =(RED)
text_color =(BLACK)


# playlist_picture = pygame.image.load("platy_list_name.jpg")
# playlist_picture_rect =playlist_picture.get_rect()

# video_button = []


clock = pygame.time.Clock()
while running:
	clock.tick(60)
	screen.fill(back_ground)

	for i in range(len(playlists_name_button)):
		draw_and_check_mouse(playlists_name_button[i])
	try:
		for i in range(len(video_button)):
			draw_and_check_mouse(video_button[i])
	except:
		pass		
	
	for event in pygame.event.get():
		if event.type ==pygame.MOUSEBUTTONDOWN:
			if event.button ==1:
				for i in range(len(playlists)):
					if playlists_name_button[i].is_mouse_on_text():
						video_button= video_name_button(playlists[i])
						playlist_choice = i

				
				if playlist_choice!= None:
					for i in range(len(video_button)):
						if video_button[i].is_mouse_on_text():
							playlists[playlist_choice].videos[i].open()		
		if event.type == pygame.QUIT:
			running = False
	pygame.display.flip()

pygame.quit()