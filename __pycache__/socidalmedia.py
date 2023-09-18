# creating social media user class which will have name and email id for each user
class User: # class concepts of OPPS
    def __init__(self, username, email_id): #constructor concept of OPPS
        self.name = username 
        self.email_id = email_id
        #creating empty list to store different kind of the post like video, text, image etc for user to store his/her new posts
        self.posts = [] 

    # defining another function just to add newly created post of a user to container posts
    def add_post(self, post):
        self.posts.append(post)
    
class Comment: # defning another class 
    def __init__(self, text, user): #constructor the opps concept
        self.text = text # making a container to store the value of text to container with name text in the container self.text
        self.user = user

class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_post(self,):
        print(f"Post by: {self.content}")
        print("Comments")

        for comment in self.comments:
            print(f": ")

class Text_Post(Post): # another concept of opps, inheretance
    def __init__(self, content, user):
        super().__init__(content, user)

class  Image_Post(Post):
    def __init__(self, content, user, image_url):
        super().__init__(content, user)
        self.image_url = image_url

class Video_Post(Post):
    def __init__(self, content, user, video_url):
        super().__init__(content, user)
        self.video = video_url


# creating instance of the User class or creating real life object of User class
user1 = User("user1", "user1@gmail.com")
user2 = User("user2", "user2@gmail.com")

# creating instanc of the text post class
text_post = Text_Post("This is post for user1", user1)

# creating instance of the image post
image_post = Image_Post("This is image post for user2", user2, "The url is here")

#creating instance of the video post
video_post = Video_Post("This is video post of user1", user1, "The url is here")

# creating instance of the comment post
comment1 = Comment("Nice post!", user1)
comment2 = Comment("Great pose!", user2)

# adding comment to post
text_post.add_comment(comment1)

# adding image to post
image_post.add_comment(comment2)

# creating relation between user and the post
user1.add_post(text_post)
user2.add_post(image_post)

# Display posts and comments
text_post.display_post()
image_post.display_post()
video_post.display_post()
