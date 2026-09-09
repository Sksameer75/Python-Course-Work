class Instagram:
    def __init__(self,username,password,post):
        self.username = username
        self.__password = password
        self._post = []
        
    def accesspwd(self):
        return self.__password
    
    def updatepwd(self,newpwd):
        self.__password = newpwd

    @property
    def posts(self):
        return self._post

    @posts.setter
    def postsupdate(self,newpost):
        self._post.append(newpost)

sameer = Instagram("Sameer",'1234556','50')
print(sameer.username)
print(sameer.accesspwd())
print(sameer.posts)

sameer.username = 'sameer_123'
print(sameer.username)

sameer.updatepwd("sameer@123")
print(sameer.accesspwd())

sameer.postsupdate = 'python'
sameer.postsupdate = 'java'
print(sameer.posts)
