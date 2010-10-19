import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):
    def get(self):
    	self.response.out.write('<html><body>' )
        self.response.out.write('</html></body>')

class Guestbook(webapp.RequestHandler):

	def post(self):
		str1 = self.request.get('name')
		fin_color=self.map_color(eval(str1))
		self.response.out.write(fin_color)

	def map_color(self,list1):
		def adj_matrix(l):
                        i=0
                        matrix=[]
                        for x in l:
                                list2=[0]*len(l)
                                for y in x:
                                        list2[y]=1
                                matrix.append(list2)
                        return matrix

                def find_color(mat):
        		color={}
        		colors = [1, 2, 3, 4, 5, 6, 7, 8]
        		i=0
        		while i<len(mat):
                		k=0
                		color[i]=colors[k]
                		k+=1
                		j=0
                		while j<i:
                        		if color[i]==color[j] and mat[i][j]==1:
                                		color[i]=colors[k]
                                		k+=1
                                		j=0
                        		else:
                                		j+=1
				i+=1
        		return color

        	adjmat=adj_matrix(list1)
        	color=find_color(adjmat)
        	fin_color=[0]*len(list1)
	        for x in color:
        	        fin_color[x]=color[x]
        	return fin_color
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/a', Guestbook)]
                                     )
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
